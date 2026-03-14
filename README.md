# Riverwood Estate — AI Voice Agent

An AI-powered voice agent prototype for Riverwood Estate's 
customer relations CRM system.

## Features
- Natural conversation flow with context memory
- Voice input using Groq Whisper
- Voice output using ElevenLabs
- LLM responses using Groq
- FastAPI Python backend

## Tech Stack
- FastAPI + Uvicorn
- Groq (LLM + Speech to Text)
- ElevenLabs (Text to Speech)
- Python + HTML/CSS/JavaScript

## Setup
1. Clone the repository
2. Install dependencies: `pip3 install -r requirements.txt`
3. Create .env file with your API keys
4. Run: `uvicorn main:app --reload` 