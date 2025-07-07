# 🐍 Day 1 – Python Basics for Laravel Developers

🎯 **Goal:** Learn Python syntax, data types, functions, conditions, and loops — enough to be productive.

---

## ✅ 1. Create Your First Python File

Create a folder called `Python-Basics` and inside it:

```bash
touch hello.py  # or create manually if you're on Windows
```

Paste this code:

```python
print("👋 Hello from Python!")
```

Run it:

```bash
python hello.py
```

---

## 📌 2. Variables & Data Types

### 💡 You don’t need `$` or `var` — just write:

```python
age = 24
name = "Ayoub"
is_active = True
```

### 🔎 Type Checking

```python
print(type(age))       # <class 'int'>
print(type(name))      # <class 'str'>
print(type(is_active)) # <class 'bool'>
```

---

## 🔢 3. Numbers & Strings

```python
x = 5
y = 2.5
z = x + y

greeting = "Hello"
name = "Ayoub"
message = greeting + ", " + name
print(message)  # Hello, Ayoub
```

✅ Strings can use `"..."` or `'...'`
✅ No need for semicolons

---

## ✅ 4. Lists & Dictionaries (like arrays & assoc arrays)

```python
# List (like JS array)
numbers = [1, 2, 3]
numbers.append(4)

# Dictionary (like PHP assoc array or JS object)
user = {"name": "Ayoub", "age": 22}
print(user["name"])  # Ayoub
```

---

## 🔁 5. Conditions

```python
score = 85

if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Good")
else:
    print("Keep improving")
```

✅ No `{}` → indentation is required

---

## 🔁 6. Loops

### For loop with `range`:

```python
for i in range(5):
    print(i)
```

### Looping over a list:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### While loop:

```python
count = 0
while count < 3:
    print("Counting", count)
    count += 1
```

---

## ⚙️ 7. Functions

```python
def greet(name):
    return f"Hello, {name}!"

msg = greet("Ayoub")
print(msg)
```

✅ Use `def` instead of `function`

---

## 📦 8. Using Packages

### Installing a package:

```bash
pip install requests
```

### Using it:

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
```

---

## 🧪 9. Practice: Mini App

Create `userinfo.py`:

```python
import requests

def get_user_info():
    username = input("Enter GitHub username: ")
    url = f"https://api.github.com/users/{username}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        user_data = response.json()
        name = user_data.get("name") or "No name provided"
        public_repos = user_data.get("public_repos")
        followers = user_data.get("followers")
        avatar_url = user_data.get("avatar_url")
        
        print(f"👋 GitHub User: {username}")
        print(f"Name: {name}")
        print(f"Public Repos: {public_repos}")
        print(f"Followers: {followers}")
        print(f"Profile Image URL: {avatar_url}")
    else:
        print(f"User '{username}' not found. Please check the username and try again.")

get_user_info()

```

Run it:

```bash
python userinfo.py
```

---

## 📚 Bonus Tips

| Laravel/PHP        | Python                   |
| ------------------ | ------------------------ |
| `$name = "Ayoub";` | `name = "Ayoub"`         |
| `echo`             | `print()`                |
| `isset()`          | `in` or `get()` in dicts |
| `foreach`          | `for ... in`             |
| `array()`          | `[]` or `list()`         |

---

## ✅ What to Do Today

* ✅ Create at least 2 Python scripts: `hello.py` and `userinfo.py`
* ✅ Practice with `list`, `dict`, `range`, `if`, and `def`
* ✅ Install and import 1 package (`requests`)
* ✅ Ask questions if anything feels weird compared to PHP
