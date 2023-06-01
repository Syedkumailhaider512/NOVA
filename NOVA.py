import re
import datetime
import os
import random
import openai
import speech_recognition as sr
import pyttsx3 as pt
#import nova_eyes as ne
import webbrowser
import time
import spacy
import pytextrank
import nltk



#name = ne.eye()
name = "Kumail"
if "Someone" in name:
    name = name.replace("Someone", "")

nlp = spacy.load("en_core_web_lg")
nlp.add_pipe("textrank")

engine = pt.init('sapi5')
voice = engine.getProperty('voices')
male = voice[0].id
female = voice[1].id
# print(voice)
engine.setProperty('voice', female)




def speak(text):
    engine.say(text)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 5:
        n_wish = {"Hello Sir!", "hi sir", "hi sir . how are you", "hello sir. how are you"}
        n_item = random.choice(list(n_wish))
        speak(n_item)

    elif hour > 5 and hour <= 11:
        m_wish = {"morning sir", "good morning sir", "morning. how are you sir", "how are you sir",
                  "Have a good morning sir"}
        m_item = random.choice(list(m_wish))
        speak(m_item)

    elif hour > 11 and hour <= 15:
        a_wish = {"good afternoon sir", "afternoon sir", "how are you sir", "good afternoon sir. let's work together",
                  "good afternoon sir. it's time to work", "Have a good afternoon sir"}
        a_item = random.choice(list(a_wish))
        speak(a_item)


    elif hour > 16 and hour <= 19:
        e_wish = {"evening " + name, "good evening " + name + " . how was the day", "Have a good evening "+ name, "Good Evening "+ name}
        e_item = random.choice(list(e_wish))
        speak(e_item)

    else:
        # speak("Hello Sir!")
        wish = {"Hi " + name + " . how are you", "Good Evening " + name , "How was the day "+ name, "hello " + name + " . how are you"}
        item = random.choice(list(wish))
        speak(item)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 400
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en_in')
        print(f"User: {query}\n")

    except Exception as e:
        print("Say that again please!")
        # speak("Say That Again please")
        return "None"

    return query


openai.api_key = "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"


prompt = "NOVA(Naturally Oriented Voice Assistant), Use for various tasks!"


def openai_create(prompt):

    try:
        response = openai.Completion.create(

            model="text-davinci-003",
            prompt=prompt,
            temperature=0.9,
            max_tokens=2500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" User:", " NOVA:"]
        )

    except Exception as e:
        print("Sorry Internet is down!")
        return "None"

    return response.choices[0].text


exit_res = {"Good Bye Sir!", "Good Bye", "Good Bye Dear", "Bye", "I'm going to sleep... bye", "okay  bye", "take care",
            "thanks for giving time .. bye", "okay sir.. i'm working on background tasks..  bye"}
exit_item = random.choice(list(exit_res))


wishMe()

