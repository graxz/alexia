import speech_recognition as sr
import os
import webbrowser

print("Eai mano, quer abrir o zap ?")

recon = sr.Recognizer()
site = "https://web.whatsapp.com/"

with sr.Microphone() as source:
    audio = recon.listen(source)
    aswer = recon.recognize_google(audio, language='pt-BR')

    if aswer == "sim":
        print("abrindo carai...")
        os.system('start chrome {}'.format(site))
    elif aswer == "não":
        print("Tchau")
