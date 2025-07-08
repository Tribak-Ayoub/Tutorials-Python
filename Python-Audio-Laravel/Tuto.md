# 🧑‍💻 Day 6: Handle File & Audio Uploads (FastAPI + Laravel)

### 🎯 Goal

Learn to upload audio files from a Laravel backend to a FastAPI microservice that receives, saves, and responds.

---

## Part 1 — FastAPI: Receive & Save Uploaded Audio

**`main.py`**

```python
from fastapi import FastAPI, File, UploadFile
import shutil

app = FastAPI()

@app.post("/upload-audio/")
async def upload_audio(file: UploadFile = File(...)):
    """
    Receive an uploaded audio file and save it.
    """
    file_location = f"uploaded_files/{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "message": "File successfully uploaded!"}
```

- Make sure you have a folder called `uploaded_files` in your project directory.
- Run FastAPI server:

```bash
uvicorn main:app --reload
```

---

## Part 2 — Laravel: Send Audio File to FastAPI

In Laravel, create a controller method to send the audio file.

```php
<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Http;

class AudioController extends Controller
{
    public function uploadToFastAPI(Request $request)
    {
        // Validate incoming request has a file called 'audio'
        $request->validate([
            'audio' => 'required|file|mimes:mp3,wav,ogg|max:10240', // max 10MB
        ]);

        $file = $request->file('audio');

        // Send file to FastAPI microservice
        $response = Http::attach(
            'file', file_get_contents($file->getRealPath()), $file->getClientOriginalName()
        )->post('http://127.0.0.1:8000/upload-audio/');

        if ($response->successful()) {
            return response()->json([
                'message' => 'Audio uploaded successfully',
                'fastapi_response' => $response->json()
            ]);
        } else {
            return response()->json(['error' => 'Failed to upload audio'], 500);
        }
    }
}
```

---

## Part 3 — Laravel Route

Add a route for the audio upload in `routes/api.php`:

```php
use App\Http\Controllers\AudioController;

Route::post('/upload-audio', [AudioController::class, 'uploadToFastAPI']);
```

---

## Part 4 — How to test?

- Start **FastAPI** server on port 8000:
  `uvicorn main:app --reload`

- Start **Laravel** server on port 8001 or another port:
  `php artisan serve --port=8001`

- Use Postman or Thunder Client to **POST** to Laravel API endpoint:
  `http://127.0.0.1:8001/api/upload-audio`

- In Postman Body, select `form-data`, add key `audio` of type File, then upload your audio file and send.

---

## Part 5 — What happens?

- Laravel receives the audio file from client.
- Laravel validates the file.
- Laravel sends the audio file to FastAPI `/upload-audio/` endpoint using multipart form-data.
- FastAPI receives the file, saves it to `uploaded_files` folder.
- FastAPI responds with JSON confirmation.
- Laravel returns this confirmation JSON back to the client.

---

## Extra Tips:

- **File validation** on Laravel side ensures only allowed audio types and max size.
- You can **secure** FastAPI endpoints later with tokens or API keys.
- For large files or production, consider **streaming uploads** or async file processing.
- You can extend FastAPI to do audio processing (e.g., call Whisper API) after saving.
