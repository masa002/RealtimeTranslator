import subprocess
import webbrowser
import configparser
import sys

import speech_recognition as sr
import deepl

def Say(text):
    try:
        _start = "start ./softalk/softalk.exe"
        _speed = "/S:" + config.get('TALK_SETTINGS', 'speed')
        _hide = "/X:1" if config.getboolean('TALK_SETTINGS', 'hide') else ""
        _word = "/W:" + text
        _command = [_start, _speed, _hide, _word]

        subprocess.run(' '.join(_command), shell=True)
    
    except:
        print("Softalk Error")
        return

def Translate(text, target_langs):
    try:
        target_lang = target_langs[1]
        translator = deepl.Translator(key)

        result = translator.translate_text(text, target_lang=target_lang).text

    except:
        print("Translation Error")
        return

    Say(result)

def main(source_langs, target_langs):
    source_lang = source_langs[0]

    while True:
        print("Say something ...")

        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        print ("Now to recognize it...")
        try:
            text = r.recognize_google(audio, language=source_lang)
            print(source_lang + " : " + text)

            if text == "ストップ" or text == "stop":
                subprocess.run("start ./softalk/softalk.exe /close_now", shell=True)
                print("end")
                break

            print ("Now to translate it...")
            Translate(text, target_langs)

        except sr.UnknownValueError:
            print("could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))



if __name__ == '__main__':
    try:
        r = sr.Recognizer()
        mic = sr.Microphone()

        lang = {'en-US':['en-US', 'en-US'],
                'en-GB':['en-GB', 'en-GB'],
                'zh-ZH':['zh', 'zh'],
                'id-ID':['id-ID', 'ID'],
                'de-DE':['de-DE', 'DE'],
                'fr-FR':['fr-FR', 'FR'],
                'it-IT':['it-IT', 'IT'],
                'ja-JP':['ja-JP', 'JA']
        }

        config = configparser.ConfigParser()
        config.read('./config.ini')

        key = config.get('API_KEY', 'key')
        if key == "":
            print("Please Enter the API key for deepl in the config.ini")
            webbrowser.open('https://www.deepl.com/pro-api?cta=header-pro-api', autoraise=True)
            sys.exit(0)

        source_langs = lang[config.get('TRANSLATE_SETTINGS', 'source_lang')]
        target_langs = lang[config.get('TRANSLATE_SETTINGS', 'target_lang')]
    
    except:
        print("Loading Error")

    main(source_langs, target_langs)