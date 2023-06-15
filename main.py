
import pyttsx3
import speech_recognition as sr
import subprocess
import pyautogui
import datetime
import time

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[15].id)


def speak(audio):
    try:
        engine.say(audio)
        engine.runAndWait()
    except Exception as e:
        print(f"Text-to-speech error: {str(e)}")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Waiting...')
        query = r.recognize_google(audio, language='en')
        print('User said:', query)
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you please repeat?")
    except sr.RequestError as e:
        speak(f"Speech recognition error: {str(e)}")
    return ""


def open_application(app):
    try:
        subprocess.Popen([app])
        speak(f"Opening {app}")
    except Exception as e:
        speak(f"Error opening {app}: {str(e)}")


def copy_text():
    pyautogui.hotkey('ctrl', 'a') # Select all text
    time.sleep(0.5) # Wait for selection to take effect
    pyautogui.hotkey('ctrl', 'c') # Copy selected text


def paste_text():
    pyautogui.hotkey('ctrl', 'v') # Paste copied text


def wish():
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        speak("Good morning!")
    elif 12 <= current_hour < 17:
        speak("Good afternoon!")
    elif 17 <= current_hour < 20:
        speak("Good evening!")
    else:
        speak("Good night!")


if __name__ == '__main__':
    wish()
    while True:
        query = takecommand()
        if query:
            words = query.split()
            if 'open' in words:
                app = ' '.join(words[1:])
                open_application(app)
            elif 'scroll up' in query:
                pyautogui.scroll(100)
            elif 'scroll down' in query:
                pyautogui.scroll(-100)
            elif 'close' in query:
                pyautogui.hotkey('alt', 'f4') # Close the current window
            elif 'back' in query:
                pyautogui.hotkey('alt', 'left') # Go back in the browser
            elif 'type' in query:
                text = ' '.join(words[1:])
                pyautogui.typewrite(text)
            elif 'copy' in query:
                copy_text()
            elif 'paste' in query:
                paste_text()
            else:
                speak("Sorry, I couldn't understand the command.")

