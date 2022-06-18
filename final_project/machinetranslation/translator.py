'''
This module build a translator that can translate English to French and vice versa.
Using IBM Watson API.
'''
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.ibm.com'
    )


def englishToFrench(englishText):
    '''
    This function receives a trunck of english text to be translated,
    and returns the French version as output.
    '''
    translation = language_translator.translate(
        text=englishText,
        source='English',
        target='French'
    ).get_result()
    return translation["translations"][0]["translation"]

def frenchToEnglish(frenchText):
    '''
    This function receives a trunck of french text to be translated,
    and returns the English version as output.
    '''
    translation = language_translator.translate(
        text=frenchText,
        source='French',
        target='English'
    ).get_result()
    return translation["translations"][0]["translation"]