while True:
    #query = takeCommand().lower()
    query = input("\nEnter Your Query: ").lower()

    if "exit" in query or "good bye" in query or "bye" in query:
        print(exit_item)
        speak(exit_item)
        break


    elif "remember that" in query:
        reply = query.replace("remember that my", "Remembered! That Your")
        print(reply)
        speak(reply)
        reply = reply.replace("Remembered! That ", "")
        with open("D:\\Programming\\Python\\Research Work\\NOVA\\NOVA\\Brain\\MemoryBrain.txt", 'a+') as f:
            f.write(reply + "\n")


    elif "remember" in query:
        reply = query.replace("remember my", "Remembered! Your")
        print(reply)
        #speak(reply)
        reply = reply.replace("Remembered! ", "")
        speak(reply)
        with open("D:\\Programming\\Python\\Research Work\\NOVA\\NOVA\\Brain\\MemoryBrain.txt", 'a+') as f:
            f.write(reply + "\n")

    #Last NOVA Functions
    #Some Useful Functions
    elif 'open youtube' in query:
        speak("opening youtube")
        webbrowser.open("www.youtube.com")

    elif 'on youtube' in query:
        search_set = ['searching', 'searching. wait a minute', 'okay sir',
                      'hold your breath. i will search video for you']
        search_use = random.choice(search_set)
        speak(search_use)
        query = query.replace("search", "")
        query = query.replace("on youtube", "")
        result = "https://www.youtube.com/results?search_query=" + query
        time.sleep(1)
        result_set = ['here are some resluts', 'results regard your query', 'searched', 'searched. opening for you',
                      'i have found best matching videos', ""]
        result_use = random.choice(result_set)
        speak(result_use)
        webbrowser.open(result)

    elif 'open' in query and "website" in query:
        query = query.replace("open ", "")
        query = query.replace(" website", "")
        speak("opening" + query)
        webbrowser.open("https://" + query + ".com")


    elif 'open google' in query:
        speak("opening google")
        webbrowser.open("google.com")


    elif 'open facebook' in query:
        speak("opening facebook")
        webbrowser.open("facebook.com")

    elif 'open twitter' in query:
        speak("opening twitter")
        webbrowser.open("twitter.com")

    elif 'open instagram' in query:
        speak("opening instagram")
        webbrowser.open("instagram.com")

    elif 'open linked in' in query:
        speak("opening linked in")
        webbrowser.open("linkedin.com")

    elif 'open quora' in query:
        speak("opening quora for you")
        webbrowser.open("qoura.com")

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir. the time is {strTime}")


    #Conversation
        # conversation

    elif 'fine and you' in query:
        speak("I am everytime fine sir!")
        speak("How may i help you")


    elif 'what is your name' in query:
        speak("sir. my name is nova. Your Personal A I assistant")
        print("Nova. Your Personal AI Assistant!")

    elif 'how i call you' in query:
        speak("Sir you can call me nova. i am Your Personal A I assistant")
        print("Nova. Your Personal AI Assistant!")


    elif 'who are you' in query:
        speak("Sir i am nova. Your Personal A I assistant")
        print("Nova. Your Personal AI Assistant!")

    elif 'how can i call you' in query:
        speak("Sir i am nova. Your Personal A I assistant")
        print("Nova. Your Personal AI Assistant!")

    elif 'shutdown' in query:
        speak("Sorry Sir! i can't shut down the device for you")

    elif 'fine nova' in query:
        fine_wish = {"glad to hear sir", "that's good . sir", "that's great"}
        fine_item = random.choice(list(fine_wish))
        speak(fine_item)

    elif 'thanks' in query:
        pleasure_wish = {"mine pleasure sir", "my pleasure sir", "no need of thanks sir", "that's my job sir"}
        pleasure_item = random.choice(list(pleasure_wish))
        speak(pleasure_item)

    elif 'thank you' in query:
        pleasure_wish = {"mine pleasure sir", "my pleasure sir", "no need of thanks sir", "that's my job sir"}
        pleasure_item = random.choice(list(pleasure_wish))
        speak(pleasure_item)

    elif 'am fine' in query:
        fine_wish = {"glad to hear sir", "that's good . sir", "that's great"}
        fine_item = random.choice(list(fine_wish))
        speak(fine_item)

    elif 'great work' in query:
        thanks_Wish = {"thanks sir", "that's my job sir", "thank you soo much sir", "bundle of thanks sir",
                       "happy to get great remarks sir"}
        thanks_item = random.choice(list(thanks_Wish))
        speak(thanks_item)

    elif 'hello' in query:
        hello_wish = {"hello sir", "hi sir", "hello", "hi"}
        hello_item = random.choice(list(hello_wish))
        speak(hello_item)

    elif 'hi' in query:
        hello_wish = {"hello sir", "hi sir", "hello", "hi"}
        hello_item = random.choice(list(hello_wish))
        speak(hello_item)

    elif 'how are you' in query:
        fine2_wish = {"i'm good", "i am fine", "i'm fine sir", "i'm every time fine sir", "i am good sir"}
        fine2_item = random.choice(list(fine2_wish))
        speak(fine2_item)

    elif 'are you pakistani' in query:
        coun_reply = {"yes i am pakistani", "alhamdullilah pakistani", "yes offcourse", "yes"}
        coun_item = random.choice(list(coun_reply))
        speak(coun_item)

    elif 'where are you from' in query:
        speak("i am from haasilpur pakistan")

    elif "your identity" in query or "your id" in query or "do you have id" in query or "do you have any identity" in query or "do you have identity" in query:
        print("NOVA-12-KS-512")
        speak("yes i have, it is NOVA 12 KS 512")


    elif 'nice to meet you' in query:
        speak("nice to meet you too")

    elif 'excuse me' in query:
        speak("yes. sir?")

    elif 'you speak english' in query:
        speak("yes sir. i'm expert in english")

    elif 'how about you' in query:
        speak("i'm nova. the personal A I assistant of kumaail")

    elif 'your location' in query:
        speak("i am in front of you")

    elif 'what do you do for work' in query:
        speak("sir. i am new born baby A I and try to learn about new things. ")

    elif 'your birth' in query or 'your birthday' in query:
        speak("12 september 2021")

    elif 'you speak english very' in query:
        thanks_Wish = {"thanks sir", "that's my job sir", "thank you soo much sir", "bundle of thanks sir",
                       "happy to get great remarks sir"}
        thanks_item = random.choice(list(thanks_Wish))
        speak(thanks_item)

    elif 'about hasalpur' in query:
        speak(
            "Haasilpur, is a city in Bahawalpur District in southern Punjab, Pakistan. The city is located between the Satluj River and the Indian border and lies 96 km east of the district Bahawalpur.")

    elif 'i love you' in query:
        speak("i love you too")

    elif 'like you' in query:
        speak("thanks sir")

    elif 'do you like racing' in query:
        speak(
            "yes. off course. racing is a competition of speed, against an objective criterion, usually a clock or to a specific point. and sir it's my job to work as fast as i can.")

    elif 'is love' in query:
        speak("It is 7th sense that destroy all other senses")

    elif 'reason for you' in query:
        speak("I was created as a starter project of A I by Mister Syed Kumail Haider ")


    elif 'good job' in query:
        thanks_Wish = {"thanks sir", "that's my job sir", "thank you soo much sir", "bundle of thanks sir",
                       "happy to get great remarks sir"}
        thanks_item = random.choice(list(thanks_Wish))
        speak(thanks_item)

    elif 'good work' in query:
        thanks_Wish = {"thanks sir", "that's my job sir", "thank you soo much sir", "bundle of thanks sir",
                       "happy to get great remarks sir"}
        thanks_item = random.choice(list(thanks_Wish))
        speak(thanks_item)

    elif 'boring' in query:
        speak("why. sir")

    elif 'good day' in query:
        speak("glad to know this sir. how may i help you sir")


    elif "why you came to world" in query or "purpose of creating you" in query:
        speak("Thanks to Kumail. further It's a secret")


    elif "famous places in" in query:
        print("Searching for famous places...")
        speak("searhing for famous places")

        time.sleep(1)
        place_data = {"fount it sir", "sir . i have found it", "sir . i am showing you famous places",
                      "ready for famous places sir "}
        place_set = random.choice(list(place_data))
        speak(place_set)
        google = "www.google.com/"
        webbrowser.open(google + query)


    elif "what is" in query:
        reply = openai_create(query)
        print(reply)
        speak(reply)
        reply = reply.replace("\n", "")
        query = query.replace("?", "")
        with open("D:\\Programming\\Python\\Research Work\\NOVA\\NOVA\\Brain\\QuestionAnswering.txt",
                  'a+') as f:
            f.write("Q: " + query.capitalize() + "?\n" + "Ans: " + reply + "\n-------------------------\n")


    elif "who is" in query:
        query1 = query.replace("who is ", "")
        query1 = query1.title()
        file = open("D:\\Programming\\Python\\Research Work\\NOVA\\NOVA\\Brain\\Persons.txt", 'r')
        lines = file.readlines()
        file.close()
        a = 0
        for line in lines:
            if query1 in line:
                if "None" not in line:
                    a = 1
                    line1 = line.split(" : ")
                    print(line)
                    speak(line1[1])
                else:
                    print("Data not Available, Wait I'm searching on internet!")

        if a != 1:
            reply = openai_create(query)
            if reply!= "None":
                print(reply)
                speak(reply)
                query = query.replace("who is ", "")
                query = query.title()
                print(query)
                reply = reply.replace("\n", "")
                with open("D:\\Programming\\Python\\Research Work\\NOVA\\NOVA\\Brain\\Persons.txt",'a+') as f:
                    f.write(query + " : " + reply + "\n-------------------------\n")


    elif "code for" in query or "code of" in query or "write a code" in query or "write a program" in query:
        reply = openai_create(query)
        print(reply)
        speak("Your code is prepared!")
        with open("D:\\Programming\\Python\\Research Work\\NOVA\\NOVA\\Brain\\DataBrain.txt", 'a+') as f:
            f.write("Query: " + query.capitalize() + "?\nReply: " + reply + "\n-------------------------\n")


    elif "about me" in query or "facts about me" in query:
        data = open(r"D:\\Programming\\Python\\Research Work\\NOVA\\NOVA\\Brain\\MemoryBrain.txt",'r')
        reply = data.read()
        print("Yes I know! "+ reply)
        speak(reply)
        speak("did i guess right")
        query = input("Did i Guess Right: ")

        if "yes" in query:
            print("Thank you! "+ '\U0001f632')
            speak("Thank you")

        elif "no" in query:
            print("Sorry")


    elif "discovery of" in query or "discoveries" in query:
        reply = openai_create(query)
        print(reply)
        query = query.replace("?", "")
        with open("D:\\Programming\\Python\\Research Work\\NOVA\\NOVA\\Brain\\Discoveries.txt", 'a+') as f:
            f.write("Query: " + query.title() + "?\nAnswer: " + reply + "\n-------------------------\n")


    else:
        reply = openai_create(query)
        print(reply)
        #speak(reply)
        reply = reply.replace("\n", " ")
        query = query.replace("?","")
        with open("D:\\Programming\\Python\\Research Work\\NOVA\\NOVA\\Brain\\DataBrain.txt", 'a+') as f:
            f.write("Query: " + query.capitalize() + "?\nReply: " + reply + "\n-------------------------\n")


