import wolframalpha
from Body.listen import micExecution
from Body.speak import speak

def WolfRamAlpha(query):
    apikey = "JUV8L7-W69TUEX698"   #Enter Your OWN API KEY
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value is not answerable")

def Calc(query):
    Term = str(query)
    Term = Term.replace("Spider","")
    Term = Term.replace("one","*")
    Term = Term.replace("plus","+")
    Term = Term.replace("minus","-")
    Term = Term.replace("divide","/")

    Final = str(Term)
    try:
        result = WolfRamAlpha(Final)
        print(f"{result}")
        speak(f"The value is: {result}")

    except:
        speak("The value is not answerable")