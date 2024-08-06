from gtts import gTTS
import os

def speak_telugu(text):
    # Create a gTTS object
    tts = gTTS(text=text, lang='te')
    
    # Save the audio to a file
    tts.save("output.mp3")
    
    # Play the audio file
    os.system("start output.mp3")

# Example usage
telugu_text = "నమస్కార, మీరు ఎలా ఉన్నారు?"
speak_telugu(telugu_text)

