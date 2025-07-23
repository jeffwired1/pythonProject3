import tkinter as tk
from tkinter import filedialog
import csv
from datetime import datetime

# Suppress root window
root = tk.Tk()
root.withdraw()

def find_data(biller, start_date, end_date):
    number_withdrawals = 0
    total_amount = 0
    for i in range(num_rows):
        # print(data_list[i])
        if biller in (data_list[i]['Description']):
            if number_withdrawals < 12:
                target_date = datetime.strptime((data_list[i]['Date']), "%m/%d/%y")
                if start_date <= target_date <= end_date:
                    number_withdrawals += 1
                    # print(data_list[i])
                    cleaned = (data_list[i]['Amount'])
                    cleaned = float(cleaned.replace("$", "").replace(",", ""))
                    total_amount += cleaned
                    t = target_date.strftime("%m/%d/%Y")
                    print("    ", t, total_amount)
                    # target_date = datetime.strptime((data_list[i]['Date']), "%m/%d/%y")
                    # if start_date <= target_date <= end_date:
                    # print("OK")

            # print(total)
    return number_withdrawals, total_amount
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
num_rows = len(data_list)
print(f"Number of rows: {num_rows}")


start_date = datetime.strptime("01/01/24", "%m/%d/%y")
end_date = datetime.strptime("06/30/25", "%m/%d/%y")
cc_total = 0

biller = "CHASE CARD SERV"
print("\n")
print(biller)
withdrawals, total = find_data(biller, start_date, end_date)
print(f"Biller:{biller}, #:{withdrawals}, Total:{total}")
cc_total += total

biller = "AMERICAN EXPRESS "
print("\n")
print(biller)
withdrawals, total = find_data(biller, start_date, end_date)
print(f"Biller:{biller}, #:{withdrawals}, Total:{total}")
cc_total += total

biller = "FIRST BANKCARD"
print("\n")
print(biller)
withdrawals, total = find_data(biller, start_date, end_date)
print(f"Biller:{biller}, #:{withdrawals}, Total:{total}")
cc_total += total

print("\n")
s = start_date.strftime("%m/%d/%Y")
e = end_date.strftime("%m/%d/%Y")
print(f"Start Date:{s}, End Date:{e}")
print(f"Total Credit Cards = {int(cc_total)}")
print(f"Total Credit Cards Monthly = {int(cc_total/12)}")
