import speech_recognition as sr

recon = sr.Recognizer()

with sr.Microphone() as source:
    print("Aguardando conexão...")
    audio = recon.listen(source)
    print(recon.recognize_sphinx(audio))