#import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey_it = os.environ['apikey']
url_it = os.environ['url']

authenticator = IAMAuthenticator(apikey_it)
language_translator = LanguageTranslatorV3(version='2018-05-01',
authenticator=authenticator)

def english_to_french(english_text):
    translate_response = language_translator.translate(text=english_text,
    model_id='en-fr').get_result()
    french_text = translate_response['translation'][0]['translation']
    return french_text

def french_to_english(french_text):
    translate_response = language_translator.translate(text=french_text,
    model_id='fr-en').get_result()
    english_text = translate_response['translation'][0]['translation']
    return english_text
