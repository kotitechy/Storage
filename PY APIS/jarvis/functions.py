def speak(txt):
    import pyttsx3
    # engine
    e = pyttsx3.init()
    e.say(txt)
    e.runAndWait()
    e.stop()

def translater():
    from googletrans import Translator
    t = Translator()
    te = input("Enter an sentence: ")
    r = t.translate(te, dest="te")
    print(r)

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
            recognize_speech()
            return 'jarvis'
        r =  text
    # r = input('Enter the sentence : ')
    return r

def wish():
    import datetime as dt
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

        
def _time():
    import datetime as dt
    tme = dt.datetime.now().strftime("%H:%M:%S")
    print(tme)
    speak(tme)

def _date():
    import datetime as dt
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
    import datetime as dt
    wkdy = dt.datetime.now().weekday()
    print(wkdy)
    wkd = ['monday','tuesday','wednesday','thursday','friday','saturday']
    wkd1 = [0,1,2,3,4,5,6,7]

    for i in wkd1:
        if wkdy == i:
            print("today is : ", wkd[i])
            speak(f"today is : {wkd[i]}")

def meaning(q):
    from PyDictionary import PyDictionary 
    dict = PyDictionary()
    speak('whats the word:')
    print('whats the word:')
    q = recognize_speech()
    meaning = dict.meaning(q)
    print(meaning)
    speak(meaning)

def age_calc():
    from datetime import datetime as dt
    born = dt(2005, 4, 27).date()
    current_date = dt.now().date()
    age = current_date.year - born.year - ((current_date.month, current_date.day) < (born.month, born.day))
    print(age)

# print(recognize_speech())
def wiki():
    import wikipedia as wk
    speak('what to serch on wikipedia:')
    q = recognize_speech()
    r = wk.summary(q,sentences=5)
    print('bot : ', r)
    speak(r)

def okgoogle():
    import webbrowser as wb
    speak('search google')
    q = recognize_speech()
    speak(f'alright searching {q} on google')
    wb.open(f'{q}.com')

def opengoogle():
    import webbrowser as wb
    wb.open('google.com')
def facebook():
    import webbrowser as wb
    wb.open('facebook.com')
def twitter():
    import webbrowser as wb
    wb.open('twitter.com')
def stackoverflow():
    import webbrowser as wb
    wb.open('stackoverflow.com')
def instagram():
    import webbrowser as wb
    wb.open('instagram.com')

def watsapp():
    import webbrowser as wb
    wb.open('watsapp.com')

def automate(q):
    s = q.split()
    import webbrowser as wd
    print(s[1])
    s1 = s[1]
    wd.open(s1)


def ext():
    import sys
    speak('ok shutting down the system')
    sys.exit()

def speak_tel(q):
    speak('ok setting lanuage to telugu')
    # eng - tel
    from googletrans import Translator
    translator = Translator()
    translation = translator.translate(q, src='en', dest='te')
    r = translation.text

    # tel txt - speech

    import pygame
    from gtts import gTTS

    tts = gTTS(text=r, lang='te')
    tts.save("output_telugu.mp3")

    # Initialize pygame
    pygame.mixer.init()
    
    # Load the MP3 file
    sound = pygame.mixer.Sound("output_telugu.mp3")

    # Play the audio
    sound.play()

    # Wait for the audio to finish playing
    while pygame.mixer.get_busy():
        pygame.time.Clock().tick(10)

    # Clean up
    pygame.mixer.quit()
    import os
    os.remove("output_telugu.mp3")





def process(q):
    import brain as b
    if  'who are you' in q:
        speak(b.b1.Self)
    elif 'telugu' in q:
        q = recognize_speech()
        speak_tel(q)
    elif 'happy' in q:
        speak(b.b1.laugh)
    elif 'anger' in q:
        speak(b.b1.angry)
    elif 'age' in q :
        age_calc()
    elif 'hunger' in q:
        speak(b.b1.hunger)
    elif 'favourite' in q:
        speak(b.b1.q)
    elif 'confused' in q:
        speak(b.b1.confused)
    elif 'sad' in q:
        speak(b.b1.sad)
    elif 'stress' in q:
        speak(b.b1.stress)
    elif 'irritation' in q:
        speak(b.b1.irritated)
    # elif 'scold' or 'sale' or 'stupid' or 'mental' in q:
        # speak(b.b1.scold)
    elif 'love' in q:
        speak(b.b1.love)
    elif 'beautiful' in q:
        speak(b.b1.romance)
    elif 'pain'in q:
        speak(b.b1.pain)
    elif 'sexy' in q:
        speak(b.b1.lust)
    elif 'jealousy' in q:
        speak(b.b1.jelaousy)
    elif 'cunning' in q:
        speak(b.b1.cunning)
    elif 'statisfied' in q:
        speak(b.b1.satisfaction)
    elif 'motivation' in q:
        speak(b.b1.motivation)
    elif 'nervess' in q:
        speak(b.b1.nervess)
    elif 'shy' in q:
        speak(b.b1.shyness)
    elif 'depress' in q:
        speak(b.b1.depressed)
    elif 'quote' in q:
        speak(b.b1.quote)
    elif 'namaste'in q:
        speak(b.b1.wish)
    elif 'hot' in q:
        speak(b.b1.hot)
    elif 'cold'in q:
        speak(b.b1.cold)
    elif 'sour' in q:
        speak(b.b1.sour)
    elif 'bitter' in q:
        speak(b.b1.bitter)
    elif 'salty' in q:
        speak(b.b1.salty)
    elif 'thank' in q:
        speak(b.b1.thank)
    elif 'goal' in q:
        speak(b.b1.goal)
    elif 'request' in q:
        speak(b.b1.request)
    elif 'father' in q:
        speak(b.b1.father)
    elif 'mother' in q:
        speak(b.b1.mother)
    elif 'questions' in q:
        speak('continue')
    elif 'believe' in q:
        speak(b.b1.belive)
    elif 'inspiration' in q:
        speak(b.b1.inspiration)
    elif 'marry' in q:
        speak(b.b1.secert)
    elif 'sad' in q:
        speak(b.b1.sad)
    elif 'wikipedia' in q:
        wiki()
    elif 'ok google' in q:
        okgoogle()
    elif 'facebook' in q:
        facebook()
    elif 'instagram' in q:
        instagram()
    elif 'stackoverflow' in q:
        stackoverflow()
    elif 'twitter' in q:
        twitter()
    elif 'google.com' in q:
        opengoogle()
    elif 'watsapp' in q:
        watsapp()
    elif 'open' in q:
        automate(q)
    # elif 'stop':
        # ext()
    elif 'date' in q:
      _date()
    elif 'time' in q:
      _time()
    elif  'day'in q:
      week()
    elif 'dictionary' in q:
        meaning(q) 
    elif 'hello jarvis' in q:
        wish()
    elif 'good night' in q:
        speak('good night') 
    else:
        speak('no result')



recognize_speech()