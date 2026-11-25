import pyautogui
import time
from datetime import datetime

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5


import pyautogui
import time

print("Step 1: Open Chrome...")

pyautogui.hotkey('command', 'space', interval=0.1)
time.sleep(1)

pyautogui.write('chrome', interval=0.15)
time.sleep(1)

pyautogui.press('enter')
time.sleep(3)

print("Step 2: Go to the website...")

pyautogui.hotkey('command', 't', interval=0.1)
time.sleep(1)

pyautogui.write('https://www.google.com', interval=0.15)
pyautogui.press('enter')

time.sleep(3)

print("Website opened successfully!")


from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://www.google.com")

    print("Google opened successfully!")

    page.wait_for_timeout(5000)

    browser.close()