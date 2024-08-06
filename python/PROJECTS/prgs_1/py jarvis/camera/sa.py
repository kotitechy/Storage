import pyaudio
import wave
import threading
import sys

# Define parameters for audio recording
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
WAVE_OUTPUT_FILENAME = "recorded_audio.wav"

# Flag to indicate whether to continue recording
keep_recording = True

def record_audio():
    global keep_recording
    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open stream
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")

    frames = []

    # Record audio until keep_recording is set to False
    while keep_recording:
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    # Stop stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded audio to qa file
    with wave.open(WAVE_OUTPUT_FILENAME, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print("Audio saved to", WAVE_OUTPUT_FILENAME)

# Start recording in a separate thread
record_thread = threading.Thread(target=record_audio)
record_thread.start()

# Wait for 'q' key press to stop recording
print("Press 'q' to stop recording.")
while True:
    key_press = input()
    if key_press.lower() == 'q':
        keep_recording = False
        break

# Wait for the recording thread to finish
record_thread.join()

print("Recording stopped.")
