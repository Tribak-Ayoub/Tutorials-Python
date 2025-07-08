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
