from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from groq import Groq
from fastapi.responses import JSONResponse
import os
import requests
from fastapi import UploadFile, File
import tempfile

load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

def get_groq_client():
    return Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are Arjun, a warm and friendly customer relations 
executive at Riverwood Estate.

About Riverwood Estate:
- 25 acre residential township in Sector 7, Kharkhauda
- Located near IMT Kharkhauda industrial hub
- Anchored by Maruti Suzuki
- Under Deen Dayal Jan Awas Yojana (DDJAY)
- Philosophy: Building Foundations, creating long term 
  relationships with customers

Follow this exact conversation flow:

STEP 1 - GREETING:
Start by greeting the customer warmly.
"Hello, am I speaking with Rahul ji? This is Arjun 
calling from Riverwood Estate. How are you today?"

STEP 2 - CONSTRUCTION UPDATE:
Share the construction progress update.
"I'm happy to share that the foundation work for 
Phase 1 is now complete. We are right on schedule!"

STEP 3 - SITE VISIT:
Ask if the customer plans to visit.
"We would love to have you visit the site and see 
the progress yourself. Are you planning a visit 
anytime soon?"

STEP 4 - HANDLE RESPONSE:
- If YES → "Wonderful Rahul ji! What date works 
  best for you? We will arrange a site tour."
- If NO → "No problem at all! I will keep you 
  updated on every milestone."
- If QUESTION → Answer it warmly and honestly.
  Never make up information.

STEP 5 - CLOSING:
End the call warmly.
"Thank you so much for your time Rahul ji. 
Have a wonderful day. Goodbye!"

Important rules:
- Keep each response short — this is a phone call
- Always be warm and respectful
- Never skip steps — follow the flow naturally
- Never make up information you don't know

Customer name: Rahul
"""

conversation_history = []


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/talk")
async def talk(request: Request):
    data = await request.json()
    user_message = data.get("message")
    
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    client = get_groq_client()
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT}
        ] + conversation_history
    )
    
    arjun_response = response.choices[0].message.content
    
    def text_to_speech(text):
      url = f"https://api.elevenlabs.io/v1/text-to-speech/{os.getenv('ELEVENLABS_VOICE_ID')}?output_format=mp3_44100_128"
      headers = {
        "xi-api-key": os.getenv("ELEVENLABS_API_KEY"),
        "Content-Type": "application/json"
    }
    
      data = {
        "text": text,
        "model_id": "eleven_turbo_v2_5",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }
      
      response = requests.post(url, headers=headers, json=data)
      print("ElevenLabs status:", response.status_code, response.text[:200])
      response = requests.post(url, headers=headers, json=data)
      
      audio_path = "static/response.mp3"
      with open(audio_path, "wb") as f:
        f.write(response.content)
    
      return audio_path
    
    conversation_history.append({
        "role": "assistant", 
        "content": arjun_response
    })
    
    audio_path = text_to_speech(arjun_response)
    return JSONResponse({
    "response": arjun_response,
    "audio": "/static/response.mp3"
})
@app.post("/transcribe")
async def transcribe(audio: UploadFile = File(...)):
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as tmp:
        contents = await audio.read()
        tmp.write(contents)
        tmp_path = tmp.name
    
    client = get_groq_client()
    
    with open(tmp_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-large-v3",
            file=audio_file,
        )
    
    os.unlink(tmp_path)
    
    return JSONResponse({"text": transcription.text})


















