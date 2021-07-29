from gtts import gTTS
from pygame import mixer
import os.path

directory = input("Enter the directory of the file: ")

path = os.path.isfile(directory)

if path == True:
    print("File is load...")
    file_data = open(directory)

    file_data = file_data.read()
    print("Save file...")

    audio_data = gTTS(text=file_data, lang='pt')
    audio_data.save("audio.mp3")

    print("Speak...")

    mixer.init()
    mixer.music.load('audio.mp3')
    mixer.music.play()

else:
    print("File not found")
