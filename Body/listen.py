import speech_recognition as sr
from googletrans import Translator
from Body.speak import speak


def takecommand():
    r = sr.Recognizer()  # to define the recognizer
    with sr.Microphone() as source:  # connecting the microphone
        print("")
        print('Listening.....')
        r.pause_threshold = 1  
        audio = r.listen(source,0,5) #for this time period spider can listen

    try:
        print('Recognizing...')
        # taking the query of google search engine
        query = r.recognize_google(audio, language='hi') #"hi"

    # if spidy doesnt recognize you
    except Exception as e:
        # speak('Say that again Please..!')
        return ""
    
    query=str(query).lower()    
    return query 

#for translation from Hindi to English
def translation_hi_to_eng(Text):
    line=str(Text)
    translate= Translator()
    #translating the text
    result=translate.translate(line) #default is english
    data=result.text
    print("")
    print(f"==> You: {data}")
    return data
    
def micExecution():
    query=takecommand()
    data=translation_hi_to_eng(query)
    
    # if len(query)<3:
    #     speak("Boss! I think you forgot to communicate...")
    #     takecommand()
    return data
