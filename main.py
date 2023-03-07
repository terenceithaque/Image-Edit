# Script initial
from tkinter import *
from openfile import *
import keyboard

window = Tk() # Création de la fenêtre principale

menu_bar = Menu(window) # Création de la barre de menu

image_label = Label(window)
image_label.pack()



file_menu = Menu(menu_bar, tearoff=0) # Création du menu "Fichier"

file_menu.add_command(label = "Ouvrir un fichier  Ctrl + O", command = lambda:OpenFile(image_label))
keyboard.add_hotkey("Ctrl + O", lambda : OpenFile(image_label))

file_menu.add_command(label = "Quitter l'application", command = window.destroy)
keyboard.add_hotkey("Ctrl + Q", window.destroy)


menu_bar.add_cascade(label = "Fichier", menu = file_menu) # Intégrer le menu "Fichier" à la barre de menu
window.config(menu = menu_bar)

window.mainloop() # Lancer le programme