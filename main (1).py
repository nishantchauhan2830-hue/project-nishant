# Check if 5 is greater than 2
if 5 > 2:
    print("Five Is Greater Than Two")

# Basic arithmetic operations
x = 5
y = 2
print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division

# Print a string
print('Hello world')

# Print integer and string variables
x = 8
y = "Ankush"
print(x)
print(y)

# Print types of variables
x = 8
y = "Ankush"
print(type(x))  # <class 'int'>
print(type(y))  # <class 'str'>
# Boolean evaluation
x = 5
y = 4
print(bool(x + y))  # True because 9 is non-zero
print(bool(x + y))  # Repeated for demonstration

# Multiple variable assignment
x = y = z = "apple"
print(x)
print(y)
print(z)

# Unpacking a list into variables
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Reassigning variables and printing types
fruits = [2, 4, 7, 8, 34, 50]
x = y = fruits  # Assigning the entire list to both x and y
print(x)
print(y)
print(fruits)
print(type(x))       # <class 'list'>
print(type(fruits))  # <class 'list'>

# String assignment and printing
x = "This Is Python"
print(x)

# Printing multiple strings
x = "python"
y = "is"
z = "good"
print(x, y, z)
# Print a simple message
print("!! Hello World !!")

# Example 1: Using a global variable inside a function
x = "Good"  # Global variable

def my_function():
    # Function Opening
    print("Python Is " + x)  # Accessing global variable
    # Action

my_function()
# Function Closing
print("Python Is " + x)

# Example 2: Defining a global variable inside a function
def my_function():
    global x
    x = "Good"

my_function()
print("Python Is " + x)

# Example 3: Accessing a global variable from within a function
x = "Good"

def my_function():
    print("Python Is " + x)

my_function()

# -------- DATA TYPE --------
# -------- DATA TYPES --------

x = 5
print(type(x))  # <class 'int'>

x = 5.6
print(type(x))  # <class 'float'>

x = 1j
print(type(x))  # <class 'complex'>

x = {"Apple", "Banana"}
print(type(x))  # <class 'set'>

x = "Good"
print(type(range(5)))  # <class 'range'> — corrected to show type of a range object

# -------- ARITHMETIC OPERATIONS --------

x = 10
y = 5
print(x + y)   # Addition: 15
print(x - y)   # Subtraction: 5
print(x * y)   # Multiplication: 50
print(x / y)   # Division: 2.0
print(x % y)   # Modulus: 0
print(x ** y)  # Exponentiation: 100000
print(x // y)  # Floor Division: 2

# -------- LIST (Coming Next) --------
# Define a list and print its type, contents, and length
my_list = ["Apple", "Banana"]
print(type(my_list))
print(my_list)
print(len(my_list))

# Access elements by index
my_list = ["Apple", "Banana", "Cherry"]
print(my_list[1])     # Output: Banana
print(my_list[-1])    # Output: Cherry

# Slice the list
my_list = ["Apple", "Banana", "Cherry", "Mango", "Lemon", "Coconut"]
# print(my_list[2:5])  # Optional: Cherry to Lemon
print(my_list[-5:-2])  # Output: Banana, Cherry, Mango

# Modify an element in the list
my_list = ["Apple", "Banana", "Cherry", "Mango", "Lemon", "Coconut"]
my_list[1] = "Tomato"
print(my_list)         # Output: ['Apple', 'Tomato', 'Cherry', 'Mango', 'Lemon', 'Coconut']
# Print greetings
print("hello")
print("good morning")

# Modify elements in a list
my_list = ["apple", "banana", 1, 3, 5, 7]
my_list[2] = "abc"
print(my_list)  # Output: ['apple', 'banana', 'abc', 3, 5, 7]

# Replace a slice of the list
my_list[2:5] = ["abc"]
print(my_list)  # Output: ['apple', 'banana', 'abc', 7]

# Insert and append elements
my_list = [1, 2, 4, 5, 6]
my_list.insert(2, 3)  # Inserts 3 at index 2
my_list.append(7)     # Appends 7 at the end
print(my_list)        # Output: [1, 2, 3, 4, 5, 6, 7]

# Extend one list with another
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)          # Output: [1, 2, 3, 4, 5, 6]
# Initial list and removal
list1 = [1, 2, 3, "apple", 4, 5, 6]
# list1.remove("apple")  # Optional: removes "apple" by value
list1.pop()              # Removes the last element (6)
print(list1)             # Output: [1, 2, 3, 'apple', 4, 5]

