print('hello from python')

######

age = 24
name = "Ayoub"

print(type(age))
print(type(name))

######

x = 2
y = 5
z = x + y

greeting = 'hello'
name = "Ayoub"
message = greeting + ', ' + name

print(z)
print(message)

######

# List
numbers = [1, 5, 3]
numbers.append(9)

print(numbers)

# Dictionary
user = {"name": "Ayoub", "age": 24}

print(user["age"])

######

# Conditions
score = 85

if score >= 90:
    print('excellent')
elif score >= 75:
    print('good')
else:
    print('keep improving')

#######

# Loops

for i in range(4):
    print(i)

#

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#

count = 0
while count < 3:
    print('counting: ', count)
    count += 1

#######

# Functions

# with type
def evenOdd(x: int) -> str:
    """Function to check if the number is even or odd"""
    if(x % 2 == 0):
        print('Even')
    else:
        print('Odd')

evenOdd(4)

# Docstring
print(evenOdd.__doc__)

# without type
def evenOddV2(x):
    if(x % 2 == 0):
        print('Even')
    else:
        print('Odd')

evenOddV2(5)

# f-strings
def greet(name):
    return f"Hello, {name}!"

msg = greet("Ayoub")
print(msg)

########

# using packages
import requests

response = requests.get("https://api.github.com")
print(response.status_code)