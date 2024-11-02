Let’s break down each part of the code so you can see how it generates a password:

1. `Setting User Preferences`
```python
upper, lower, nums, syms = True, True, True, True  # change these if you want a specific type of generated password
```
These four variables (`upper`, `lower`, `num`s, and `syms`) allow you to customize the password generator. Each variable is set to `True` or `False`:
`upper`: Whether to include uppercase letters.
`lower`: Whether to include lowercase letters.
`nums`: Whether to include numbers.
`syms`: Whether to include special symbols.
If you change any of these to `False`, that category will be excluded from the generated password.

2. `Setting Password Parameters`
```python
length = 20
amount = 10
```
These lines define two important variables:
`length`: The length of each generated password.
`amount`: The number of passwords to generate.
In this example, each password will be 20 characters long, and the program will generate 10 passwords.

3. `Defining Character Pools`
```python
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},;:./?!@#$%^&*-="
```
Each variable here contains a string of characters that might be included in a password:
`uppercase_letters`: A string of uppercase letters.
`lower_letters`: A string of lowercase letters (created by converting `uppercase_letters` to lowercase).
`digits`: A string of numeric characters.
`symbols`: A string of special symbols.
These character sets will be combined depending on your preferences (from Step 1).

4. `Building the Character Pool`
```python
all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lower_letters
if nums:
    all += digits
if syms:
    all += symbols
```
Here, an empty string `all` is created, which will hold all possible characters for password generation.
The `if` statements check each of the user’s preferences (`upper`, `lower`, `nums`, `syms`).
If a preference is `True`, the corresponding characters are added to `all`.
So, if all four variables are `True`, `all` will contain uppercase letters, lowercase letters, digits, and symbols.

5. `Generating and Printing Passwords`
```python
for _ in range(amount):
    password = "".join(random.choices(all, k=length))  # Using choices instead of sample
    print(password)
```
This part of the code generates the passwords:
The `for` loop repeats `amount` times (10 in this case), generating one password per loop.
Inside the loop, `random.choices(all, k=length)` randomly selects length (20) characters from `all` and allows repetition.
`"".join(...)` joins the randomly selected characters into a single string, creating a password.
`print(password)` outputs the generated password.
Each iteration of the loop creates and prints a new password according to the specified preferences and length.

Enjoy :)
