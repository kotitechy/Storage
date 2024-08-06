import pygame 

def play_song(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Wait for the song to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()

if __name__ == "__main__":
    # Replace the file path with the correct path to your audio file
    song_path = r'C:\Users\ksc11\Music\vs4.mp3'

    try:
        play_song(song_path)
    except Exception as e:
        print(f"An error occurred: {e}")
