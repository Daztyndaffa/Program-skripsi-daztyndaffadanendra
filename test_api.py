import requests

url = "https://api.maiarouter.ai/v1/chat/completions"

headers = {
    "Authorization": "Bearer sk-Q39Xi-B4IqKA0i-QDy7ICA",
    "Content-Type": "application/json"
}

data = {
    "model": "openai/gpt-4o-mini",
    "messages": [
        {"role": "user", "content": "hai"}
    ]
}

response = requests.post(url, headers=headers, json=data)

print(response.json())