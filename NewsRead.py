import requests
import json
from Body.speak import speak
from Body.listen import micExecution

def latestnews():
    api_dict = {"business" :"https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=a5eb379a70f64333a7785478dc03376b" ,
            "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=a5eb379a70f64333a7785478dc03376b",
            "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=a5eb379a70f64333a7785478dc03376b",
            "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=a5eb379a70f64333a7785478dc03376b",
            "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=a5eb379a70f64333a7785478dc03376b",
            "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=a5eb379a70f64333a7785478dc03376b"
}

    content = None
    url = None
    speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    
    # field = input("Type field news that you want: ")
    field = micExecution().lower()
    for key ,value in api_dict.items():
        if key.lower() in field.lower():
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts :
        article = articles["title"]
        # print(article)
        speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        speak("Boss Do you want me to Continue?")
        ans=micExecution().lower()
        if ans.lower()=="no" or ans.lower()=="No" or ans.lower()=="enough":
            break
        else:
            pass
        # a = input("[press 1 to cont] and [press 2 to stop]")
        # if str(a) == "1":
        #     pass
        # elif str(a) == "2":
        #     break
    
# latestnews()        
    speak("thats all")