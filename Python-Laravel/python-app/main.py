from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Lead(BaseModel):
    name: str
    email: str
    phone: str
    interest_level: int

@app.post('/api/score-lead')
async def score_lead(lead: Lead):
    print('Received lead: ', lead)

    score = lead.interest_level * 10
    if '@gmail.com' in lead.email:
        score += 5
    return {'lead_score': min(score, 100)}