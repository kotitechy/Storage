import speech_recognition as sr
from googletrans import Translator

def detect_and_translate():
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    # Use default microphone as the audio source
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        
    try:
        # Recognize speech using Google Speech Recognition
        spoken_text = recognizer.recognize_google(audio)
        print("You said:", spoken_text)
        
        # Detect language
        translator = Translator()
        detected_language = translator.detect(spoken_text).lang
        
        # Translate the text to English
        translated_text = translator.translate(spoken_text, dest='en').text
        
        print("Detected language:", detected_language)
        print("Translated text:", translated_text)
        
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    except Exception as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    detect_and_translate()
