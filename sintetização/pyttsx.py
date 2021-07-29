import pyttsx3

en = pyttsx3.init()
en.setProperty('rate', 130)
en.setProperty('volume', 0.80)
en.setProperty('voice', b'brazil')
en.say("oi carai!")
en.runAndWait()
