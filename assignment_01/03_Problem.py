# import requests

# response = requests.get("https://www.tripadvisor.com/Attraction_Review-g295424-d10687494-Reviews-IMG_Worlds_of_Adventure-Dubai_Emirate_of_Dubai.html")
# print(response.status_code)  # Print the HTTP status code

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello World ")
engine.runAndWait()