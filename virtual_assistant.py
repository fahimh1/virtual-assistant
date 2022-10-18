import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Voice language options
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id3 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
id4 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0'
id5 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_JA-JP_HARUKA_11.0'



# Hear the microphone and return the audio as text
def transform_audio_into_text():

    # Store recogniser in variable
    r = sr.Recognizer()

    # Set micorphone
    with sr.Microphone() as source:

        # Waiting time
        r.pause_threshold = 0.8

        # Report that recording has begun
        print('You can now speak ')

        # Save what you hear as audio
        audio = r.listen(source)

        try:
            # Search on google
            request = r.recognize_google(audio, language='en-gb')

            # test in text
            print('You said ' + request)

            # Return request
            return request
        # Incase it doesn't understand audio
        except sr.UnknownValueError:

            # Show proof that it didn't understand the audio
            print("OOPS! I didn't understand the audio")

            #return error
            return 'I am still waiting'

        # Incase the request cannot be resolved
        except sr.RequestError:

            # Show proof that it didn't understand the audio
            print("OOPS! there is no service")

            #return error
            return 'I am still waiting'

        # Unexpected error
        except:

            # Show proof that it didn't understand the audio
            print("OOPS! something went wrong")

            #return error
            return 'I am still waiting'


# Function so the assistant can be heard
def speak(message):

    # Start engine of pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    # Deliver message
    engine.say(message)
    engine.runAndWait()



# Inform day of the week
def ask_day():

    # Create a variable with today's information
    day = datetime.date.today()
    print(day)

    # Create a variable for the day of the week
    week_day = day.weekday()
    print(week_day)

    # Names of days
    calender = {0: 'Monday',
                1: 'Tuesday',
                2: 'Wednesday',
                3: 'Thursday',
                4: 'Friday',
                5: 'Saturday',
                6: 'Sunday'}
    # Say the day of the week
    speak(f"Today is  {calender[week_day]} ")

# Inform what tie it is
def ask_time():

    # Variable with time information
    time = datetime.datetime.now()
    time = f'At this moment it is {time.hour} hours and {time.minute} minutes.'

    # Say the time
    speak(time)


# Create initial greeting
def initial_greeting():

    # Say greeting
    speak("Hello I am Hazel. How can I help you?")


# Main function of the assistant
def my_assistant():

    # Activate Initial greeting
    initial_greeting()

    # Cutt-off variable
    go_on = True

    # Main loop
    while go_on:

        # Activate microphone and save request
        my_request = transform_audio_into_text().lower()

        if 'open youtube' in my_request:
            speak('Sure, I am opening youtube.')
            webbrowser.open('https://www.youtube.com')
            continue

        elif 'open browser' in my_request:
            speak('Of course, I am on it')
            webbrowser.open('https://google.com')
            continue

        elif 'what day is it today' in my_request:
            ask_day()
            continue

        elif 'what time is it' in my_request:
            ask_time()
            continue

        elif 'do a wikipedia search for' in my_request:
            speak('Ok!, I am looking for it now')
            my_request = my_request.replace('do a wikipedia search for', '')
            answer = wikipedia.search(my_request, sentences= 1)
            speak('According to wikipedia')
            speak(answer)
            continue

        elif 'search the internet for' in my_request:
            speak('Of course, right now')
            my_request = my_request.replace('search the internet for', '')
            pywhatkit.search(my_request)
            speak('This is what I found')
            continue

        elif 'play' in my_request:
            speak("Oh, what a great idea!, I'll play it right now")
            pywhatkit.playonyt()
            continue

        elif 'joke' in my_request:
            speak(pyjokes.get_joke())
            continue


        elif 'stock price' in my_request:

            share = my_request.split()[-2].strip()
            portfolio = {'apple': 'APPL',
                         'amazon': 'AMZN',
                         'google': 'GOOGL'}
            try:

                searched_stock = portfolio[share]
                searched_stock = yf.Ticker(searched_stock)
                price = searched_stock.info['regularMarketPrice']
                speak(f'I found it! The price of {share} is {price}')
                continue

            except:
                speak('I am sorry, but I didn´t find it')
                continue

        elif 'goodbye' in my_request:
            speak('I am going to rest. Let me know if you need anything')
            break



my_assistant()