# Creating and modifying a list
list1 = []
list1.append(1)          # Adds 1 to the list
print(list1)             # Output: [1]

list1[0] = "hello"       # Replaces 1 with "hello"
print(list1)             # Output: ['hello']

# Looping through a list
list1 = [1, 2, 3, 4, 4, 4, "apple", 5, 6]
for x in list1:
    print(x)
    # Assignment and arithmetic operations
x = 5
y = 0  # Initialize y before using +=
y += 3
print("x =", x)
print("y =", y)

x -= 3
print("x after -= 3:", x)

x *= 3
print("x after *= 3:", x)

x /= 3
print("x after /= 3:", x)

# Comparison operations
x = 10
y = 7

print("x == y:", x == y)
print("x != y:", x != y)
print("x > y:", x > y)
print("x < y:", x < y)
print("x >= y:", x >= y)
print("x <= y:", x <= y)
# Logical operators
x = 5
print(x > 3 and x < 10)  # True

# Variable assignment
x = 8
y = x
print(y)  # Output: 8

# Identity operator
x = 8
y = x
z = 10
print(y)           # Output: 8
print(x is not y)  # False, because x and y refer to the same object

# Tuples
# A tuple is an ordered collection of items, similar to a list, but immutable (cannot change elements).
# Tuples are defined using parentheses ()
my_tuple = (1, 2, 3, "apple")
print(my_tuple)

# Sets
# A set is an unordered collection of unique items.
# Sets do not allow duplicates and are defined using curly braces {}
my_set = {1, 2, 3, 3, "apple", "banana"}
print(my_set)  # Output will not include duplicate 3
# Creating a Set
colors = {"red", "green", "blue"}
print(colors)

# Adding Elements
colors.add("yellow")
print(colors)

# Removing Elements
colors.remove("green")
print(colors)

# Iterating Through Set
for color in colors:
    print(color)

# Python Dictionaries
# A dictionary is an unordered collection of key-value pairs.
# Keys must be unique and immutable (string, number, tuple).
# Values can be any data type.
# Dictionaries are defined using curly braces {} with key: value.

# Creating a Dictionary
student = {"name": "Alice", "age": 45, "grade": "A+"}
print(student)
# Dictionary operations
student = {"name": "Alice", "age": 20, "grade": "A+"}

# ACCESSING VALUES
print(student["name"])        # Output: Alice
print(student.get("age"))     # Output: 20

# ADDING/UPDATING VALUES
student["age"] = 21
student["city"] = "Delhi"
print(student)                # Output: {'name': 'Alice', 'age': 21, 'grade': 'A+', 'city': 'Delhi'}

# REMOVING ITEMS
student.pop("grade")
del student["city"]
print(student)                # Output: {'name': 'Alice', 'age': 21}

# ITERATING THROUGH DICTIONARY
for key, value in student.items():
    print(key, ":", value)

# IF....ELSE IN PYTHON
age = 17  # You can change this value to test different outcomes

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    # 1. The if Statement
# The if statement is used to check a condition. If the condition is true, the code inside will run.

# if...else example
age = 20

if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult")
    # 1. if...elif...else Statement
# We can check multiple conditions using elif (else if)

age = 16

if age == 18:
    print("You are a teen")
elif age == 17:
    print("You are 17")
elif age < 18:
    print("You are not an adult")
else:
    print("You are an adult")

# 2. Another example using marks
marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")
    # Grading system
marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# Nested If
x = 15

if x > 10:
    print("x is greater than 10")
    if x > 20:
        print("x is greater than 20")
    else:
        print("x is not greater than 20")

# QUESTION-01: Check if a number is positive or negative
x = 10

if x > 0:
    print("Positive Number")
elif x < 0:
    print("Negative Number")
else:
    print("Zero")

# Check if a number is even
if x % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
    # Check if a number is even or odd
x = 19

if x % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Check driving eligibility
x = 19

