import configparser

import pyttsx3
import speech_recognition as sr
import deepl

def Say(data):
    s.say(data)  
    s.runAndWait()

def Translate(text):
    try:
        source_lang = lang[0]
        target_lang = lang[1]
        translator = deepl.Translator(config.get('API_KEY', 'key'))

        result = translator.translate_text(text, target_lang="en-US").text

        Say(result)
        
    except:
        return

def main():
    language = lang[0]

    while True:
        print("Say something ...")

        #雑音対策
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        print ("Now to recognize it...")
        try:
            text = r.recognize_google(audio, language=language)
            print(lang[mode] + " : " + text)

            # ストップといって終了
            if text == "ストップ" or text == "stop":
                print("end")
                break

            print ("Now to translate it...")
            Translate(text)

        # エラー処理
        except sr.UnknownValueError:
            print("could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))



if __name__ == '__main__':
    s = pyttsx3.init()
    r = sr.Recognizer()
    mic = sr.Microphone()
    lang = []

    config = configparser.ConfigParser()
    config.read('./config.ini')

    lang.append(config.get('TRANSLATE_SETTINGS', 'source_lang'))
    lang.append(config.get('TRANSLATE_SETTINGS', 'target_lang'))

    main()