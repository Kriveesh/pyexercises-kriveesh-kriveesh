"""Exercise 10.0 — Checking the shape of text (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Validate three pieces of information typed by the user, and only save them when all
    three are acceptable.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your three fields, and what makes a value acceptable for each? Write the
       rule in plain English before writing any pattern.

WHAT THE AI CANNOT KNOW
    Your three rules. "A valid email" is not a rule, it is a wish. Say what you accept
    and what you reject, and be ready to defend a borderline case.

WHAT TO WATCH
    An assistant will hand you a pattern that looks like line noise. Do not accept it
    until it has explained it to you piece by piece, and you have written that
    explanation in your own words above it.

CHECK IT YOURSELF
    For each field, prepare one value that must pass and two that must fail. Run all
    nine. Any surprise goes in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""
# 1. In: A campaign code, a discount code, and a French postal code.
# 2. Process: Check each value against its rule using regular expressions.
#    Ask again when a value fails. Save only after all three pass.
# 3. Out: campaign_details.csv containing the three accepted values.
# 4. My fields and rules:
#    Campaign code: exactly three uppercase English letters,
#    a hyphen, then three digits. Example: ADS-123.
#    Discount code: exactly four uppercase English letters.
#    French postal code: exactly five digits.
#    This checks its shape, not whether the postal code really exists.
#    Spaces and lowercase letters are rejected.

# Your code below
import csv
import re


# Ask again until the entire input matches the pattern.
def get_valid_input(prompt, pattern):
    while True:
        value = input(prompt)
        if re.fullmatch(pattern, value):
            return value
        print("Invalid format. Please try again.")


# [A-Z] means an uppercase English letter.
# {3} requires three letters.
# - matches a literal hyphen.
# [0-9]{3} requires three digits.
campaign_pattern = r"[A-Z]{3}-[0-9]{3}"

# [A-Z]{4} requires exactly four uppercase English letters.
discount_pattern = r"[A-Z]{4}"

# [0-9]{5} requires exactly five digits.
# Keep this value as text so leading zeros are preserved.
postal_pattern = r"[0-9]{5}"


# Prepare nine checks: one pass and two failures per field.
tests = [
    (campaign_pattern, "ADS-123", True),
    (campaign_pattern, "ads-123", False),
    (campaign_pattern, "ADS123", False),
    (discount_pattern, "SALE", True),
    (discount_pattern, "sale", False),
    (discount_pattern, "SALE5", False),
    (postal_pattern, "75001", True),
    (postal_pattern, "7500", False),
    (postal_pattern, "75A01", False)
]


# Run the checks and compare actual results with predictions.
for pattern, value, expected in tests:
    actual = re.fullmatch(pattern, value) is not None
    print(value, "Passed check:", actual == expected)

# Expected: all nine checks display True.
# After running, record any unexpected results here.


# Collect all three acceptable values before opening the output file.
campaign = get_valid_input("Campaign code (ADS-123): ", campaign_pattern)
discount = get_valid_input("Discount code (SALE): ", discount_pattern)
postal = get_valid_input("French postal code (75001): ", postal_pattern)


# Append the accepted entry, writing the header only once.
with open("campaign_details.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    if file.tell() == 0:
        writer.writerow(["campaign_code", "discount_code", "postal_code"])

    writer.writerow([campaign, discount, postal])

print("Details saved successfully.")