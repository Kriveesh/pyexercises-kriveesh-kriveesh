"""Exercise 9.0 — Surviving what you did not expect

Useful for the final exam: two campaigns in the exam dataset have zero conversions.

WHAT THE PROGRAM MUST DO
    Ask the user for a number, divide something by it, and keep running whatever the
    user types. Never crash.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two different failures can happen here, and should they produce the same
       message to the user? Decide before coding.

WHAT THE AI CANNOT KNOW
    Your answer to question 4, and how many attempts you allow before giving up.

    An assistant will often propose catching every error at once. Find out why catching
    each failure separately is better, and write the reason in a comment.

CHECK IT YOURSELF
    Run it with: a normal number, then zero, then the word "abc", then an empty line.
    Four runs, four behaviours, all described in a comment. If any of them stopped your
    program, it is not finished.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:A number entered by the user.
# 2. Process:Convert the input to a number, then divide 100 by it.
#    If the input is invalid, explain the problem and ask again.
# 3. Out:The division result or a specific error message.
# 4. The two failures, and whether they deserve the same message:ValueError: text or an empty input cannot become a number.
#    ZeroDivisionError: division by zero is not possible.
#    They need different messages because the user must fix different problems.
#    Catching them separately makes the feedback clearer.
#    I allow unlimited attempts until a valid number is entered.


# Your code below
# Ask for input and attempt the calculation.
while True:
    try:
        number = float(input("Enter a number to divide 100 by: "))
        result = 100 / number

    # Handle text and empty input.
    except ValueError:
        print("Please enter a valid number.")

    # Handle division by zero.
    except ZeroDivisionError:
        print("Cannot divide by zero. Enter a non-zero number.")

    # Show the result after a successful calculation.
    else:
        print("Result:", result)
        break

# Expected checks; run these and record your actual results:
# 5: displays 20.0 and finishes normally.
# 0: displays the zero-division message and asks again.
# abc: displays the invalid-number message and asks again.
# Empty input: displays the invalid-number message and asks again.