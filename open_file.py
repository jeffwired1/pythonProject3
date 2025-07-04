import tkinter as tk
from tkinter import filedialog

# Create and hide the root window
root = tk.Tk()
root.withdraw()

# Prompt user to choose a file name and location
save_path = filedialog.asksaveasfilename(
    title="Save As",
    defaultextension=".txt",  # Automatically add extension
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
)

# Use the result
if save_path:
    print(f"File will be saved as: {save_path}")
else:
    print("Save operation was canceled.")

