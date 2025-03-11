# narrate.py

import os
import requests

# 1) Set up your ElevenLabs API key
API_KEY = "sk_39f7ffa204297b392d2fbc978844c5b0aa6441c06970917d"

# 2) Read the text from a file
with open("script.txt", "r", encoding="utf-8") as f:
    text_content = f.read()

# 3) Send a request to the ElevenLabs Text-to-Speech API
# Using Bill's voice ID: pqHfZKP75CvOlQylNhV4
url = "https://api.elevenlabs.io/v1/text-to-speech/pqHfZKP75CvOlQylNhV4"  # Voice ID for Bill

headers = {
    "Accept": "audio/mpeg",
    "Content-Type": "application/json",
    "xi-api-key": API_KEY
}

payload = {
    "text": text_content,
    "model_id": "eleven_monolingual_v1",
    "voice_settings": {
        "stability": 0.5,          # 50% stability
        "similarity_boost": 0.75,  # 75% similarity
        "style": 0.1,              # 10% style exaggeration
        "speed": 1.0               # Speed 1.0 (normal speed)
    }
}

response = requests.post(url, json=payload, headers=headers)

# 4) Save the audio to an MP3 file
if response.status_code == 200:
    with open("output.mp3", "wb") as out:
        out.write(response.content)
    print("Narration saved to output.mp3")
else:
    print(f"Error: {response.status_code}")
    print(response.text)