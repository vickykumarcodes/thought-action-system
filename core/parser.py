import json
import re

def parse(raw_text):
    try:
        matches = re.findall(r'\{.*?\}', raw_text, re.DOTALL)
        results = []
        for match in matches:
            results.append(json.loads(match))
        return results
    except Exception as e:
        print("Parsing failed:", e)
        return None

if __name__ == "__main__":
    sample = """```json
    {
        "action": "open_browser",
        "site": "youtube"
    }
    ```"""

    print(parse(sample))
