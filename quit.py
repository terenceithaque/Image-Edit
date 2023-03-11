# Allow user to quit app

from tkinter import messagebox

def quit(master_window):
    "Quit app"
    user_confirm = messagebox.askyesno("Confirm quit", "Do you really want to quit Image-Edit ? Unsaved data will be lost.") # Ask user if he really wants to quit the app
    if user_confirm:
      master_window.destroy()
