from googletrans import Translator

def translate_to_telugu(text):
    translator = Translator()
    translation = translator.translate(text, src='en', dest='hi')
    return translation.text

english_text = "South India is known for its rich cultural heritage and diverse cuisine. India, with its vast landscape, boasts a multitude of languages, traditions, and landscapes, making it a vibrant tapestry of culture and history."
telugu_translation = translate_to_telugu(english_text)
print("Telugu Translation:", telugu_translation)