import speech_recognition as sr

def recognize_speech():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Listen for the user's input
        audio_data = recognizer.listen(source)

        print("Recognizing...")

        try:
            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio_data)
            print("You said:", text)
        except Exception as e:
            print(e)

# Call the function to start speech recognition
recognize_speech()
