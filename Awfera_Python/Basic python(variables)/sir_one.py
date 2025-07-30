# 1. Understanding Variables in Python
# Variables store data temporarily during program execution

# Example of a variable storing a string
greeting = "Hello, Python!"
print(greeting)  # Output: Hello, Python!

# Example of a variable storing an integer
age = 25
print(age)  # Output: 25

# Example of a variable storing a float
price = 99.99
print(price)  # Output: 99.99

# Example of a variable storing a boolean
is_active = True
print(is_active)  # Output: True

# 2. Rules for Naming Variables
# Valid variable names
username = "JohnDoe"
_firstname = "Ali"
age1 = 30
user_name = "Ahmed"

# Invalid variable names (commented out to avoid errors)
# 1user = "Invalid"  # Cannot start with a number
# print = 10  # Cannot use reserved keywords

# 3. Variable Naming Conventions
# Snake Case (Recommended for Python)
user_name = "Alice"
# Camel Case (Common in JavaScript, Java, etc.)
userName = "Bob"
# Pascal Case (Used in class names)
UserName = "Charlie"

# 4. Data Types in Python
# Integer
a = 10  # Whole number
# Float
b = 3.14  # Decimal number
# String
c = "Python Programming"  # Sequence of characters
# Boolean
d = False  # True or False

# 5. Python Collections
# Dictionary - key-value pairs
person = {"name": "John", "age": 30, "city": "New York"}
print(person["name"])  # Output: John

# List - ordered collection (mutable)
numbers = [10, 20, 30, 40]
numbers.append(50)
print(numbers)  # Output: [10, 20, 30, 40, 50]

# Tuple - ordered collection (immutable)
person_tuple = ("Alice", 25, "Engineer")
print(person_tuple[0])  # Output: Alice

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(full_name)  # Output: John Doe

# 6. Virtual Environment Setup (Command Line Instructions)
# Run these commands in your terminal (for Anaconda users)
# conda create -n myenv python=3.10
# conda activate myenv
# code .  # Opens VS Code in the correct environment

# 7. Best Practices
# Use meaningful variable names
student_name = "Sarah"
age = 22

# Use f-strings for string formatting
print(f"Student Name: {student_name}, Age: {age}")  # Output: Student Name: Sarah, Age: 22
