"""Exercise 8.0 — Operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Take two values of your choice and display, as a readable table, the result of every
    comparison between them and of the logical combinations of those results.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two values did you pick, and which comparison result surprised you?

WHAT THE AI CANNOT KNOW
    Your two values. Pick a pair where the answer is not obvious: two strings with
    different capitalisation, a number and the same number written as text, or zero and
    an empty string.

CHECK IT YOURSELF
    Predict each result before running. Count how many you got right.

DELIVERABLE
    This file, with your comments and your code.
"""
 
# 1. In: Two strings, "apple" and "Apple".
# 2. Process: Compare them using six comparison operators.
#    Combine comparison results using and, or, and not.
# 3. Out: A readable table showing each expression and its result.
# 4. Chosen values: "apple" and "Apple".
#    A potentially surprising result is "apple" > "Apple".
#    Lowercase "a" has a higher character code than uppercase "A".
#    After running, add which result actually surprised you.

# Your code below

a = "apple"
b = "Apple"

# Predictions: check these yourself before running.
# a == b: False
# a != b: True
# a < b: False
# a > b: True
# a <= b: False
# a >= b: True
# (a > b) and (a != b): True
# (a < b) or (a == b): False
# not (a == b): True

results = [
    ("a == b", a == b),
    ("a != b", a != b),
    ("a < b", a < b),
    ("a > b", a > b),
    ("a <= b", a <= b),
    ("a >= b", a >= b),
    ("(a > b) and (a != b)", (a > b) and (a != b)),
    ("(a < b) or (a == b)", (a < b) or (a == b)),
    ("not (a == b)", not (a == b))
]

print("a =", repr(a))
print("b =", repr(b))
print()
print(f"{'Expression':<28} Result")
print("-" * 35)

for expression, result in results:
    print(f"{expression:<28} {result}")

# After checking, record your own prediction count:
# I predicted ___ out of 9 correctly.