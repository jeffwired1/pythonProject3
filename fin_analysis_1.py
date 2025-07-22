import tkinter as tk
from tkinter import filedialog
import csv

def load_csv_to_dict():
    # Suppress root window
    root = tk.Tk()
    root.withdraw()

    # Open file dialog
    filepath = filedialog.askopenfilename(
        title="Select a CSV File",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )

    if not filepath:
        print("No file selected.")
        return None

    # Read CSV into dictionary
    data_dict = {}
    with open(filepath, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader, None)  # Skip header row if present

        for row in reader:
            if row:
                key = row[0]
                value = row[1:]
                data_dict[key] = value

    return data_dict

# 📍 Main code starts here
csv_data = load_csv_to_dict()
if csv_data:
    print("🔎 Dictionary contents:")
    for key, values in csv_data.items():
        print(f"{key}: {values}")
else:
    print("❌ No data to display.")