import random

upper, lower, nums, syms = True, True, True, True  # change these if you want a specific type of generated password

length = 20
amount = 10

# Do not touch the rest of the code if you don't know Python, or it won't work
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},;:./?!@#$%^&*-="

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lower_letters
if nums:
    all += digits
if syms:
    all += symbols

for _ in range(amount):
    password = "".join(random.choices(all, k=length))
