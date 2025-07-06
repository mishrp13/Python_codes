# Parse a CSV file and print contents.

import csv

csv_file_path=r"C:\python_automation_scripts\python_codes\example.csv"

with open(csv_file_path,mode='r',newline='') as file:
    reader=csv.reader(file)
    for line in reader:
        print(line)

