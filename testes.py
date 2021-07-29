import pyttsx3

en = pyttsx3.init()

new_velocity = 50
new_volume = 0.1

while new_velocity <= 300:
    en.setProperty('rate', new_velocity)
    en.say('The quick brown fox jumped over the lazy dog.')
    en.runAndWait()
    new_velocity += 50

while new_volume <= 1:
    en.setProperty('volume', new_volume)
    en.say('The quick brown fox jumped over the lazy dog.')
    en.runAndWait()
    new_volume += 0.1
