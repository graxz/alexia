import speech_recognition as sr

recon = sr.Recognizer()

with sr.Microphone() as source:

    while True:
        recon.adjust_for_ambient_noise(source)

        print("Aguardando conexão...")
        audio = recon.listen(source)

        print(recon.recognize_google(audio, language='pt-BR'))
