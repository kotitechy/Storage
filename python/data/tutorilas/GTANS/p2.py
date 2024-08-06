from gtts import gTTS
import os

def text_to_speech(text, language='en'):
    tts = gTTS(text=text, lang=language)
    tts.save("output.mp3")
    os.system("mpg321 output.mp3") # For Linux
    # os.system("start output.mp3") # For Windows

text = "Hello, how are you?"
text_to_speech(text)