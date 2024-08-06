# jarvis --> simple ai

import pyttsx3 as pt
import datetime as dt
import speech_recognition as sr

engine = pt.init('sapi5')
# get voices in system
voices = engine.getProperty('voices')
print(voices)

# set voice
engine.setProperty('voice', voices[1].id)
# 0--> male , 1 --> female


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(dt.datetime.now().hour)
    if hour >=0 and hour<12:
        speak('Good Morning')

    elif hour >= 12 and hour < 18:
        speak('Good Afternon')

    else:
        speak('Good Night')


def prompt():
    # prompt to perform task -i/p from microphone and text as o/p

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1 # seconds of non-speking time before taking the phase to be completed

        audio = r.listen(source)
        # 
        try:
            print('Reconizing...')
            q = r.recognize_google(audio, language='en-in')
            print(f'user said: {q} \n ') 
        except Exception as e:
            print(e)
            print('Say That again!')
    

speak('Hi Sir Iam jarvis')
audio = 'hello shiva'
speak(audio)
prompt()

