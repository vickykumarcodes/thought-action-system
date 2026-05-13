from actions import browser, system, typing

def execute(actions):
    opened_sites = set()

    # 🔥 FIRST PASS — run all searches
    for action in actions:
        if action['action'] == "search":
            print("RUNNING:", action)

            query = action.get('query', '')
            site = action.get('site', 'google')

            opened_sites.add(site)
            browser.search(query, site)

    # 🔥 SECOND PASS — run other actions
    for action in actions:
        action_type = action['action']

        if action_type == "open_browser":
            site = action.get("site")

            if site in opened_sites:
                continue

            print("RUNNING:", action)

            if site == "youtube":
                browser.open_youtube()
            elif site == "google":
                browser.open_url("https://www.google.com")

        elif action_type == "open_app":
            print("RUNNING:", action)
            system.open_app(action['app'])

        elif action_type == "type_text":
            print("RUNNING:", action)
            typing.type_text(action['text'])

if __name__ == "__main__":
    test_actions = [
        {"action": "open_browser", "site": "youtube"},
        {"action": "search", "query": "flats in delhi", "site": "google"},
        {"action": "open_app", "app": "notepad"},
        {"action": "type_text", "text": "Hello Vicky"}
    ]

    execute(test_actions)

