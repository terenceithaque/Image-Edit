# Initial script
from tkinter import *
from openfile import *
from quit import *
import keyboard

window = Tk() # Create main window

menu_bar = Menu(window) # Creating app's menu bar

image_label = Label(window)
image_label.pack()



file_menu = Menu(menu_bar, tearoff=0) # Creating "File" menu

file_menu.add_command(label = "Open file  Ctrl + O", command = lambda:OpenFile(image_label,window))
keyboard.add_hotkey("Ctrl + O", lambda : OpenFile(image_label,window))

file_menu.add_command(label = "Quit app Ctrl + Q", command = lambda:quit(window))
keyboard.add_hotkey("Ctrl + Q", lambda:quit(window))


menu_bar.add_cascade(label = "File", menu = file_menu) # Integrate "File" menu to menu bar
window.config(menu = menu_bar)

window.mainloop() # Start window main loop