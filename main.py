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
                sayToMe("текст был распознан и записан в файл image_text.txt")

        if result == "read file":
            with open('image_text.txt', 'r') as file:
                print('read!!! '+ file.read())
                sayToMe("текст был считан из файла image_text.txt и выведен в консоль")

        if result == "exit":
            sayToMe("давай до свидания")
            break

except sr.UnknownValueError:
    sayToMe("Голос был не распознан")
except sr.RequestError:
    sayToMe("Что-то пошло не так")