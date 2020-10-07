import pyttsx3
import speech_recognition as sr
from PIL import Image
from pytesseract import image_to_string

engine = pyttsx3.init()

def sayToMe(talk):
    engine.say(talk)
    engine.runAndWait()

sayToMe("Thell me")

record = sr.Recognizer()
try:
    while True:
        with sr.Microphone(device_index=0) as source:
            print("Thell me..")
            audio = record.listen(source)
            result = record.recognize_google(audio, language="en")
            result = result.lower()
            print(result)

        if result == "write to file":
            text = image_to_string(Image.open('photo.png'))
            with open('image_text.txt', 'w') as file:
                file.write(text)
                print(text)
                sayToMe("the text was recognized and written to a file image_text.txt")

        if result == "read file":
            with open('image_text.txt', 'r') as file:
                print('read!!! '+ file.read())
                sayToMe("the text was read from a file image_text.txt and output to the console")

        if result == "exit":
            sayToMe("ok, bye")
            break

except sr.UnknownValueError:
    sayToMe("The voice was not recognized")
except sr.RequestError:
    sayToMe("Something went wrong")