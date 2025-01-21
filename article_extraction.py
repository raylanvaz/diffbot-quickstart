import requests
from dotenv import load_dotenv
import os
import json

# Load environment variables from .env file
load_dotenv()

# Get the API token
API_TOKEN = os.getenv("DIFFBOT_API_TOKEN")

if not API_TOKEN:
    raise ValueError("API token is missing. Please set it in the .env file.")

# Diffbot API URL for Article Extraction
url = "https://api.diffbot.com/v3/article"
params = {
    "token": API_TOKEN,
    "url": "https://www.diffbot.com/"
}

response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    print("Extracted Data:", json.dumps(data, indent=2))
else:
    print("Error:", response.status_code, response.text)