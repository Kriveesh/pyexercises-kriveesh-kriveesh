"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:A list of expenses and a budget amount.
# 2. Process, function by function:calculate_total adds the expenses.calculate_remaining subtracts the total from the budget.check_budget checks whether the remaining amount is zero or positive.
# 3. Out:True if the expenses are within budget, otherwise False.
# 4. The question my fourth function answers:Are my total expenses within my budget?
#    Splitting the work makes it easier to test each calculation separately.


# Your code below
def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total = total + expense
    return total


def calculate_remaining(budget, total):
    return budget - total


def check_budget(remaining):
    return remaining >= 0


def expenses_within_budget(expenses, budget):
    total = calculate_total(expenses)
    remaining = calculate_remaining(budget, total)
    return check_budget(remaining)


# Test 1: Expenses [20, 15, 30]. Expected total: 65.
print(calculate_total([20, 15, 30]))

# Test 2: Budget 100, total 65. Expected remaining: 35.
print(calculate_remaining(100, 65))

# Test 3: Remaining -5. Expected result: False.
print(check_budget(-5))

# Test the fourth function.
expenses = [20, 15, 30]
budget = 100
print("Within budget:", expenses_within_budget(expenses, budget))