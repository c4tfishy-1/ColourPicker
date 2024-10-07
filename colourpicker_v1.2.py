#This code was written by c4tfishy_1 in order to improve my understanding of the Python standard GUI, Tkinter. 
#Other modules used include Pyperclip and the colorchooser package included in Tkinter. 
#Variable names are written in Australian English, hence the usage of "colour" rather thann "color".
#The author would like to take this opportunity to apologise to North Americans confused by this. 
#It is what it is ¯\_(ツ)_/¯
#Once copied to clipboard, your chosen colour can be pasted as a hexadecimal string anywhere, eg. a web browser or document. 
#Enjoy!

import tkinter as tk
from tkinter import colorchooser
import pyperclip
import customtkinter as ctk

ctk.set_appearance_mode("light") 
ctk.set_default_color_theme("dark-blue") 

root = ctk.CTk()
root.title("Colour Picker")

window_width = 700
window_height = 550

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

nothing = ctk.CTkLabel(root, text="       ")
nothing.pack()

switch_state = 0

def switch_mode():
    global switch_state
    switch_state = 1 - switch_state
    if (switch_state == 0):
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

choose_appearance_mode_button = ctk.CTkButton(root, text="Switch appearance mode (light/dark)", command=switch_mode)
choose_appearance_mode_button.pack()

title_label = ctk.CTkLabel(root, text="\n Colour Picker \n", width=20, height=2)
title_label.pack()

note = ctk.CTkLabel(root, text="Choose a colour with the below button to make the colour codes appear in the boxes above it.")
note.pack()

colour_entry = ctk.CTkEntry(root, border_width=2, placeholder_text="Hex Code")
colour_entry.pack()

rgb_entry = ctk.CTkEntry(root, border_width=2, placeholder_text="RGB Value")
rgb_entry.pack()

def choose_colour():
    global colour_code
    colour_code = colorchooser.askcolor(title="Choose a colour!")
    if colour_code[1]:
        chosen_colour.configure(text=f"\n Selected Color (hexadecimal): {colour_code[1]}")
        colour_frame.configure(bg_color=colour_code[1], fg_color=colour_code[1])

        colour_entry.delete(0, tk.END)
        colour_entry.insert(0, colour_code[1])

        rgb_string = f"RGB = {tuple(int(colour_code[1].lstrip('#')[i:i+2], 16) for i in (0, 2, 4))}"
        rgb_entry.delete(0, tk.END)
        rgb_entry.insert(0, rgb_string)
        chosen_colour_rgb.configure(text=f"\n Selected Color (RGB): {rgb_string}")

def copy_to_clipboard():
    pyperclip.copy(colour_entry.get())
    show_copied_message("Hexadecimal colour code copied to clipboard!")

def copy_to_clipboard_rgb():
    pyperclip.copy(rgb_entry.get())
    show_copied_message("RGB colour code copied to clipboard!")

def show_copied_message(message):
    copied_colour = ctk.CTkLabel(root, text=message)
    copied_colour.pack()
    root.after(10000, copied_colour.destroy)  # Remove message after 10 seconds

choose_colour_button = ctk.CTkButton(root, text="Choose a colour!", command=choose_colour)
choose_colour_button.pack()

chosen_colour = ctk.CTkLabel(root, text="     ")
chosen_colour.pack()

chosen_colour_rgb = ctk.CTkLabel(root, text="     ")
chosen_colour_rgb.pack()

colour_frame = ctk.CTkFrame(root, width=100, height=50)
colour_frame.pack(padx=20, pady=20)

copy_button = ctk.CTkButton(root, text="Copy Hex to Clipboard", command=copy_to_clipboard)
copy_button.pack()

copy_button_rgb = ctk.CTkButton(root, text="Copy RGB to Clipboard", command=copy_to_clipboard_rgb)
copy_button_rgb.pack()

root.mainloop()
