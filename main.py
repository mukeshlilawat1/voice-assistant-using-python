import speech_recognition as sr
import pyttsx3
import webbrowser
import os
# Removed: from wikipedia import languages (not used)
import openai  # You can remove this if not used later
import datetime

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def take_Command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # recognizer.pause_threshold = 1
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            print("Recognizing, please wait...")
            query = recognizer.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print("Sorry, I did not understand that. Please try again.")
            return ""  # Important: return empty string to avoid crashing on None

if __name__ == '__main__':
    print("Starting speech recognition...")
    say("Hello, I am your Jarvis AI. How can I assist you today?")

    while True:
        print("Waiting, I am listening...")
        query = take_Command()

        if not query:
            continue  # Skip if query is empty

        site = [
            ["youtube", "https://www.youtube.com"],
            ["google", "https://www.google.com"],
            ["facebook", "https://www.facebook.com"]
        ]
        for sites in site:
            if f"open {sites[0]}" in query.lower():
                say(f"Opening {sites[0]} Sir")
                webbrowser.open(sites[1])
                break

        musics = [
            ["open music", "https://youtu.be/2hFcy3S7Pbg?si=xlwbZWy56dv9Hmjj"],
            ["open song", "https://youtu.be/KzKqzvBAhTs?si=Pdxo4OsQ_L6jHcAB"],
            ["open gaana", "https://youtu.be/1qePizAXvUQ?si=wCitH_YNTLc-WpWG"]
        ]
        for music in musics:
            if music[0] in query.lower():  # Fixed: removed `f"Open{music[0]}"`
                say(f"Opening {music[0]} sir")
                webbrowser.open(music[1])
                break

            if "time" in query.lower():
                # current_time = datetime.datetime.now()
                # formatted_time = current_time.strftime("%H:%M:%S")
                hour = datetime.datetime.now().strftime("%H")
                minute = datetime.datetime.now().strftime("%M")
                say(f"Sir Time is {hour} : {minute} Minutes Now ")
                break

            # Open Windows Applications
            if "open notepad" in query.lower():
                say("Opening Notepad")
                os.system("start notepad")
                break

            if "open camera" in query.lower():
                say("Opening Camera")
                os.system("start microsoft.windows.camera:")
                break


            if "open calculator" in query.lower():
                say("Opening Calculator")
                os.system("start calc")
                break

            if "open paint" in query.lower():
                say("Opening Paint")
                os.system("start mspaint")
                break

            if "open command prompt" in query.lower() or "open cmd" in query.lower():
                say("Opening Command Prompt")
                os.system("start cmd")
                break

            if "open chrome" in query.lower():
                say("Opening Google Chrome")
                os.system("start chrome")
                break

        # if "open music" in query.lower() :
        #     # music_url =
        #    import subprocess, sys
        #
        #    opener = "open" if sys.platform == "darwin" else "xdg-open"
        #      subprocess.call([opener, music_url])



        if "stop" in query.lower():
             say("Goodbye Sir, have a nice day")
             break


