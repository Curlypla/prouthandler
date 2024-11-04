import requests
import json


# Corps de la requête
json_data = {
    "prompt": "dit bonjour 2 fois",
}

# Envoi de la requête POST
response = requests.post(f"http://127.0.0.1:5000/generate", json=json_data)

print(response.json())

