import pyttsx3
friend = pyttsx3.init()
speech = input("say anything: ")
friend.say(speech)
friend.runAndWait()