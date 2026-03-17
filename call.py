import requests
import os
from dotenv import load_dotenv
from assistant import MAYA_ASSISTANT

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
        "assistant": MAYA_ASSISTANT
    }
    
    response = requests.post(url, headers=headers, json=data)
    print("Call status:", response.status_code)
    print("Response:", response.json())
    return response.json()

if __name__ == "__main__":
    phone_number = input("Enter phone number to call along with the country code: ")
    make_call(phone_number)