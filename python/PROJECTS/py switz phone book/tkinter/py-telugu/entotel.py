from googletrans import Translator

def translate_to_telugu(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='te')
    return translation.text

english_text = "Hello, how are you?"
telugu_translation = translate_to_telugu(english_text)
print("Telugu Translation:", telugu_translation)
