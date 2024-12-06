import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import time


#function of speech recognition
def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing..")
            data = recognizer.recognize_google(audio)
            print(data)
            return data

        except sr.UnknownValueError:
            print("Not Understand")

##sptext()

def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

#speechtx("hello welcome to pda college of engineering")

if __name__== "__main__":
     

    #if "hey siri" in sptext().lower():

        while True:
        #print("test")
                    data1=sptext().lower()

                    if "your name" in data1:
                        name = "my name is Nihal"
                        speechtx(name)

                    elif "old are you" in data1:
                        age = "i am Twenty year old"
                        speechtx(age)

                    
                    elif "time" in data1:
                        time = datetime.datetime.now().strftime("%I%M%p")
                        #date_only = now.strftime("%Y-%m-%d")
                        speechtx(time)

                    elif "date" in data1:
                       now = datetime.datetime.now()
                       speechtx(now)

                    elif "college" in data1:
                        webbrowser.open("https://pdacek.ac.in/")

                    elif "joke" in data1:
                        joke_1=pyjokes.get_joke(language="en",category="neutral")
                        print(joke_1)
                        speechtx(joke_1)

                    elif "exit" in data1:
                        speechtx("thank you")
                        break
                        
                        time.sleep(2)
        

else:
    print("thanks")