import subprocess

APP_PATHS = {
    "notepad": "C:\\Windows\\System32\\notepad.exe",
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "whatsapp": r"C:\Users\kumar\OneDrive\Desktop\WhatsApp.lnk"
    }

def open_app(app_name):
    """
    Opens an application using predefined paths.
    """

    app_name = app_name.lower()

    if app_name in APP_PATHS:
        path = APP_PATHS[app_name]

        try:
            subprocess.Popen(["cmd", "/c", "start", "", path])
            print(app_name + " opened successfully.")

        except FileNotFoundError:
            print(f"Executable not found at path: {path}")

    else:
        try:
            subprocess.Popen(["cmd", "/c", "start", "", app_name])
            print(app_name + " opened using Windows search.")

        except Exception as e:
            print(f"Failed to open {app_name}: {e}")

if __name__ == "__main__":
    open_app("whatsapp")
    #open_app("spotify")
    #open_app("calc")
    #open_app("code")
