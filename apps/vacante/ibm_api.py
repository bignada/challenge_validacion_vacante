from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import json
from ibm_watson.natural_language_understanding_v1 import CategoriesOptions, EntitiesOptions, Features
from ibm_watson import DiscoveryV1
from .base import get_env_var

class ibm_ner:
    
    def call_watson(self, texto):
            authenticator = IAMAuthenticator(get_env_var('NLU_KEY'))
            natural_language_understanding = NaturalLanguageUnderstandingV1(
                version='2019-07-12',
                authenticator=authenticator
            )
            natural_language_understanding.set_service_url(get_env_var('NLU_URL'))

            response = natural_language_understanding.analyze(
                language="es-MX",
                text=texto,
                features=Features(
                    entities=EntitiesOptions(
                        model=get_env_var('MODEL_ID_KS')
                    ),
                )
                ).get_result()

            return json.dumps(response)
