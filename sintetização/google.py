from gtts import gTTS
from pygame import mixer

voice = gTTS(text='Hello', lang='pt')
voice.save("hello.mp3")

mixer.init()
mixer.music.load('hello.mp3')
mixer.music.play()

x = input("Digite algo para finalizar... ")
