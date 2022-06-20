# RealTimeTranslate

Installation
========
Virtual audio driver installation.
[Syncroom Download](https://syncroom.yamaha.com/play/dl/)

Install the module from PyPI.
```
pip install -r requirements.txt
```

Usage
========
1.Obtain API key for translator.  
[Deepl API](https://www.deepl.com/pro-api?cta=header-pro-api)

2.Enter the obtained API key into the config.  
Example : key = 12345678-9abc-def0-1234-56789abcde:fx  
3.Execution method.  
```
python Translate.py
```

Config
========
Configuration of config.
```
- API_KEY -
key 		: 	Deepl API Key.

- TRANSLATE_SETTINGS -
source_lang 	: 	The language you speak.
target_lang	:	Target Language.

- TALK_SETTINGS -
speed		:	Talk Speed.
hide		:	Hide Softalk.
```
