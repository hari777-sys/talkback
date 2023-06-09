import speech_recognition as sr
listener = sr.Recognizer()
try:
    with sr.Microphone() as source:
        print('listening')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(command)
except Exception:
    print('not working')