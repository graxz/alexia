import pyttsx3
from datetime import datetime

now = datetime.now()
name = "mano"
hour = now.hour
minute = now.minute

time = "Eai " + name + " agora são " + str(hour) + ":" + str(minute)

en = pyttsx3.init()
en.setProperty('rate', 130)
en.setProperty('volume', 0.80)
en.setProperty('voice', b'brazil')
en.say(time)
en.runAndWait()
