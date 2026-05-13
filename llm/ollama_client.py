import requests

def ask(prompt):
    url = "http://localhost:11434/api/generate"

    payload = {
            "model": "llama3:latest",
            "prompt": prompt,
            "stream": False
            }

    response = requests.post(url, json=payload)
    return response.json()["response"]

if __name__ == "__main__":
    prompt = """
Respond ONLY in valid JSON.
No explanation.

Format:
{
    "action": "open_browser",
    "site": "youtube"
}
User input : open youtube
"""
    print(ask(prompt))