if x >= 18:
    print("Good!! You are eligible to drive.")
else:
    print("Sorry!! You are not eligible to drive.")

# PYTHON FOR LOOPS
# A for loop in Python is used to iterate (repeat) over a sequence such as a list, string, tuple, or range.

# SYNTAX:
# for variable in sequence:
#     code to execute

# Example: Iterating through a string
word = "python"
for x in word:
    print(x)
    # Using range() in For Loops
# The range() function generates a sequence of numbers.

for i in range(5):
    print(i)  # Output: 0 to 4

# You can also use range(start, stop, step)
for i in range(1, 10, 2):
    print(i)  # Output: 1, 3, 5, 7, 9

# Nested For Loops
# You can put a for loop inside another for loop.
for i in range(1, 4):
    for j in range(1, 3):
        print(f"i={i}, j={j}")

# Using break in For Loops
# break stops the loop when a condition is met.
for i in range(1, 6):
    if i == 4:
        break
    print(i)  # Output: 1, 2, 3

# Using continue in For Loops
# continue skips the current iteration when a condition is met.
for i in range(1, 6):
    if i == 3:
        continue
    print(i)  # Output: 1, 2, 4, 5
    # Using continue in For Loops
for i in range(1, 6):
    if i == 3:
        continue
    print(i)  # Output: 1, 2, 4, 5

# QUESTION NUM -> 1
# Print numbers from 1 to 19
for i in range(1, 20):
    print(i)

# QUESTION NUM -> 2
# Print even numbers from 1 to 30
for i in range(1, 31):
    if i % 2 == 0:
        print(i)

# QUESTION NUM -> 3
# Print multiplication table of 5
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

# QUESTION NUM -> 4
# Nested loops to print combinations of i, j, and k
for i in range(1, 4):
    for j in range(1, 5):
        for k in range(1, 6):
            print(f"i={i}, j={j}, k={k}")
            # 1. DEFINING A FUNCTION
# Use the def keyword to define a function.

def greet():
    print("Hello, Python!")

greet()  # Calling the function

# 2. FUNCTION WITH PARAMETERS
# Parameters allow you to pass values into a function.

def greet_with_name(name):
    print(f"Hello, {name}!")

greet_with_name("Alice")
greet_with_name("Bob")

# 3. FUNCTION WITH RETURN VALUE
# A function can return a value using the return statement.

def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
# Function with subtraction
def subtract(a, b):
    return a - b

result = subtract(5, 3)
print(result)  # Output: 2

# Function with multiplication
def multiply(a, b):
    return a * b

result = multiply(5, 3)
print(result)  # Output: 15

# Function with division
def divide(a, b):
    return a / b

result = divide(5, 3)
print(result)  # Output: 1.666...

# 4. FUNCTION WITH DEFAULT PARAMETER
# You can give a default value to a parameter.
def greet(name="Student"):
    print(f"Hello, {name}!")

greet()         # Output: Hello, Student!
greet("Alice")  # Output: Hello, Alice!

# Scope of variables
x = 10

def my_func():
    y = 5
    print("Inside function:", x, y)

my_func()  # Output: Inside function: 10 5
# Function scope demonstration
x = 10

def my_func():
    y = 5
    print("Inside:", x, y)

my_func()
print("Outside:", x)

# QUESTION NUM -> 01
def greet(name):
    print(f"Hello, {name}")

greet("Harsh")  # Output: Hello, Harsh

# QUESTION NUM -> 02
def add(a, b):
    return a + b

result = add(5, 4)
print(result)  # Output: 9

# OOPs IN PYTHON (BASIC)
# OOPs = Object-Oriented Programming System --> Organizing code using classes and objects.

# 1. CLASS AND OBJECT
class Car:
    def __init__(self, brand, color):  # Corrected from _init_ to __init__
        self.brand = brand  # Attribute
        self.color = color  # Attribute

    def drive(self):  # Method
        print(f"{self.color} {self.brand} is driving 🚗")

# Creating an object and calling the method
my_car = Car("Toyota", "Red")
my_car.drive()  # Output: Red Toyota is driving 🚗
# Object creation and method calling
car1 = Car("BMW", "Black")
car2 = Car("Tesla", "White")

car1.drive()
car2.drive()