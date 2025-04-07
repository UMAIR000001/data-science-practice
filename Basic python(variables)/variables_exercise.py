# 1. Understanding Variables in Python

# Assigning values to variables
fruit = "apple"  # String variable
a = 10  # Integer variable
pi = 3.14  # Float variable
is_student = True  # Boolean variable

# Printing variables
print(f"Fruit: {fruit}")
print(f"Integer value: {a}")
print(f"Float value: {pi}")
print(f"Boolean value: {is_student}")

# 2. Understanding Naming Conventions
snake_case = "This is snake case"
camelCase = "This is camel case"
PascalCase = "This is Pascal case"

print(snake_case)
print(camelCase)
print(PascalCase)

# 3. Python Dictionary Operations
person = {"name": "John", "age": 30, "city": "New York"}
print(person["name"])  # Accessing dictionary value
person["country"] = "USA"  # Adding a new key-value pair
del person["age"]  # Removing an element

print("Updated dictionary:", person)

# 4. Lists in Python
numbers = [10, 20, 30, 40]
numbers.append(50)  # Appending an element
numbers.insert(2, 15)  # Inserting at index 2
numbers.pop()  # Removing last element
numbers[0] = 99  # Modifying first element

print("Updated list:", numbers)

# 5. Strings in Python
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Concatenation
print(full_name)
print("ha" * 3)  # String repetition
print(first_name[0:2])  # Slicing

# Using f-strings
age = 25
print(f"My age is {age}")

# 6. Tuples in Python
person_tuple = ("Bob", 30, "Engineer")
print(person_tuple[0])  # Accessing elements

# Tuple unpacking
name, age, job = person_tuple
print(f"Name: {name}, Age: {age}, Job: {job}")
