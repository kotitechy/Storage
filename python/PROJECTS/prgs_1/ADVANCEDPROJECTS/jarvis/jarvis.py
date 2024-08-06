# jarvis --> simple ai

import pyttsx3 as pt
import datetime as dt
import speech_recognition as sr 
import wikipedia as wk
from PyDictionary import PyDictionary 
import webbrowser as wb
import os 
import pywhatkit as py


engine = pt.init('sapi5')
# get voices in system
voices = engine.getProperty('voices')
# print(voices)

# set voice
engine.setProperty('voice', voices[0].id)
# 0--> male , 1 --> female

 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(dt.datetime.now().hour)
    if hour >=0 and hour<12:
        speak('Good Morning sir')
        print('Good Morning sir')
        print('how can i help you ')
        speak('how can i help you ')

    elif hour >= 12 and hour < 18:
        speak('Good Afternon sir ')
        print('Good Afternon sir ')
        print('how can i help you ')
        speak('how can i help you ')
        

    else:
        speak('Good evening sir')
        print('Good evening sir')
        print('how can i help you ')
        speak('how can i help you ')
        
def youtube(q):
    speak('what to search on youtube')
    q = recognize_speech()
    wb.open('youtube.com/'+q)
    speak(f'alright opening {q} on google')

def google():
    speak('what to search on google')
    q = recognize_speech()
    speak(f'alright searching {q} on google')
    wb.open('google.com'+q)
    
def stackoverflow():
    speak('ok opening stack over flow ')
    wb.open('stackoverflow.com')

def playmsc():
    # C:\\Users\\SHIVA\\Music\\divine
    msc_dir = "output.mp3"
    print('playing ')
    os.startfile(msc_dir)
def meaning(q):
    dict = PyDictionary()
    speak('whats the word:')
    print('whats the word:')
    q = recognize_speech()
    meaning = dict.meaning(q)
    print(meaning)
    speak(meaning)
def wiki(q):
    speak('what to serch on wikipedia:')
    q = recognize_speech()
    r = wk.summary(q,sentences=3)
    print('bot : ', r)
    speak(r)
def _time():
    tme = dt.datetime.now().strftime("%H:%M:%S")
    print(tme)
    speak(tme)

def _date():
    d1 = dt.datetime.now().year
    d2 = dt.datetime.now().month
    d3 = dt.datetime.now().day
    print(f"{d1}: {d2}: {d3}")
    mon = ['january', 'febraury', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november','december']
    mon1 = [0,1,2,3,4,5,6,7,8,9,10,11]
    for i in mon1:
        if d2 == i:
            print('Month: ',mon[i-1]) 
            d2 = mon[i-1]
    speak(f'its {d1}, {d2}, {d3}')

def week():
    wkdy = dt.datetime.now().weekday()
    print(wkdy)
    wkd = ['monday','tuesday','wednesday','thursday','friday','saturday']
    wkd1 = [0,1,2,3,4,5,6,7]

    for i in wkd1:
        if wkdy == i:
            print("today is : ", wkd[i])
            speak(f"today is : {wkd[i]}")



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
        r =  text.lower()
        
    return r
def watsmsg():
    pnos= {'dad' : '+916300922617','mom' : '+918465965773','sai' : '+919392953796','vamshi' : '+919391457750','group' : 'TIMEPASS'}
    per = ['dad','mom','sai','vamshi']
    nums = ['+916300922617','+918465965773','+919392953796','+919391457750']
    speak('whom do u want to send message')
    # pno = recognize_speech()
    pno= input()
    print(pno)
    speak('whats message')
    msg = recognize_speech()
    print('u want to send message to ',pno, 'and message is ', msg)
    speak('are the details provided correct')
    reply = input()
    if reply == 'yes':
        speak('alright sending text message on watsapp')
        for p in per:
            if p == pno:
                try:
                    print(pnos[p])
                    py.sendwhatmsg_instantly(nums[p.index],msg)
                    speak('message sent')
                except:
                    speak('failed to send message')
            else:
                speak('number not found')
    else:
        watsmsg()
    
def err():
    print('Soryy sir i can get the information/data')
    speak('Soryy sir i can get the information/data')
def answer(q):
    if 'jarvis' in q:
        wish()
    elif 'date' in q:
      _date()
    elif 'time' in q:
      _time()
    elif  'day'in q:
      week()
    elif 'open google'in q:
      google()
    elif 'open stackoverflow' in q:
      stackoverflow()
    elif 'play music'in q:
      playmsc()
    elif 'wikipedia'in q:
      wiki(q)
    elif 'meaning' in q:
        meaning(q)  
    elif 'open youtube' in q:
        youtube(q)
    elif 'message' in q:
        watsmsg()
    
    else: 
        err()


wish()


while True:
    q = recognize_speech()
    answer(q)