import requests

response = requests.post("http://localhost:11434/api/generate", json={
    "model": "llama3.2",
    "prompt": "Who is the Prime Minister of India?",
    "stream": False
})

print(response.status_code)
print(response.json())
