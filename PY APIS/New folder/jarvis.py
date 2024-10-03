import pyttsx3 as pt
import datetime as dt
import speech_recognition as sr
import wikipedia as wk
from PyDictionary import PyDictionary
import webbrowser as wb
import os

engine = pt.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # 0--> male, 1 --> female

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = dt.datetime.now().hour
    if hour < 12:
        greet = 'Good Morning sir'
    elif hour < 18:
        greet = 'Good Afternoon sir'
    else:
        greet = 'Good Night sir'
    
    speak(greet)
    print(greet)
    speak('How can I help you?')

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio_data = recognizer.listen(source)

        print("Recognizing...")
        try:
            text = recognizer.recognize_google(audio_data)
            print("You said:", text)
            return text.lower()
        except Exception as e:
            print(e)
            return ""

def google():
    speak('What do you want to search on Google?')
    q = recognize_speech()
    if q:
        speak(f'Alright, searching {q} on Google.')
        wb.open(f'https://www.google.com/search?q={q}')

def youtube():
    speak('What do you want to search on YouTube?')
    q = recognize_speech()
    if q:
        wb.open(f'https://www.youtube.com/results?search_query={q}')
        speak(f'Opening {q} on YouTube.')

def stackoverflow():
    speak('Opening Stack Overflow.')
    wb.open('https://stackoverflow.com')

import os

def play_music():
    music_file = "hello.mp3"  # Assuming hello.mp3 is in the same directory as the script
    
    if os.path.exists(music_file):
        print('Playing:', music_file)
        speak(f'Playing {music_file}')
        os.startfile(music_file)
    else:
        speak("No music file found.")


def meaning():
    dict = PyDictionary()
    speak('What word do you want the meaning of?')
    q = recognize_speech()
    if q:
        meaning = dict.meaning(q)
        if meaning:
            print(meaning)
            speak(f'The meaning of {q} is: {meaning}')
        else:
            speak("Sorry, I couldn't find the meaning.")

def wiki():
    speak('What do you want to search on Wikipedia?')
    q = recognize_speech()
    if q:
        try:
            summary = wk.summary(q, sentences=3)
            print('Bot:', summary)
            speak(summary)
        except Exception as e:
            speak("Sorry, I couldn't find any information on Wikipedia.")

def tell_time():
    current_time = dt.datetime.now().strftime("%H:%M:%S")
    print(current_time)
    speak(current_time)

def tell_date():
    today = dt.datetime.now()
    date_string = today.strftime("%Y-%m-%d")
    print(date_string)
    speak(f'Today is {date_string}')

def tell_weekday():
    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    today = dt.datetime.now().weekday()
    print(f"Today is: {week_days[today]}")
    speak(f"Today is: {week_days[today]}")

def handle_command(command):
    if 'jarvis' in command:
        wish()
    elif 'date' in command:
        tell_date()
    elif 'time' in command:
        tell_time()
    elif 'day' in command:
        tell_weekday()
    elif 'open google' in command:
        google()
    elif 'open stackoverflow' in command:
        stackoverflow()
    elif 'play music' in command:
        play_music()
    elif 'wikipedia' in command:
        wiki()
    elif 'meaning' in command:
        meaning()
    elif 'open youtube' in command:
        youtube()
    else:
        speak("Sorry sir, I can't get that information.")

wish()

while True:
    command = recognize_speech()
    if command:
        handle_command(command)
