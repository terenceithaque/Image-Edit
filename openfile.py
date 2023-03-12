# Open image file

from tkinter import filedialog, messagebox, Label # Import file dialog and  messagebox modules, and Label widget
from PIL import ImageTk # Importer le module ImageTk de PIL


def showImage(label, file):
        "Show opened image"
        global image

        image = ImageTk.PhotoImage(file = file)

        label.config(image = image)
        label.image = image    
        

def OpenFile(label, master_window):
    "Ask for a file to open"
    try:
        file = filedialog.askopenfilename(initialdir= "C:", filetypes= [("Fichiers image", (".jpg", ".png"))]) # Ask user what file to open
        master_window.title("{} - Image-Edit".format(file))
    
        showImage(label = label,file = file)

    except FileNotFoundError:
        messagebox.showerror("Fichier introuvable", "le fichier {} est introuvable".format(file))

       
