"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of ten numbers.
# 2. Process:Create new lists in four different orders.
# 3. Out:The four reordered lists and the unchanged original list.
# 4. My four orders, and which ones modify the original:I chose ascending, descending, reversed, and rotated and none change the original list.


# Your code below
list_of_numbers = [12, 5, 9, 2, 15, 7, 1, 10, 4, 8]

# Smallest to largest
ascending = sorted(list_of_numbers)
print("Ascending:")
print(ascending)

# Largest to smallest
descending = sorted(list_of_numbers, reverse=True)
print("Descending:")
print(descending)

# Reverse the original order
reversed_list = list_of_numbers[::-1]
print("Reversed:")
print(reversed_list)

# Move the first number to the end
rotated = list_of_numbers[1:] + list_of_numbers[:1]
print("Rotated:")
print(rotated)

# Prove that the original list has not changed
print("Original list:")
print(list_of_numbers)