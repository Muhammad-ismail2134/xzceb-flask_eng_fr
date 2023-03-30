"""
This is a English to French and vise versa Translator
"""
import json
import ibm_watson 
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
#from dotenv import load_dotenv


# apikey = os.environ['16pANfP5tw9OJmbMqPt-0hIWKw2yOZXLWl9oIlt--YJm']
# url = os.environ['https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/805e20a0-f413-4898-8aa0-dfbd2956e451']
authenticator  = IAMAuthenticator('16pANfP5tw9OJmbMqPt-0hIWKw2yOZXLWl9oIlt--YJm')
translator = ibm_watson.LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
translator.set_service_url('https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/805e20a0-f413-4898-8aa0-dfbd2956e451')


def english_to_french(english_text):
    """
    English to French Function
    """
    if english_text is None:
        return "Error: Null input"
    else:
        translation = translator.translate(
            text = english_text,
            model_id = 'en-fr'
        ).get_result()
        french_text = translation['translations'][0]['translation']
        return french_text

def french_to_english(french_text):
    """    
    French to English Function
    """
    if french_text is None:
        return "Error: Null input"
    else:
        translation = translator.translate(
            text = french_text,
            model_id = 'fr-en'
        ).get_result()
        english_text =  translation['translations'][0]['translation']
        return english_text

