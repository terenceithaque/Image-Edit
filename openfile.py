# Ouvrir un fichier image

from tkinter import filedialog, messagebox, Label # Importer le module de communication avec le système de fichiers, les boîtes de dialogue et Label
from PIL import ImageTk # Importer le module ImageTk de PIL



def OpenFile(label):
    "Ouvrir un fichier image"
    try:
        file = filedialog.askopenfilename(initialdir= "C:", filetypes= [("Fichiers image", ".jpg", ".png")]) # Demander à l'utilisateur le fichier à ouvrir
       

        print(file)
        def showImage():
            image = ImageTk.PhotoImage(file = file)
            label.config(image = image)
            label.image = image
            
            



        showImage()

    except FileNotFoundError:
        messagebox.showerror("Fichier introuvable", "le fichier {} est introuvable".format(file))

       
