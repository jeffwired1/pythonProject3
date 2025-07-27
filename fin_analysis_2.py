import tkinter as tk
from tkinter import filedialog
import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta


# Suppress root window
root = tk.Tk()
root.withdraw()

def find_data(search, start_date, end_date):
    number_withdrawals = 0
    total_amount = 0
    lines = []
    for i in range(num_rows):
        # print(data_list[i])
        if search in (data_list[i]['Description']):
            target_date = datetime.strptime((data_list[i]['Date']), "%m/%d/%y")
            if start_date <= target_date <= end_date:
                number_withdrawals += 1
                cleaned = (data_list[i]['Amount'])
                cleaned = float(cleaned.replace("$", "").replace(",", ""))
                total_amount += cleaned
                t = target_date.strftime("%m/%d/%Y")
                lines.append("    " + str(t) + "   " + str(format(cleaned, ".2f")))
    return number_withdrawals, total_amount, lines

# 📍 Main code starts here
# Open file dialog
# months = 12
filepath = filedialog.askopenfilename(
    title="Select a CSV File",
    filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )

if not filepath:
    print("No file selected.")

# Read CSV into dictionary
with open(filepath, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data_list = list(reader)

# 📍 Main code starts here

file = open("accout.txt", "w")


num_rows = len(data_list)
# print(f"Number of rows: {num_rows}")

cc_total = 0
cc_average = 0

with open("input.csv", newline="") as f:
    lines = f.readlines()

# Split into two header blocks
split_index = None
for i, line in enumerate(lines):
    if line.strip() == "":  # blank line separator
        split_index = i
        break

section1 = lines[:split_index]
section2 = lines[split_index + 1:]  # skip the blank line

options = csv.DictReader(section1)
rows = list(options)
months = float(rows[0]['Months'])
today = datetime.now()
start_date = today - relativedelta(months=months)
end_date = today

# with open("input.csv", newline="") as f:
reader = csv.DictReader(section2)
# reader = csv.DictReader(f)
for row in reader:
    search = row['Search']
    name = row['Name']
    file.write("\n")
    file.write(name + "\n")
    withdrawals, total, lines = find_data(search, start_date, end_date)
    for line in lines:
        file.write(line + "\n")
    total_formatted = format(float(total), ".2f")
    average_formatted = format(float(total/months), ".2f")
    file.write(f"{name}, #:{withdrawals}, Total:{total_formatted},  Average:{average_formatted}" + "\n")
    if row['TYPE'] == "CC":
        cc_total += total
        cc_average += total/months

file.write("\n")
s = start_date.strftime("%m/%d/%Y")
e = end_date.strftime("%m/%d/%Y")
file.write(f"Start Date:{s}, End Date:{e}" + "\n\n")
cc_total_formatted = format(cc_total, ".2f")
cc_average_formatted = format(cc_average, ".2f")
file.write(f"Total Credit Cards = {cc_total_formatted}" + "\n")
file.write(f"Total Credit Cards Monthly = {cc_average_formatted}" + "\n")

