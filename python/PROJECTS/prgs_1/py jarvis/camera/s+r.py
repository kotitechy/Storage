import cv2
import pyaudio
import wave
import threading

# Define parameters for video recording
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
FPS = 30
VIDEO_OUTPUT_FILENAME = "recorded_video.avi"
VIDEO_CODEC = cv2.VideoWriter_fourcc(*'XVID')

# Define parameters for audio recording
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
AUDIO_OUTPUT_FILENAME = "recorded_audio.wav"

# Flags to indicate whether to continue recording
keep_recording_audio = threading.Event()
keep_recording_audio.set()
keep_recording_video = threading.Event()
keep_recording_video.set()

def record_audio():
    global keep_recording_audio
    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open stream
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("Recording audio...")

    frames = []

    # Record audio until keep_recording_audio is set to False
    while keep_recording_audio.is_set():
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording audio.")

    # Stop stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to a file
    with wave.open(AUDIO_OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print("Audio saved to", AUDIO_OUTPUT_FILENAME)

def record_video():
    global keep_recording_video
    # Initialize video writer
    video_writer = cv2.VideoWriter(VIDEO_OUTPUT_FILENAME, VIDEO_CODEC, FPS, (FRAME_WIDTH, FRAME_HEIGHT))

    # Initialize camera
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Error: Couldn't open camera.")
        exit()

    print("Recording video...")

    # Record video until keep_recording_video is set to False
    while keep_recording_video.is_set():
        ret, frame = camera.read()

        if not ret:
            print("Error: Couldn't capture frame.")
            break

        video_writer.write(frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    print("Finished recording video.")

    # Release resources
    camera.release()
    video_writer.release()
    cv2.destroyAllWindows()

# Start recording audio and video in separate threads
audio_thread = threading.Thread(target=record_audio)
video_thread = threading.Thread(target=record_video)
audio_thread.start()
video_thread.start()

# Wait for 'q' key press to stop recording
print("Press 'q' to stop recording.")
while True:
    key_press = input()
    if key_press.lower() == 'q':
        keep_recording_audio.clear()
        keep_recording_video.clear()
        break

# Wait for the recording threads to finish
audio_thread.join()
video_thread.join()

print("Recording stopped.")
