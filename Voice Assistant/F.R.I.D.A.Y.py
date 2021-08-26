import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import wolframalpha

listener=sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

#define the command functions 
def take_command():
    try:
        with sr.Microphone() as data_taker:
            print("How can I help you?")
            voice=listener.listen(data_taker)
            instruct = listener.recognize_google(voice)
            instruct = instruct.lower()
            print(instruct)
            if 'Friday' in instruct:
                instruct.replace('Friday','')
                print(instruct)
            return instruct
    except:
        pass
def run_friday():
    instruct=take_command()
    app_id='RJGXXQ-A538KGTQKL'
    client=wolframalpha.Client(app_id)
    res=client.query(instruct)
    answer=next(res.results).text
    print(answer)
    talk(answer)
    if 'play' in instruct:
        song=instruct.replace('play','')
        talk('Playing' + song)
        pywhatkit.playonyt(song)
        print(song)
    elif 'time' in instruct:
        time=datetime.datetime.now().strftime('%I:%M')
        print(time)
        talk('Current time is '+time)
    elif 'tell me about' in instruct:
        thing=instruct.replace('tell me about','')
        info=wikipedia.summary(thing)
        print(info)
        talk(info)
    elif 'who are you' in instruct:
        talk('I am your Personal Assistant FRIDAY')
    elif 'who created you' in instruct:
        talk('I was created by Kailash')
    elif 'what can you do for me' in instruct:
        talk('I can play songs, tell time, and help you gain knowledge')
    elif 'bye' in instruct:
        talk('It was great talking to you. See you later')
        exit()
    
    else:
        talk('I am sorry I did not understand, can you repeat it again')
    return "Bye-bye"
while(True):
    run_friday()