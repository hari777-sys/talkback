import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice' ,voices[15].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('wait')
        query = r.recognize_google(audio,language='en')
        print('user said', query)
    except Exception as e:
        print(e)
        speak('say  that   again')
if __name__ == '__main__':
    speak('vanakam    daa    maapla')
    takecommand()