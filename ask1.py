import tkinter as tk
from tkinter import simpledialog, font

class MultiFieldDialog(simpledialog.Dialog):
    def body(self, master):
        self.big_font = font.Font(family="Helvetica", size=14)

        # Name
        tk.Label(master, text="Name:", font=self.big_font).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.name_entry = tk.Entry(master, font=self.big_font)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        # Email
        tk.Label(master, text="Email:", font=self.big_font).grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.email_entry = tk.Entry(master, font=self.big_font)
        self.email_entry.grid(row=1, column=1, padx=10, pady=5)

        # Age
        tk.Label(master, text="Age:", font=self.big_font).grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.age_entry = tk.Entry(master, font=self.big_font)
        self.age_entry.grid(row=2, column=1, padx=10, pady=5)

        return self.name_entry  # initial focus

    def apply(self):
        self.result = {
            "name": self.name_entry.get(),
            "email": self.email_entry.get(),
            "age": self.age_entry.get()
        }

# Main window
root = tk.Tk()
root.withdraw()  # Hide main window

dialog = MultiFieldDialog(root, title="User Info")
if dialog.result:
    print("Collected Data:")
    for key, value in dialog.result.items():
        print(f"{key.capitalize()}: {value}")
