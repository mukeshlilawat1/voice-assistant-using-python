import random
import ollama
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime
import pyautogui
import pyperclip
import screen_brightness_control as sbc
import ctypes
import psutil


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def set_brightness(level):
    try:
        command = f"(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{level})"
        os.system(f'powershell -Command "{command}"')
        say(f"Brightness set to {level} percent")
    except Exception as e:
        say("Failed to set brightness.")
        print("Error:", e)


def increase_brightness():
    try:
        current = sbc.get_brightness(display=0)[0]  # current brightness
        new_brightness = min(100, current + 20)     # max 100
        sbc.set_brightness(new_brightness)
        say(f"Brightness increased to {new_brightness} percent")
    except Exception as e:
        say("Failed to change brightness")
        print(e)

def decrease_brightness():
    try:
        current = sbc.get_brightness(display=0)[0]
        new_brightness = max(0, current - 20)
        sbc.set_brightness(new_brightness)
        say(f"Brightness decreased to {new_brightness} percent")
    except Exception as e:
        say("Failed to change brightness")
        print(e)


def take_Command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            print("Recognizing, please wait...")
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception:
            print("Sorry, I did not understand that. Please try again.")
            return ""

if __name__ == '__main__':
    print("Starting speech recognition...")
    say("Hello, I am your Jarvis AI. How can I assist you today?")

    while True:
        print("Waiting, I am listening...")
        query = take_Command()
        matched = False

        if not query:
            continue

        # Websites
        site = [
            ["youtube", "https://www.youtube.com"],
            ["google", "https://www.google.com"],
            ["facebook", "https://www.facebook.com"]
        ]
        for sites in site:
            if f"open {sites[0]}" in query.lower():
                say(f"Opening {sites[0]} Sir")
                webbrowser.open(sites[1])
                matched = True
                break

        # Music
        musics = [
            ["open music", "https://youtu.be/2hFcy3S7Pbg?si=xlwbZWy56dv9Hmjj"],
            ["open song", "https://youtu.be/KzKqzvBAhTs?si=Pdxo4OsQ_L6jHcAB"],
            ["open gaana", "https://youtu.be/1qePizAXvUQ?si=wCitH_YNTLc-WpWG"]
        ]
        for music in musics:
            if music[0] in query.lower():
                say(f"Opening {music[0]} sir")
                webbrowser.open(music[1])
                matched = True
                break

        # Time
        if "time" in query.lower():
             hour = datetime.datetime.now().strftime("%H")
             minute = datetime.datetime.now().strftime("%M")
             say(f"Sir Time is {hour} : {minute} Minutes Now ")
             matched = True

        # Windows Apps
        elif "open notepad" in query.lower():
            say("Opening Notepad")
            os.system("start notepad")
            matched = True

        elif "open camera" in query.lower():
            say("Opening Camera")
            os.system("start microsoft.windows.camera:")
            matched = True

        elif "open calculator" in query.lower():
            say("Opening Calculator")
            os.system("start calc")
            matched = True

        elif "open paint" in query.lower():
            say("Opening Paint")
            os.system("start mspaint")
            matched = True

        elif "open command prompt" in query.lower() or "open cmd" in query.lower():
            say("Opening Command Prompt")
            os.system("start cmd")
            matched = True

        elif "open chrome" in query.lower():
            say("Opening Google Chrome")
            os.system("start chrome")
            matched = True

        elif "open code" in query.lower():
            say(f"Opening Visual Studio Code")
            os.system("start code")
            matched = True

        elif "increase volume" in query.lower():
            pyautogui.press("volumeup")
            say("Volume increased")
            matched = True

        elif "decrease volume" in query.lower():
            pyautogui.press("volumedown")
            say("Volume decreased")
            matched = True

        elif "mute volume" in query.lower():
            pyautogui.press("volumemute")
            say("Volume muted")
            matched = True

        elif "unmute volume" in query.lower():
            pyautogui.press("volumemute")
            say("Volume unmuted")
            matched = True

        elif "take screenshot" in query.lower():
            os.system("start ms-screenclip:")
            say("Snipping Tool opened. Please capture manually.")
            matched = True

        elif "increase brightness" in query.lower():
            increase_brightness()  # set brightness to 80%
            matched = True

        elif "decrease brightness" in query.lower():
            decrease_brightness() # set brightness to 30%
            matched = True

        elif "lock screen" in query.lower():
            ctypes.windll.user32.LockWorkStation()
            matched = True

        elif "battery" in query.lower():
            battery = psutil.sensors_battery()
            percent = battery.percent
            say(f"Battery is at {percent} percent")
            matched = True

        elif "ram" in query.lower():
            ram = psutil.virtual_memory()
            say(f"RAM usage is at {ram.percent} percent")
            matched = True

        elif "cpu" in query.lower():
            cpu = psutil.cpu_percent(interval=1)
            say(f"CPU usage is at {cpu} percent")
            matched = True

        elif "clipboard" in query.lower():
            content = pyperclip.paste()
            say("Clipboard contains " + content)
            matched = True

        elif "close youtube" in query.lower() or "close video" in query.lower():
            say("Closing YouTube tab or browser")
            os.system("taskkill /F /IM chrome.exe")
            matched = True


        # Stop
        elif "stop" in query.lower():
            say("Goodbye Sir, have a nice day")
            break
