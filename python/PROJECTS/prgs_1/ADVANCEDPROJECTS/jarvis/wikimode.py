def wiki(s):
    import wikipedia as wk
    speak(f'alright providing summary on {s}')
    # q = recognize_speech()
    r = wk.summary(s,sentences=5)
    print('bot : ', r)
    speak(r)

def recognize_speech():
    import speech_recognition as sr
    # Initialize recognizer
    # speak('hello sir')
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        speak('Listening')
        print("Listening...")

        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)

        # Listen for the user's input
        audio_data = recognizer.listen(source)

        print("Recognizing...")

        try:
            # Recognize speech using Google Speech Recognition
            t = recognizer.recognize_google(audio_data)
            text = t.lower()
            print("You said:", text)
        except Exception as e:
            speak('speak again')
        r =  text
        
    return r
def speak(txt):
    import pyttsx3
    # engine
    e = pyttsx3.init()
    e.say(txt)
    e.runAndWait()
    e.stop()

def  wiki_mode():
    while True:
        q = recognize_speech()
        if 'summary' in q:
            r = q.replace('summary on','')
            print(r)
            wiki(r)

wiki_mode()