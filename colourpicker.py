#This code was written by c4tfishy_1 in order to improve my understanding of the Python standard GUI, Tkinter. 
#Other modules used include Pyperclip and the colorchooser package included in Tkinter. 
#Variable names are written in Australian English, hence the usage of "colour" rather thann "color".
#The author would like to take this opportunity to apologise to North Americans confused by this. 
#It is what it is ¯\_(ツ)_/¯
#Once copied to clipboard, your chosen colour can be pasted as a hexadecimal string anywhere, eg. a web browser or document. 
#Enjoy!

import tkinter as tk
from tkinter import *
from tkinter import colorchooser
import pyperclip

root = tk.Tk()
root.title("Colour Picker")

window_width = 300
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

newline = tk.Label(root, text="\n")
newline.pack()

title_label = tk.Label(root, text="\n Colour Picker \n", borderwidth=1, relief="solid", width=20, height=2, bg="white")
title_label.pack()

def choose_colour():
    global colour_code
    colour_code = colorchooser.askcolor(title="Choose a colour!")
    if (colour_code[1]):
        chosen_colour.config(text=f"\n Selected Color: {colour_code[1]}")
        colour_frame.config(bg=colour_code[1])
        colour_entry = tk.Entry(root, bd=2)
        colour_entry.insert(END, colour_code[1])
        colour_entry.pack()
        newline1 = tk.Label(root, text="\n")
        newline1.pack()
        copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
        copy_button.pack()

def copy_to_clipboard():
    pyperclip.copy(colour_code[1])
    copied_colour = tk.Label(root, text="\n Colour copied to clipboard!")
    copied_colour.pack()


choose_colour_button = tk.Button(root, text="Choose a colour!", width=20, height=2, command=choose_colour)
choose_colour_button.pack()

chosen_colour = tk.Label(root)
chosen_colour.pack()

colour_frame = tk.Frame(root, width=100, height=50)
colour_frame.pack(padx=20, pady=20)

root.mainloop()
