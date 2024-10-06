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
import customtkinter as ctk

ctk.set_appearance_mode("light") 
ctk.set_default_color_theme("blue") 
 
root = ctk.CTk()
root.title("Colour Picker")

window_width = 300
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#newline = ctk.CTkLabel(root, text="\n   ")
#newline.pack()

title_label = ctk.CTkLabel(root, text="\n Colour Picker \n", width=20, height=2)
title_label.pack()

def choose_colour():
    global colour_code
    colour_code = colorchooser.askcolor(title="Choose a colour!")
    if (colour_code[1]):
        chosen_colour.configure(text=f"\n Selected Color: {colour_code[1]}")
        colour_frame.configure(bg_color=colour_code[1], fg_color=colour_code[1])

        #Fix this
        colour_entry = ctk.CTkEntry(root, border_width=2, placeholder_text="test")
        colour_entry.pack()
        colour_entry.insert(0, colour_code[1])

        newline = ctk.CTkLabel(root, text="\n")
        newline.pack()
        
        copy_button = ctk.CTkButton(root, text="Copy to Clipboard", command=copy_to_clipboard)
        copy_button.pack()

def copy_to_clipboard():
    pyperclip.copy(colour_code[1])
    copied_colour = ctk.CTkLabel(root, text="\n Colour copied to clipboard!")
    copied_colour.pack()


choose_colour_button = ctk.CTkButton(root, text="Choose a colour!", command=choose_colour)
choose_colour_button.pack()

chosen_colour = ctk.CTkLabel(root, text="     ")
chosen_colour.pack()

colour_frame = ctk.CTkFrame(root, width=100, height=50)
colour_frame.pack(padx=20, pady=20)

root.mainloop()
