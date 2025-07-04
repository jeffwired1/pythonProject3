import tkinter as tk
from tkinter import messagebox

def confirm_action():
    answer = messagebox.askyesno(title="Confirmation", message="Are you sure?")
    if answer:
        print("User confirmed.")
    else:
        print("User canceled.")

root = tk.Tk()
root.geometry("200x100")

btn = tk.Button(root, text="Do Something", command=confirm_action)
btn.pack(pady=20)

root.mainloop()