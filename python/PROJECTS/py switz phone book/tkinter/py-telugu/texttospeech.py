from gtts import gTTS
import os

def text_to_speech_telugu(text):
    tts = gTTS(text=text, lang='te')
    tts.save("output_telugu.mp3")
    os.system("mpg321 output_telugu.mp3") # For Linux
    # os.system("start output_telugu.mp3") # For Windows

telugu_text = "నమస్తే, మీరు ఎలా ఉన్నారు?"
text_to_speech_telugu(telugu_text)
