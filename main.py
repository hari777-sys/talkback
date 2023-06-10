import pyttsx3
engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')
engine.setProperty('voice' ,voices[12].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == '__main__':
    speak('vanakam    daa    maapla')