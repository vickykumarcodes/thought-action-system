import pyautogui
import time


def type_text(text):
    time.sleep(3)
    pyautogui.write(text)

if __name__ == "__main__":
    type_text("Hello, Vicky")
