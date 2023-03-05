# Script initial
from tkinter import *

window = Tk() # Création de la fenêtre principale

menu_bar = Menu(window) # Création de la barre de menu


file_menu = Menu(menu_bar, tearoff=0) # Création du menu "Fichier"


menu_bar.add_cascade(label = "Fichier", menu = file_menu) # Intégrer le menu "Fichier" à la barre de menu
window.config(menu = menu_bar)

window.mainloop() # Lancer le programme