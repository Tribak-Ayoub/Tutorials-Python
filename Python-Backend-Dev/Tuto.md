# 🗓️ **Day 2 – Python for Backend Developers**

🎯 **Goal:** Learn file handling, JSON operations, modular code organization, and project environment management — all tailored for backend workflows (like you’d do in Laravel but with Python).

---

## ✅ 1. Organizing Code with Modules

In Laravel, logic is organized into controllers, services, etc.
In Python, you organize code using **modules** and **packages**.

### 📁 Create structure:

```
my_project/
├── main.py
└── utils/
    └── formatter.py
```

### 📦 Example: `utils/formatter.py`

```python
def format_user(name, age):
    return f"{name} is {age} years old"
```

### 🧠 Use it in `main.py`:

```python
from utils.formatter import format_user

print(format_user("Ayoub", 24))
```

> ✅ This makes your code reusable and clean — like Laravel services/helpers.

---

## ✅ 2. File Handling (📄 read/write)

### ✍️ Writing to a file:

```python
with open("log.txt", "w") as f:
    f.write("This is a backend log.\n")
```

### 📖 Reading a file:

```python
with open("log.txt", "r") as f:
    content = f.read()
    print(content)
```

> 🧠 Similar to writing logs or configs in Laravel, but much simpler.

---

## ✅ 3. JSON Handling (API-Ready 🧩)

You're already familiar with JSON in Laravel APIs. Python handles JSON natively.

### Convert Python → JSON string:

```python
import json

user = {"name": "Ayoub", "age": 24}
json_str = json.dumps(user)
print(json_str)  # '{"name": "Ayoub", "age": 24}'
```

### Save JSON to a file:

```python
with open("user.json", "w") as f:
    json.dump(user, f)
```

### Read JSON from file:

```python
with open("user.json", "r") as f:
    data = json.load(f)
    print(data["name"])
```

> 🔄 Just like Laravel’s `json_encode()` and `json_decode()` — but built in.

---

## ✅ 4. Using Environment Variables

In Laravel, `.env` is key. In Python, use `os` + `python-dotenv`.

### 🧪 Step-by-step:

1. Install dotenv:

```bash
pip install python-dotenv
```

2. Create a `.env` file:

```
API_KEY=your_secret_key
```

3. Use it in Python:

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
print(api_key)
```

> 🔐 Use this for API keys, DB creds, etc.

---

## ✅ 5. Virtual Environments (`venv`) for Isolated Projects

Just like Laravel uses `composer.lock`, Python projects use **virtual environments** to isolate dependencies.

### 📦 Create a venv:

```bash
python -m venv venv
```

### ✅ Activate:

* Windows:

  ```bash
  .\venv\Scripts\activate
  ```
* macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

Now install packages **inside your project**:

```bash
pip install requests python-dotenv
```

When done:

```bash
deactivate
```

> 🔁 This keeps dependencies clean, per project — just like Laravel’s `vendor`.

---

## 🧪 Practice Task: `save_user.py`

Create a script that:

* Gets user info via `input()`
* Saves it to a `.json` file
* Loads it back and prints it

```python
import json

def save_user():
    name = input("Name: ")
    age = input("Age: ")
    user = {"name": name, "age": age}
    
    with open("user.json", "w") as f:
        json.dump(user, f)
    print("✅ Saved!")

def read_user():
    with open("user.json", "r") as f:
        data = json.load(f)
        print(f"Hello {data['name']}, age {data['age']}")

save_user()
read_user()
```

---

## 📚 Resources

* [Python File I/O – W3Schools](https://www.w3schools.com/python/python_file_handling.asp)
* [Real Python – Modules & Packages](https://realpython.com/python-modules-packages/)
* [python-dotenv GitHub](https://github.com/theskumar/python-dotenv)

---

## ✅ Day 2 Summary

| Concept       | Laravel Equivalent                    | Python Practice                 |
| ------------- | ------------------------------------- | ------------------------------- |
| Modular Code  | Service class, helper                 | `from mymodule import myfunc`   |
| File Handling | `Storage::put()`                      | `open("file.txt", "w")`         |
| JSON          | `json_encode()`, `response()->json()` | `json.dumps()`, `json.load()`   |
| .env          | `.env` config                         | `os.getenv()` + `python-dotenv` |
| Virtual Envs  | `vendor` isolation                    | `venv` + `pip install`          |

---

## 🎯 What to Do Today

✅ Create `save_user.py` with file + JSON handling
✅ Organize logic using your own module (`utils/formatter.py`)
✅ Practice with `.env` and use `os.getenv()`
✅ Use `venv` to isolate dependencies
