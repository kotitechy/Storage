from gtts import gTTS
text=input("Enter text to sound : ")
language = 'en'
myobj = gTTS(text=mytext, lang=language)
myobj.save("welcome.mp3")

