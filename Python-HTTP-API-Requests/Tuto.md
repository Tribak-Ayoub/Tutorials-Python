# 🗓️ **Day 3 – HTTP & API Requests in Python**

🎯 **Goal:** Learn how to use Python’s `requests` package to **send GET/POST requests**, **handle JSON**, and **simulate real use cases** (e.g. GitHub API, contact form, public country data).

---

## ✅ Laravel vs Python Comparison

| Laravel                             | Python                                    |
| ----------------------------------- | ----------------------------------------- |
| `Http::get('url')`                  | `requests.get('url')`                     |
| `Http::post('url', [...])`          | `requests.post('url', json=data)`         |
| `$response->json()`                 | `response.json()`                         |
| `['Authorization' => 'Bearer ...']` | `headers={'Authorization': 'Bearer ...'}` |

---

## 🔧 Setup (One Time)

First, activate your virtual environment:

```powershell
.\venv\Scripts\Activate
```

Then install the `requests` package:

```bash
pip install requests
```

---

## 📥 Example 1: ✅ GitHub User Info (GET Request)

File: `github_user.py`

```python
import requests

def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        user = response.json()
        print(f"👤 Username: {user['login']}")
        print(f"📛 Name: {user.get('name', 'No name')}")
        print(f"📍 Location: {user.get('location', 'Unknown')}")
        print(f"📸 Avatar: {user['avatar_url']}")
        print(f"📦 Public Repos: {user['public_repos']}")
        print(f"👥 Followers: {user['followers']}")
    else:
        print(f"❌ User '{username}' not found.")

username = input("🔎 Enter GitHub username: ")
get_github_user(username)
```

🧪 Try with: `torvalds`, `octocat`, `your-username`

---

## 📤 Example 2: ✅ Simulate a Contact Form (POST Request)

File: `contact_form.py`

```python
import requests

def submit_contact_form():
    url = "https://httpbin.org/post"  # Test server that echoes your data
    data = {
        "name": input("👤 Your name: "),
        "email": input("📧 Your email: "),
        "message": input("💬 Your message: ")
    }

    response = requests.post(url, json=data)

    if response.ok:
        result = response.json()
        print("\n✅ Server received the following data:")
        for key, value in result["json"].items():
            print(f" - {key}: {value}")
    else:
        print("❌ Submission failed.")

submit_contact_form()
```

🧪 Try sending fake messages — and see how your data is returned.

---

## 🌍 Example 3: ✅ Country Info Lookup (Real API)

File: `country_info.py`

```python
import requests

def get_country_info(country):
    url = f"https://restcountries.com/v3.1/name/{country}"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()[0]
        print(f"\n🌍 Country: {data['name']['common']}")
        print(f"🏙️ Capital: {data['capital'][0]}")
        print(f"👥 Population: {data['population']:,}")
        print(f"💱 Currency: {list(data['currencies'].keys())[0]}")
        print(f"📍 Region: {data['region']}")
    except Exception as e:
        print("❌ Country not found or request failed.")

country = input("🌍 Enter country name: ")
get_country_info(country)
```

🧪 Try `Morocco`, `Germany`, `Japan`, `Brazil`.

---

## 🧪 BONUS Example 4: Handle Headers & Auth

```python
import requests

url = "https://api.example.com/private"
headers = {
    "Authorization": "Bearer YOUR_API_TOKEN",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

if response.ok:
    print(response.json())
else:
    print("❌ Unauthorized or error:", response.status_code)
```

🔐 Works exactly like Laravel's `Http::withHeaders([...])->get(...)`

---

## 🛡️ Bonus: Use `try` / `except` for Error Handling

```python
try:
    response = requests.get("https://api.github.com/users/fakeuser")
    response.raise_for_status()
    print(response.json())
except requests.exceptions.HTTPError as err:
    print("⚠️ HTTP error:", err)
except Exception as e:
    print("❌ Other error:", e)
```

---

## ✅ What to Practice Today

| Task                                 | Done? |
| ------------------------------------ | ----- |
| ✅ Send a GET request to GitHub       |       |
| ✅ Send a POST request to httpbin     |       |
| ✅ Call a public REST API (countries) |       |
| ✅ Print useful fields from JSON      |       |
| ✅ Add error handling (`try/except`)  |       |

---

## ✅ Summary for Day 3

| Skill   | Tool / Concept    | You Used       |
| ------- | ----------------- | -------------- |
| GET     | `requests.get()`  | GitHub API     |
| POST    | `requests.post()` | Simulated form |
| JSON    | `response.json()` | Parse data     |
| Headers | `headers={}`      | Tokens, auth   |
| Errors  | `try/except`      | Clean handling |
