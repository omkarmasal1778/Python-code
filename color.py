import tkinter as tk
from tkinter import colorchooser

def change_color():
    # Open the color chooser dialog
    color_code = colorchooser.askcolor(title="Choose color")
    if color_code:
        # Change the background color
        root.configure(bg=color_code[1])

# Create the main window
root = tk.Tk()
root.title("Color Change Program")
root.geometry("400x300")

# Create a button to change the color
color_button = tk.Button(root, text="Change Color", command=change_color)
color_button.pack(pady=20)

# Start the main event loop
root.mainloop()

