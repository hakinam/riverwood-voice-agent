### How It Works

1. Operator inputs the customer's phone number
2. VAPI orchestrates the call via Twilio — the customer's phone rings
3. On answer, VAPI routes audio through the conversation pipeline
4. The customer's speech is transcribed in real time
5. Groq LLaMA 3.3 generates a contextual, natural response
6. ElevenLabs synthesises the response into a human-like voice
7. The audio is streamed back to the customer — the loop continues

---

## Version History

### v2 — Outbound Calling System (Current)
- VAPI + Twilio for fully automated outbound phone calls
- Groq LLaMA 3.3 for LLM reasoning
- ElevenLabs for voice synthesis
- Designed to scale to 1000+ customers via queue-based parallel processing

### v1 — Browser-Based Demo
- FastAPI backend orchestrating a speech-to-speech pipeline
- Groq Whisper for speech-to-text
- Groq LLM for response generation
- ElevenLabs for voice output
- HTML/CSS/JS frontend with MediaRecorder API for real-time voice capture

---

## Tech Stack

| Component | Tool |
|---|---|
| Voice Orchestration | VAPI |
| Telephony | Twilio |
| LLM | Groq LLaMA 3.3 |
| Voice Synthesis | ElevenLabs |
| Backend (v1) | FastAPI |
| Speech-to-Text (v1) | Groq Whisper |

---

## Setup

### Prerequisites
- Python 3.9+
- VAPI account with an outbound phone number configured
- Twilio account
- Groq API key
- ElevenLabs API key

### Installation

```bash
git clone https://github.com/hakinam/riverwood-voice-agent
cd riverwood-voice-agent
pip3 install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the root directory:

```env
VAPI_API_KEY=your_vapi_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
GROQ_API_KEY=your_groq_key
ELEVENLABS_API_KEY=your_elevenlabs_key
```

### Run

```bash
python3 call.py
```

Enter the customer's phone number with country code when prompted. 
The call is initiated automatically.

---

## Built By

Innam Ul Haq — [GitHub](https://github.com/hakinam) 
· [LinkedIn](#) ← add your LinkedIn URL
