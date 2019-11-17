import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from django.core.exceptions import ImproperlyConfigured

with open(os.path.join(BASE_DIR,'config.json')) as f:
 configs = json.loads(f.read())
 
def get_env_var(setting, configs=configs):
 try:
     val = configs[setting]
     if val == 'True':
         val = True
     elif val == 'False':
         val = False
     return val
 except KeyError:
     error_msg = "ImproperlyConfigured: Set {0} environment      variable".format(setting)
     raise ImproperlyConfigured(error_msg)