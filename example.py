import warnings
import json
warnings.filterwarnings("ignore")

from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer

# Fichier configuration
with open("dejavu.cnf") as f:
    config = json.load(f)

if __name__ == '__main__':

	# creation d'un objet de classe Dejavu avec l'argument config
	djv = Dejavu(config)

	# l'argument fingerprint qui permet de créer l'empreinte des fichiers "mp3" dans le dossier "classique"
	djv.fingerprint_directory("mp3", [".mp3"])

	# l'argument recognize qui permet de lancer la reconnaissance
	#song = djv.recognize(FileRecognizer, "mp3/Sean-Fournier--Falling-For-You.mp3")
	#print("From file we recognized: {}\n".format(song))

	# l'argument recognize appelé avec un paramètre de type "microphone"
	secs = 15
	#song = djv.recognize(MicrophoneRecognizer, seconds=secs)
	#if song is None:
	#	print("Nothing recognized -- did you play the song out loud so your mic could hear it? :3 ")
	#else:
	#	print("From mic with %d seconds we recognized: %s\n" % (secs, song))

	#Or use a recognizer without the shortcut, in anyway you would like
	#recognizer = FileRecognizer(djv)
	#song = recognizer.recognize_file("mp3/Josh-Woodward--I-Want-To-Destroy-Something-Beautiful.mp3")
	#print("No shortcut, we recognized: {}\n".format(song))
