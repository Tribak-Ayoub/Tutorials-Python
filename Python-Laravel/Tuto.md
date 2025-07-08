# 🐍 Day 5 – Connect Laravel ↔ Python (FastAPI) with Debugging Output

---

## 1. FastAPI Microservice — `main.py`

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Lead(BaseModel):
    name: str
    email: str
    phone: str
    interest_level: int

@app.post("/api/score-lead")
async def score_lead(lead: Lead):
    print("Received lead:", lead)  # <-- Debug: show data in Python console
    score = lead.interest_level * 10
    if "@gmail.com" in lead.email:
        score += 5
    return {"lead_score": min(score, 100)}
```

---

## 2. Run the FastAPI server:

```bash
uvicorn main:app --reload
```

*Leave this running to receive requests.*

---

## 3. Laravel Controller — `LeadController.php`

```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

class LeadController extends Controller
{
    public function score(Request $request)
    {
        $response = Http::post('http://127.0.0.1:8000/api/score-lead', [
            'name' => $request->input('name'),
            'email' => $request->input('email'),
            'phone' => $request->input('phone'),
            'interest_level' => $request->input('interest_level'),
        ]);

        return response()->json([
            'python_response' => $response->json()
        ]);
    }
}
```

---

## 4. Laravel Route — `routes/web.php`

```php
use App\Http\Controllers\LeadController;

Route::post('/lead/score', [LeadController::class, 'score']);
```

---

## 5. Testing the Integration

Use Postman, Thunder Client, or an HTML form to send a POST request to:

```
http://localhost:8000/lead/score
```

With JSON body like:

```json
{
  "name": "Ayoub",
  "email": "ayoub@gmail.com",
  "phone": "+212600000000",
  "interest_level": 7
}
```

---

## 6. What Happens?

* **FastAPI console** (where you run `uvicorn`) will print:

```
Received lead: name='Ayoub' email='ayoub@gmail.com' phone='+212600000000' interest_level=7
```

* **Laravel** will return:

```json
{
  "python_response": {
    "lead_score": 75
  }
}
```

---

## 7. Optional: HTML form to test manually (Blade view)

```blade
<form action="/lead/score" method="POST">
    @csrf
    <input type="text" name="name" placeholder="Name" required>
    <input type="email" name="email" placeholder="Email" required>
    <input type="text" name="phone" placeholder="Phone" required>
    <input type="number" name="interest_level" placeholder="Interest Level (1-10)" required min="1" max="10">
    <button type="submit">Send to Python</button>
</form>
```

---

## Summary

This tutorial shows you how to:

* Send JSON from Laravel to Python FastAPI
* Receive and parse JSON in Python
* Debug by printing received data in Python console
* Return JSON back to Laravel and use it
