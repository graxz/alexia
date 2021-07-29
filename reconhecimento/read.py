import speech_recognition as sr

recon = sr.Recognizer()

PATH = 'reconhecimento\Fala.wav'

with sr.AudioFile(PATH) as source:
    audio = recon.record(source)

    print(recon.recognize_sphinx(audio))
