from pocketsphinx import LiveSpeech

for phrase in LiveSpeech():
    print("Voce disse: " + str(phrase))
