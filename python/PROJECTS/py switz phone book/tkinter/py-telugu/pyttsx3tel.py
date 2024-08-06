def translate_to_telugu(text):
    from googletrans import Translator
    translator = Translator()
    translation = translator.translate(text, src='en', dest='te')
    r = translation.text
    return r

def text_to_speech_telugu(text):
    import pygame
    from gtts import gTTS

    tts = gTTS(text=text, lang='te')
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

txt = input('Enter sentence : ')
telugu_text = translate_to_telugu(txt)
text_to_speech_telugu(telugu_text)
