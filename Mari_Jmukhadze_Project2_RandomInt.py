#Mariam Jmukhadze Project N2 Random 16bit Number Generator using voice recognition

import quantumrandom
import speech_recognition as sr


keywords = ['please, write random number', 'write random number', 'run random number generator']

rec = sr.Recognizer()

try:
    with sr.Microphone() as source:
        print('Say something in English')
        rec.adjust_for_ambient_noise(source)
        data = rec.record(source, duration=3)
        res = rec.recognize_google(data, language='eng')

    # print(res)


except sr.UnknownValueError:
    print('Program has no data to manipulate, please say something or talk in English to run the program')

except sr.RequestError:
    print("Couldn't request results from Google SR service. Please, try again. Thank you!")

else:
    if res in keywords:
        num = quantumrandom.get_data(data_type='uint16')
        print(num)
    else:
        print('please, try again.')