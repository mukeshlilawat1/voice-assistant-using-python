import random
import ollama
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime

def ask_ollama(prompt):
    try:
        print("🧠 Asking Ollama AI...")

        response = ollama.chat(
            model='llama3',
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that gives clear and factual answers in one paragraph."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        answer = response.get("message", {}).get("content", "Sorry, no response.")
        print("💬 Ollama says:", answer)
        say(answer)

        if not os.path.exists("Ollama"):
            os.makedirs("Ollama")

        file_path = f"Ollama/prompt_{random.randint(1, 999999)}.txt"
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(f"Prompt: {prompt}\n\nResponse:\n{answer}")

    except Exception as e:
        print("❌ Error:", e)
        say("Sorry, there was an error while talking to the AI.")


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


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
        if "open notepad" in query.lower():
            say("Opening Notepad")
            os.system("start notepad")
            matched = True

        if "open camera" in query.lower():
            say("Opening Camera")
            os.system("start microsoft.windows.camera:")
            matched = True

        if "open calculator" in query.lower():
            say("Opening Calculator")
            os.system("start calc")
            matched = True

        if "open paint" in query.lower():
            say("Opening Paint")
            os.system("start mspaint")
            matched = True

        if "open command prompt" in query.lower() or "open cmd" in query.lower():
            say("Opening Command Prompt")
            os.system("start cmd")
            matched = True

        if "open chrome" in query.lower():
            say("Opening Google Chrome")
            os.system("start chrome")
            matched = True

        if "open code" in query.lower():
            say(f"Opening Visual Studio Code")
            os.system("start code")
            matched = True

        # AI via Ollama
        if "ai" in query.lower():
            ask_ollama(prompt=query)
            matched = True

        # Stop
        if "stop" in query.lower():
            say("Goodbye Sir, have a nice day")
            break
