"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt (found by reading it, not by guessing):
# - # - There are two blank lines.
# - Some names have spaces at the beginning.
# - Capital letters are inconsistent, for example "ada LOVELACE".
# - The names are not sorted by last name.

# 1. In:Names read from names.txt, one name per line.
# 2. Process, problem by problem:#    Skip blank lines.
#    Remove extra spaces using split() and join().
#    Correct capitalisation using title(), keeping "van" lowercase.
#    Sort the cleaned names by surname.
# 3. Out: names_cleaned.txt, containing eight sorted names.
#    The original names.txt is not changed.
# 4. How I decide which word is the last name:I assume the first word is the first name.
#    Everything after it is the surname.
#    For example, Guido has the surname "van Rossum".
#    Names alone cannot prove this rule, but it fits this file.


# Your code below
# Read the original file without changing it.
with open("names.txt", "r", encoding="utf-8") as file:
    original_lines = file.readlines()


# Remove blank lines and clean the names.
cleaned_names = []
blank_lines = 0

for line in original_lines:
    name = " ".join(line.split())

    if name == "":
        blank_lines = blank_lines + 1
        continue

    name = name.title()
    name = name.replace(" Van ", " van ")
    cleaned_names.append(name)


# Use everything after the first word as the sorting key.
def get_last_name(name):
    return name.split(" ", 1)[1].lower()


# Sort the names by surname.
cleaned_names.sort(key=get_last_name)


# Save the cleaned names to a different file.
with open("names_cleaned.txt", "w", encoding="utf-8") as file:
    for name in cleaned_names:
        file.write(name + "\n")


# Display counts so the difference can be checked.
print("Original lines:", len(original_lines))
print("Blank lines removed:", blank_lines)
print("Output lines:", len(cleaned_names))
print("First name:", cleaned_names[0])
print("Last name:", cleaned_names[-1])

# Expected: 10 original lines, 2 blank lines removed, 8 output lines.
# First entry: Margaret Hamilton.
# Last entry: Guido van Rossum, because the full surname starts with "van".