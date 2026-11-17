"""Exercise 8.1 — Bitwise operators (bonus, not graded)

WHAT THE PROGRAM MUST DO
    Represent a set of permissions as bits, combine two of them, test whether a third is
    present, then add it and remove one.

ANSWER THESE FIRST, in comments
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What are your permissions about? Not files: invent a set from your own field,

WHAT THE AI CANNOT KNOW
    Your permission set and what each one means in your context.

CHECK IT YOURSELF
    Display the value in binary at each step and read the bits yourself.

DELIVERABLE
    This file, with your comments and your code.
"""
# 1. In: Three permissions for managing a marketing campaign.
# 2. Process: Combine view and edit permissions, check publish,
#    add publish permission, then remove edit permission.
# 3. Out: The permissions displayed in binary after each step.
# 4. My example permissions:
#    VIEW: See the campaign.
#    EDIT: Change the campaign.
#    PUBLISH: Launch the campaign.
#    Each permission uses a different bit.

# Your code below

VIEW = 1       # 001
EDIT = 2       # 010
PUBLISH = 4    # 100

# Combine view and edit permissions using bitwise OR.
permissions = VIEW | EDIT
print("View and edit:", format(permissions, "03b"))  # 011

# Test publish permission using bitwise AND.
has_publish = (permissions & PUBLISH) != 0
print("Publish test:", format(permissions & PUBLISH, "03b"))  # 000
print("Can publish:", has_publish)  # False

# Add publish permission using bitwise OR.
permissions = permissions | PUBLISH
print("After adding publish:", format(permissions, "03b"))  # 111

# Remove edit permission using AND with its inverted mask.
permissions = permissions & ~EDIT
print("After removing edit:", format(permissions, "03b"))  # 101

# Read the bits from left to right: PUBLISH, EDIT, VIEW.
# 011: edit and view.
# 111: publish, edit, and view.
# 101: publish and view.