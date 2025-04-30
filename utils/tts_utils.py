from gtts import gTTS
import pygame
import time
from io import BytesIO

pygame.mixer.init()

def speak(text, lang="es"):
    try:
        tts = gTTS(text, lang=lang)
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)

        pygame.mixer.music.load(mp3_fp, namehint='mp3')
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.3)
    except Exception as e:
        print("🗣️ Error speaking:", e)
