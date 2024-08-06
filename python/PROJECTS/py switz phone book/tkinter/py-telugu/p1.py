from google.cloud import texttospeech
from googletrans import Translator
import pyttsx3

def translate_to_telugu(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='te')
    return translated.text

def text_to_speech(text, output_file):
    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="te-IN",
        name="te-IN-Wavenet-A",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    with open(output_file, "wb") as out:
        out.write(response.audio_content)

    print(f'Audio content written to file "{output_file}"')

def main():
    # Get input from the user
    english_text = input("Enter the English text to translate to Telugu and convert to speech: ")

    # Translate to Telugu
    telugu_text = translate_to_telugu(english_text)

    # Print the translated text
    print("Translated text in Telugu:", telugu_text)

    # Convert Telugu text to speech and save it to a WAV file
    output_file = "telugu_speech.wav"
    text_to_speech(telugu_text, output_file)

if __name__ == "__main__":
    main()
