from llm.ollama_client import ask
from core.parser import parse

def interpret(user_input):
    prompt = f"""
You are a computer assistant. Respond ONLY with valid JSON.
No explanation. No markdown. No extra text. Just JSON.

You can return MULTIPLE actions.

Break the user input into step-by-step actions.

IMPORTANT RULE:
If the action is "search", do NOT also include "open_browser" for the same site.

Examples:

User: open youtube
{{"action": "open_browser", "site": "youtube"}}

User: search cats on google
{{"action": "search", "query": "cats", "site": "google"}}

User: open youtube and search lo-fi music
[
  {{"action": "search", "query": "lo-fi music", "site": "youtube"}}
]

Allowed formats:
{{"action": "open_browser", "site": "youtube"}}
{{"action": "search", "query": "...", "site": "youtube or google"}}
{{"action": "open_app", "app": "..."}}
{{"action": "type_text", "text": "..."}}

User input: {user_input}
JSON:"""

    raw_response = ask(prompt)
    print("RAW:", raw_response)
    parsed = parse(raw_response)

    if parsed is None:
        return []

    return parsed
    
if __name__ == "__main__":
    result = interpret("open youtube")
    print(result)
