# Python writing files (.txt, .json, .csv)
import json
import csv

employee = [["Name", "Age", "Job"],
            ["Spongebob", 30, "Cook"],
            ["Patrick", 37, "Unemployed"],
            ["Sandy", 27, "Scientist"]]

#  file_path = "output.txt"   it will create a new file in our project
file_path = "C:/Users/DELL USER/Desktop/output.csv"    # It will create a file in your locan computer

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employee:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file is already exists!")