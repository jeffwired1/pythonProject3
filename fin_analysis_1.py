import tkinter as tk
from tkinter import filedialog
import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta


# Suppress root window
root = tk.Tk()
root.withdraw()

def find_data(search, start_date, end_date, max):
    number_withdrawals = 0
    total_amount = 0
    lines = []
    for i in range(num_rows):
        # print(data_list[i])
        if search in (data_list[i]['Description']):
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

today = datetime.now()
start_date = today - relativedelta(years=1)
# start_date = datetime.strptime("07/31/24", "%m/%d/%y")
end_date = today
# new_date = start_date - relativedelta(years=1)
print(start_date,end_date,today)

cc_total = 0
cc_average = 0

with open("input.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        search = row['Search']
        name = row['Name']
        file.write("\n")
        file.write(name + "\n")
        withdrawals, total, lines = find_data(search, start_date, end_date, int(row['MAX']))
        for line in lines:
            file.write(line + "\n")
        file.write(f"{name}, #:{withdrawals}, Total:{int(total)},  Average:{int(total/withdrawals)}" + "\n")
        if row['TYPE'] == "CC":
            cc_total += total
            cc_average += total/withdrawals

file.write("\n")
s = start_date.strftime("%m/%d/%Y")
e = end_date.strftime("%m/%d/%Y")
file.write(f"Start Date:{s}, End Date:{e}" + "\n\n")
file.write(f"Total Credit Cards = {int(cc_total)}" + "\n")
file.write(f"Total Credit Cards Average= {int(cc_average)}" + "\n")
file.write(f"Total Credit Cards Monthly = {int(cc_total/12)}" + "\n\n")

