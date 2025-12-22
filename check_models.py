import google.generativeai as genai
import os
from dotenv import load_dotenv

# Loads credentials
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Asks the API what is available
print("--- Available Models for Generation ---")
try:
    for m in genai.list_models():
        # I only want models that can 'generateContent' (chat models)
        if 'generateContent' in m.supported_generation_methods:
            print(f"Name: {m.name}")
except Exception as e:
    print(f"Error checking models: {e}")
