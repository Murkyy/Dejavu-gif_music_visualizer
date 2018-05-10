import warnings
import json
warnings.filterwarnings("ignore")
import os
from os import listdir
import subprocess

from tkinter import *

import time
root=Tk()
root.title("Visualiseur")
root.geometry("%dx%d%+d%+d" % (root.winfo_screenwidth(),root.winfo_screenheight(),0,0))
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
root.overrideredirect(1)
dessin=Canvas(root, width = 1920, height = 1080, bg = "black")
dessin.grid(sticky=NSEW)
dessin.columnconfigure(0,weight=1)
dessin.rowconfigure(0,weight=1)
sv = StringVar()
texte=Label(dessin,textvariable = sv,font=('OpineHeavy', '50'),fg="red",bg="black").grid(sticky=NSEW)
sv.set("Reconnaissance de la musique en cours...")
root.update()




from dejavu import Dejavu
from dejavu.recognize import FileRecognizer, MicrophoneRecognizer


# load config from a JSON file (or anything outputting a python dictionary)
with open("dejavu.cnf") as f:
        config = json.load(f)
        

if __name__ == '__main__':
    
        # create a Dejavu instance

        
        djv = Dejavu(config)
        secs = 7
        print("Reconnaissance de la musique en cours...")

        song = djv.recognize(MicrophoneRecognizer, seconds=secs)
        if song is None:
                print("Nothing recognized -- did you play the song out loud so your mic could hear it? :3 ")
                sv.set("Rien n'a été reconnu, est-ce assez fort? :3")
                root.update()
                time.sleep(5)
                root.destroy()
        else:
                #print("From mic with %d seconds we recognized: %s\n" % (secs, song))
                print("Musique reconnue :",song["song_name"])

                sv.set(song["song_name"])
                root.update()
                time.sleep(5)
                root.destroy()

                                
                path="c:\\Users\Julien\Desktop\dejavu\Type_de_musique\Classique"
                fichiers = os.listdir(path)
                musiques=[]
                for f in fichiers :
                        a=os.path.splitext(f)
                        musiques.append(a[0])
                if song["song_name"] in musiques:
                        print("C'est une musique classique")
                        subprocess.call("py -2.7 visualizer_Classique.py")

                path="c:\\Users\Julien\Desktop\dejavu\Type_de_musique\Rock"
                fichiers = os.listdir(path)
                musiques=[]
                for f in fichiers :
                        a=os.path.splitext(f)
                        musiques.append(a[0])
                if song["song_name"] in musiques:
                        print("C'est une musique Rock")
                        subprocess.call("py -2.7 visualizer_Rock.py")
                        
                path="c:\\Users\Julien\Desktop\dejavu\Type_de_musique\Electro"
                fichiers = os.listdir(path)
                musiques=[]
                for f in fichiers :
                        a=os.path.splitext(f)
                        musiques.append(a[0])
                if song["song_name"] in musiques:
                        print("C'est une musique Electro")
                        subprocess.call("py -2.7 visualizer_Electro.py")
                        
                path="c:\\Users\Julien\Desktop\dejavu\Type_de_musique\Reggae"
                fichiers = os.listdir(path)
                musiques=[]
                for f in fichiers :
                        a=os.path.splitext(f)
                        musiques.append(a[0])
                if song["song_name"] in musiques:
                        print("C'est une musique Reggae")
                        subprocess.call("py -2.7 visualizer_Reggae.py")
            
                path="c:\\Users\Julien\Desktop\dejavu\Type_de_musique\Metal"
                fichiers = os.listdir(path)
                musiques=[]
                for f in fichiers :
                        a=os.path.splitext(f)
                        musiques.append(a[0])
                if song["song_name"] in musiques:
                        print("C'est une musique Metal")
                        subprocess.call("py -2.7 visualizer_Metal.py")

            
            
