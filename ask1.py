import tkinter as tk

def show_custom_dialog():
    def on_yes():
        print("Confirmed!")
        dialog.destroy()

    def on_no():
        print("Cancelled!")
        dialog.destroy()

    dialog = tk.Toplevel(root)
    dialog.title("Confirmation")
    dialog.geometry("300x150")
    dialog.grab_set()

    tk.Label(dialog, text="Are you sure?", font=("Arial", 16)).pack(pady=20)

    btn_frame = tk.Frame(dialog)
    btn_frame.pack()

    tk.Button(btn_frame, text="Yes", font=("Arial", 12), width=10, command=on_yes).pack(side="left", padx=10)
    tk.Button(btn_frame, text="No", font=("Arial", 12), width=10, command=on_no).pack(side="right", padx=10)

root = tk.Tk()
tk.Button(root, text="Do Something", command=show_custom_dialog).pack(pady=30)
root.mainloop()
