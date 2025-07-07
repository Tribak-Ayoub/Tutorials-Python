# 🐍 Day 4 – Build Your First FastAPI Microservice (Detailed Beginner Guide)

🎯 **Goal:**
Build your first simple web API in Python using FastAPI — so you can create backend endpoints similar to Laravel controllers and routes.

---

## 1. What is FastAPI? Why use it?

FastAPI is a Python framework that helps you build **web APIs** easily and fast.

* Think of it like Laravel’s routing + controller system, but in Python.
* It’s modern, uses **Python type hints** for input validation.
* It automatically creates interactive API docs for you — so no need to build that manually.
* It’s super fast and widely used for microservices and backend APIs.

---

## 2. Install FastAPI and Uvicorn

Open your terminal (PowerShell or CMD) and run:

```bash
pip install fastapi uvicorn
```

* `fastapi` is the framework itself.
* `uvicorn` is a lightweight server that runs your FastAPI app.

---

## 3. Create your project file

Create a folder for your project, for example:

```bash
mkdir fastapi-tutorial
cd fastapi-tutorial
```

Create a new file named `main.py` inside it.

---

## 4. Write your first FastAPI app

Open `main.py` in your code editor (VSCode, Sublime, etc.) and paste:

```python
from fastapi import FastAPI

app = FastAPI()  # Create a FastAPI app instance

@app.get("/")  # Define a route for GET requests on "/"
def read_root():
    return {"message": "Hello from FastAPI!"}  # Returns JSON response
```

---

### What’s going on here?

* `FastAPI()` creates your app (like `$app = new LaravelApplication()`).
* `@app.get("/")` tells FastAPI: "When someone visits `/` with a GET request, run the following function."
* The function `read_root` returns a Python dictionary `{...}` — FastAPI automatically converts it to JSON.
* JSON is the standard format for API responses.

---

## 5. Run your FastAPI app

In your terminal, run:

```bash
uvicorn main:app --reload
```

Explanation:

* `main` is the file name (`main.py` without `.py`)
* `app` is the FastAPI app object
* `--reload` means the server will restart automatically if you change code (great for dev)

---

## 6. Open your browser

Go to:

* [http://127.0.0.1:8000/](http://127.0.0.1:8000/) → You’ll see:

  ```json
  {"message":"Hello from FastAPI!"}
  ```

* [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) → Interactive API docs (Swagger UI) where you can test your endpoints

* [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) → Another API doc style

---

## 7. Add a dynamic route (path parameter)

Add this below your first route in `main.py`:

```python
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}
```

---

### What does this do?

* The `{name}` in the route means **capture whatever the user writes there** as a variable.
* The `name: str` tells Python to expect a **string**.
* You return a greeting JSON with the name.
* Try going to:
  `http://127.0.0.1:8000/hello/Ayoub`
  and see what happens!

---

## 8. Handle POST requests with JSON input

Add this example below your existing routes:

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None  # Optional field
    price: float
    tax: float = None        # Optional field

@app.post("/items/")
def create_item(item: Item):
    total_price = item.price + (item.tax or 0)
    return {"name": item.name, "total_price": total_price}
```

---

### Explanation:

* `BaseModel` is from **Pydantic** and is used to **define the shape of data** you expect in POST requests.
* When someone sends JSON to `/items/`, FastAPI will **automatically convert** the JSON into an `Item` Python object.
* You can then use the fields directly: `item.name`, `item.price`, etc.
* You calculate total price and return a JSON response.

---

## 9. Test your POST endpoint

Use **curl** or a tool like **Postman**.

Example curl command:

```bash
curl -X POST "http://127.0.0.1:8000/items/" -H "Content-Type: application/json" -d '{"name":"Pen","price":1.5,"tax":0.2}'
```

Expected output:

```json
{
  "name": "Pen",
  "total_price": 1.7
}
```

---

## 10. Optional: Query parameters example

Add this:

```python
@app.get("/search/")
def search_items(q: str = None):
    return {"query": q}
```

Try:

* `/search/?q=fastapi`
* `/search/` (without q parameter)

`q: str = None` means `q` is optional.

---

## Summary Table: FastAPI vs Laravel

| FastAPI Concept               | Laravel Equivalent                |
| ----------------------------- | --------------------------------- |
| `@app.get("/route")`          | `Route::get('/route', ...)`       |
| `@app.post("/route")`         | `Route::post('/route', ...)`      |
| Pydantic models (`BaseModel`) | Form Requests or validation rules |
| Function params               | Controller method parameters      |
| `uvicorn` server              | `php artisan serve`               |

---

## What to do today?

* Install FastAPI and Uvicorn.
* Create `main.py` with simple GET and POST routes.
* Run the server and try accessing `/` and `/hello/yourname`.
* Test POST request with curl or Postman.
* Explore [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

