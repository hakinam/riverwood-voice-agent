# Riverwood Estate — AI Voice Agent

An AI-powered outbound phone call agent for Riverwood Estate's 
customer relations CRM system.

## What it Does
- Automatically calls customers on their phone
- Greets them naturally and asks for their name
- Shares construction progress updates
- Asks about site visit plans
- Handles questions honestly
- Ends the call warmly

## How to Run
1. Clone the repository
2. Install dependencies: `pip3 install -r requirements.txt`
3. Create .env file with your API keys
4. Run: `python3 call.py`
5. Enter customer phone number with country code
6. The call is initiated automatically

## Tech Stack
- VAPI — AI voice agent orchestration
- Twilio — Telephony and outbound calling
- Groq LLaMA 3.3 — LLM for conversation
- ElevenLabs — Natural voice synthesis
- FastAPI — Browser demo backend (v1)

## Scaling
Queue based parallel processing using AWS SQS and 
AWS Lambda. 50 parallel workers complete 1000 calls 
in under 40 minutes at ~$125 per 1000 calls.
