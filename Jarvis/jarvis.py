import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr #pip install SpeechRecognition
import wikipedia #pip install wikipedia 
import smtplib
import webbrowser as wb
import os
import tekore as tk #pip install tekore
import pyautogui #pip install pyautogui
import psutil #pip install psutil
import pyjokes #pip install pyjokes
import tweepy
#from youtube_search import YoutubeSearch #pip install youtube-search

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back")
    hour = datetime.datetime.now().hour
    if hour >=6 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afteroon")
    elif hour >=18 and hour<24:
        speak("Good evening")
    else:
        speak("Good night")
    speak("Jarvis at your service. please tell me how can i help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please.....")
        return None

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('bannudatta@gmail.com', '')
    server.sendmail('bannudatta@gmail.com', to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("D:\Jarvis\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at " + usage)
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)


def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("searching....")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'google' in query:
            try:
                from googlesearch import search
            except ImportError:
                print("No module name google found")
            speak("searching...")
            query = query.replace("google","")
            for j in search(query, tld="co.in", num=2, stop=2, pause=2):
                print(j)
                speak(j)
        elif 'send email' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = 'abhinav2119@gmail.com'
                sendEmail(to, content)
                speak(content)
                speak("Email has been sent!")

            except Exception as e:
                print(e)
                speak("Unable to send the mail")

        elif 'search in chrome' in query:
            speak("what should I search?")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+ '.com' )

        elif 'log out' in query:
            os.system("shutdown -1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")
        
        elif 'play songs' in query:
            songs_dir = 'D:\Music'
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif 'spotify' in query:
            conf = ('6f816838105249aeb04f3cf6fc056fa3', 'ab46488fbfa04080a16c85b06fe1217a','https://www.google.com/')
            token = tk.prompt_for_user_token(*conf, scope=tk.scope.every)

            spotify = tk.Spotify(token)
            tracks = spotify.current_user_top_tracks(limit=10)
            spotify.playback_start_tracks([t.id for t in tracks.items])

        elif 'remember that' in query:
            speak("what should I remember")
            data = takeCommand()
            speak("you said me to remember that" + data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that"+ remember.read())

        elif 'screenshot' in query:
            screenshot()
            speak("done")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'climate' in query:
            import requests, json 
            api_key = "e04780fcb03a553d76fd0257919e9617"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            speak("City name sir!")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
            response = requests.get(complete_url) 
            x = response.json()  
            if x["cod"] != "404": 
                y = x["main"] 
                current_temperature = y["temp"] 
                current_pressure = y["pressure"]  
                current_humidiy = y["humidity"] 
                z = x["weather"] 
                weather_description = z[0]["description"]  
                speak(" Temperature (in Celsius unit) = " +
                            str(current_temperature-273.15) +" degree Celsius"+
                "\n humidity (in percentage) = " +
                            str(current_humidiy) +
                "\n description = " +
                            str(weather_description)) 
                               
                               
                print(" Temperature (in Celsius unit) = " +
                            str(current_temperature-273.15) +" degree Celsius"+
                "\n humidity (in percentage) = " +
                            str(current_humidiy) +
                "\n description = " +
                            str(weather_description))
            else: 
                speak(" City Not Found ") 


        elif 'twitter' in query:
            API_key = 'vdINbSpMYQpKtC3Nh1ZnmYtC9'
            API_key_secret = 'YdChD3OOTRl6QgT7HsCNbNY3x0zdjfeYv4bGzw4DPt5OmPSDEO'
            Access_token ='1278607790995464192-gfj6hZOCXvA2oCdowLc9lT2WjP2grs'
            Access_token_secret = 'L1jW2VmsmviBtds8ASGxQ0jv5rBnel3KZmUj1TD25j5Wu'
            def OAuth():
                try:
                    auth = tweepy.OAuthHandler(API_key,API_key_secret)
                    auth.set_access_token(Access_token,Access_token_secret)
                    return auth
                except Exception as e:
                    return None
            oauth = OAuth()
            api = tweepy.API(oauth)
            speak("provide your tweet content")
            tweet_content=takeCommand().capitalize()
            speak("whom do you want to tag")
            tweet_tag=takeCommand().replace(" ","").lower()
            api.update_status(tweet_content+ " @" +tweet_tag)
            speak(tweet_content)
            print(tweet_content)
            print('A tweet is successfully posted')
            speak('A tweet is successfully posted')
        elif 'dict' in query:
            import requests

            url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
            speak("term please")
            term = takeCommand()
            

            querystring = {"term":term}

            headers = {
                'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
                'x-rapidapi-key': "1742a8b347mshfc484bc16ebe2cep1a84a3jsn5f9bad79032e"
                }

            response = requests.request("GET", url, headers=headers, params=querystring)

            print(response.text)

        elif "currency rate" in query:
            import requests

            url = "https://currency-exchange.p.rapidapi.com/exchange"
            speak("convert from")
            convert_from=takeCommand()
            speak("convert to")
            convert_to = takeCommand()
            querystring = {"q":"1.0","from":convert_from,"to":convert_to}

            headers = {
                'x-rapidapi-host': "currency-exchange.p.rapidapi.com",
                'x-rapidapi-key': "1ba82898b2msh5b3a5efd54ecdefp109aaajsnf76bd900f3e5"
                }

            response = requests.request("GET", url, headers=headers, params=querystring)

            speak(response.text)
            print(response.text)
        elif "maps" in query:
            import googlemaps
            from datetime import datetime

            gmaps = googlemaps.Client(key='AIzaSyAI4dQT9Zp-X_vSD9F5Zmm2Jifg0t43wIM')

            # Geocoding an address
            geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

            # Look up an address with reverse geocoding
            reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

            # Request directions via public transit
            now = datetime.now()
            directions_result = gmaps.directions("Sydney Town Hall",
                                                "Parramatta, NSW",
                                                mode="transit",
                                                departure_time=now)
        elif "whatsapp" in query:
            import pywhatkit
            import datetime
            hour = int(datetime.datetime.now().hour)
            minute = int(datetime.datetime.now().minute)
            speak("message you'd like to send")
            str_message=takeCommand()
            print(str_message)
            pywhatkit.sendwhatmsg("+919121450012",str_message,hour,minute+2)
            speak("message successfully sent")
            print("message successfully sent")

        elif "service provider" in query:
            import http.client

            conn = http.client.HTTPSConnection("ajith-indian-mob-info.p.rapidapi.com")

            headers = {
                'x-rapidapi-host': "ajith-indian-mob-info.p.rapidapi.com",
                'x-rapidapi-key': "c2a4e50045msh1256bb8df5fe8e3p1d37b6jsn6aef23afefca"
                }

            conn.request("GET", "/employees?mobno=9100305069", headers=headers)

            res = conn.getresponse()
            data = res.read()

            speak(data.decode("utf-8"))
            
        elif 'offline' in query:
            quit()
