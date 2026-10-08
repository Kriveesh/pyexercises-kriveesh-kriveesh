# Conversation with the AI

Written automatically by `tutor.py`. Add your own notes under any entry: what you tried, what broke, what you changed. Those notes are what is graded.

---
## 2026-10-07 12:05, in .

**Me:** how to print a statement in a python

**Tutor:**

Printing a statement in Python is done with the `print()` function.

```python
# Printing a simple statement
print("Hello, world!")
```

What is the function used to print output in Python?

---
## 2026-10-07 13:22, in .

**Me:** how to concatenate two strings

**Tutor:**

String concatenation joins two strings into one.

```python
def join_strings(first: str, second: str) -> str:
    # TODO: return the two strings joined together
    pass
```

What is the operator used to concatenate strings in Python?

---
## 2026-10-08 10:28, in .

**Me:** How to receive inputs from user and print it

**Tutor:**

Receiving inputs from the user is done with the `input()` function.

```python
# TODO: Ask the user for their name and store it
user_name = ______

# TODO: Print the name back to the user
print(______)
```

What is the function used to get input from the user?

---
## 2026-10-08 10:36, in .

**Me:** String transformation

**Tutor:**

String transformation means changing the case, removing spaces, or slicing parts of a string.

```python
def clean_name(raw: str) -> str:
    # TODO: remove leading/trailing spaces and convert to lowercase
    cleaned = raw
    return cleaned

# toy data
alpha = "  John Doe  "
beta  = "  JANE SMITH  "

print(clean_name(alpha))  # expected: 'john doe'
print(clean_name(beta))   # expected: 'jane smith'
```

What built-in string method removes whitespace from both ends?

---
## 2026-10-08 14:58, in .

**Me:** Why do we use float() for the numbers?

**Tutor:**

Converting strings to floats lets you do math with numbers that came from a CSV.

```python
# TODO: replace the strings with real numbers from your file
row = ["12345", "clicks", "42.5", "2.99"]
impressions = float(row[0])   # TODO: index 0
cost      = float(row[3])     # TODO: index 3

ctr = (impressions / 1000) * 100
cpa = cost / impressions
print("CTR:", ctr, "CPA:", cpa)
```

Which function converts a string to a floating-point number?
