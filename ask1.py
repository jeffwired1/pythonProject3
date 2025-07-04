import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()  # Hide the main window

user_input = simpledialog.askstring("Input", "What's your name?")
print(f"Hello, {user_input}!")