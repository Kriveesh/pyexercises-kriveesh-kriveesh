"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In:First name, last name, date of birth, and student number.
# 2. Process: Check the inputs and append one student entry.
#    Create the header only when the file is missing or empty.
#    Ask again if a value is invalid.
# 3. Out, file name and columns:student_data.csv
#    Columns: First Name, Last Name, Date of Birth, Student Number.
# 4. Why these columns, and what this file is for:These columns identify students and record their birthdays.
#    With 200 entries, I could search by student number
#    or organise students by birth month.



# Your code below
import csv
import os
from datetime import datetime


print("Please fill in the following details:")

first_name = input("First Name: ").strip()
while first_name == "":
    first_name = input("First name cannot be empty. Enter again: ").strip()

last_name = input("Last Name: ").strip()
while last_name == "":
    last_name = input("Last name cannot be empty. Enter again: ").strip()

while True:
    birth = input("Date of Birth (DD/MM/YYYY): ").strip()
    try:
        birth_date = datetime.strptime(birth, "%d/%m/%Y")
        if birth_date.date() <= datetime.today().date():
            break
        print("Date of birth cannot be in the future.")
    except ValueError:
        print("Enter a valid date in DD/MM/YYYY format.")

student_number = input("Student Number: ").strip()
while student_number == "":
    student_number = input("Student number cannot be empty. Enter again: ").strip()

filename = "student_data.csv"
needs_header = (
    not os.path.exists(filename)
    or os.path.getsize(filename) == 0
)

with open(filename, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    if needs_header:
        writer.writerow([
            "First Name", "Last Name", "Date of Birth", "Student Number"
        ])

    writer.writerow([first_name, last_name, birth, student_number])

print("Data saved successfully!")