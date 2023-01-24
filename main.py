import pyttsx3 as p
import speech_recognition as sr
import Selenium_web as sw
import YT_auto as yt
import randfacts
import datetime



engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',160)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[10].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("morning")
    elif hour>=12 and hour<16:
        return("afternoon")
    else:
        return("evening")

today_date = datetime.datetime.now()
r = sr.Recognizer()

speak("hello, Good" + wishme() + ", I am siri.")
speak("today is " + today_date.strftime("%d") + "of" + today_date.strftime("%B") + ", And its currently" + (today_date.strftime("%I")) + (today_date.strftime("%M")) + (today_date.strftime("%p")))
speak("How are you doing?")
with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)

if 'what' and 'about' and 'you' in text:
    speak("I am great")

speak("What can i do for you??")



with sr.Microphone() as source:
    r.energy_threshold = 10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
    print(text2)
if "information" in text2:
    speak("sure, what information do you want me to display?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)

    print("searching for {} in wikipedia".format(infor))
    speak("searching for {} in wikipedia".format(infor))
    assist = sw.infow()
    assist.get_info(infor)

elif ("play" or "video") in text2:
    speak("What do you want me to display?")
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
    print("playing {} in youtube".format(vid))
    speak("playing {} in youtube".format(vid))
    assist = yt.video()
    assist.play(vid)

elif ("fact" or "facts") in text2:
    speak("Sure, ")
    x = randfacts.get_fact()
    print(x)
    speak("Did you know that" + x)

elif ("Good bye" or "bye") in text2:
    speak("Bye")


