import csv
import tkinter as tk
import tkinter as tk
from tkinter import filedialog

def get_filename():
    root = tk.Tk()
    root.withdraw()  # Hide main window
    filepath = filedialog.askopenfilename(
        title="Select a File",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    return filepath

# Example usage
filename = get_filename()
if filename:
    print(f"Selected file: {filename}")
else:
    print("No file selected.")

# exit()
def csv_to_dict(filename):
    result = {}
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Skip header row if present

        for row in reader:
            key = row[0]
            value = row[1:]
            result[key] = value

    return result

# Example usage:
data = csv_to_dict(filename)
print(data)

search_term = "CHASE"
matching_rows = [key for key, values in reader.items() if any(search_term in value for value in values)]

print("Matching rows:", matching_rows)