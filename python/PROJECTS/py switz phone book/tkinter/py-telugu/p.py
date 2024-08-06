from googletrans import Translator

def translate_to_telugu(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='te')
    return translated.text

def main():
    # Get input from the user
    english_text = input("Enter the English text to translate to Telugu: ")

    # Translate to Telugu
    telugu_text = translate_to_telugu(english_text)

    # Print the translated text
    print("Translated text in Telugu:", telugu_text)

if __name__ == "__main__":
    main()
