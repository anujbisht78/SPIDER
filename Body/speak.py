import pyttsx3

def speak(audio):
    engine = pyttsx3.init('sapi5')  # creating a voice engine
    voices = engine.getProperty('voices')
    engine.setProperty('rate',210) #speed of spider
    
    # it will activate the voices from engine
    ID=r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voices', ID) # print(voices[1].id) id of the voices 0:david and 1:zira
    # print("")
    print(f"==> Spider: {audio}")
    # print("")
    engine.say(audio)
    engine.runAndWait()