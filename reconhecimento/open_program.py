import speech_recognition as sr
import os

print("Eai mano, quer abrir oq ?")

recon = sr.Recognizer()
zap = "https://web.whatsapp.com/"
google = "https://www.google.com.br/"
youtube = "https://www.youtube.com/"
facebook = "https://www.facebook.com/"


with sr.Microphone() as source:
    audio = recon.listen(source)
    site = (recon.recognize_google(audio, language='pt-BR')).lower()

    if site == "zap":
        os.system('start chrome {}'.format(zap))
    elif site == "google":
        os.system('start chrome {}'.format(google))
    elif site == "facebook":
        os.system('start chrome {}'.format(facebook))
    elif site == "youtube":
        os.system('start chrome {}'.format(youtube))
    elif site == "nada":
        print("vai pra bosta entao")
