import pyttsx3
import speech_recognition as sr
import subprocess

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
    except sr.RequestError as e:
        speak("Speech recognition error: {str(e)}")
    return "" #makes the  user to repeat the command until recognized


if __name__ == '__main__':
    speak('Vanakam daa maapla')
    while True:
        query = takecommand()
        if 'open firefox' in query:
            try:
                subprocess.Popen(['firefox'])
            except Exception as e:
                print("Error launching Firefox: {str(e)}")
        elif 'open vlc' in query:
            try:
                subprocess.Popen(['vlc'])
            except Exception as e:
                print("Error launching vlc: {str(e)}")