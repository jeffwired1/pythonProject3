import tkinter as tk
from tkinter import filedialog
import csv
from datetime import datetime

# Suppress root window
root = tk.Tk()
root.withdraw()

def find_data(biller, start_date, end_date, max):
    number_withdrawals = 0
    total_amount = 0
    lines = []
    for i in range(num_rows):
        # print(data_list[i])
        if biller in (data_list[i]['Description']):
            if number_withdrawals < max:
                target_date = datetime.strptime((data_list[i]['Date']), "%m/%d/%y")
                if start_date <= target_date <= end_date:
                    number_withdrawals += 1
                    # print(data_list[i])
                    cleaned = (data_list[i]['Amount'])
                    cleaned = float(cleaned.replace("$", "").replace(",", ""))
                    total_amount += cleaned
                    t = target_date.strftime("%m/%d/%Y")
                    # print("    ", t, total_amount)
                    lines.append("    " + str(t) + "   " + str(cleaned))
                    # target_date = datetime.strptime((data_list[i]['Date']), "%m/%d/%y")
                    # if start_date <= target_date <= end_date:
                    # print("OK")

            # print(total)
    return number_withdrawals, total_amount, lines
            # print("Found")

# 📍 Main code starts here
# Open file dialog
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
print(f"Number of rows: {num_rows}")


start_date = datetime.strptime("01/01/24", "%m/%d/%y")
end_date = datetime.strptime("06/30/25", "%m/%d/%y")
cc_total = 0



with open("input.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Biller']}  {row['MAX']}  {row['CC']} ")

        biller = row['Biller']
        file.write("\n")
        file.write(biller + "\n")
        withdrawals, total, lines = find_data(biller, start_date, end_date, int(row['MAX']))
        for line in lines:
            file.write(line + "\n")
        file.write(f"Biller:{biller}, #:{withdrawals}, Total:{total}" + "\n")
        if row['CC'] == "1":
            cc_total += total

file.write("\n")
s = start_date.strftime("%m/%d/%Y")
e = end_date.strftime("%m/%d/%Y")
file.write(f"Start Date:{s}, End Date:{e}" + "\n")
file.write(f"Total Credit Cards = {int(cc_total)}" + "\n")
file.write(f"Total Credit Cards Monthly = {int(cc_total/12)}" + "\n")