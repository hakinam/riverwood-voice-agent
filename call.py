import requests
import os
from dotenv import load_dotenv
from assistant import ARJUN_ASSISTANT

load_dotenv()

def make_call(phone_number):
    url = "https://api.vapi.ai/call/phone"
    
    headers = {
        "Authorization": f"Bearer {os.getenv('VAPI_API_KEY')}",
        "Content-Type": "application/json"
    }
    
    data = {
        "phoneNumberId": os.getenv("VAPI_PHONE_NUMBER_ID"),
        "customer": {
            "number": phone_number
        },
        "assistant": ARJUN_ASSISTANT
    }
    
    response = requests.post(url, headers=headers, json=data)
    print("Call status:", response.status_code)
    print("Response:", response.json())
    return response.json()

if __name__ == "__main__":
    phone_number = input("Enter phone number to call (with country code e.g. +919876543210): ")
    make_call(phone_number)