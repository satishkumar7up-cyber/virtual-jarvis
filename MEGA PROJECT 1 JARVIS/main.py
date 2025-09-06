import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(C):
    if "open google" in C.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in C.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in C.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in C.lower():
        webbrowser.open("https://linkedin.com")
    elif C.lower().startswith("play"):
        song = C.lower().replace("play", "").strip()
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, song not found.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        print("Recognizer...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            Word = recognizer.recognize_google(audio)
            if "jarvis" in Word.lower():
                print("Wake word detected.")
                speak("Yes")
                # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active..")
                    audio = recognizer.listen(source)
                    command = recognizer.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Errore {0}".format(e))


