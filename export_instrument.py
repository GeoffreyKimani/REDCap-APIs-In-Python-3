"""
#####################################################################
##                                                                 ##
##       EXPORT WITH JSON FORMAT AND WRITE TO FILE                 ##
##                                                                 ##
#####################################################################
"""

import requests

data = {
    'token': ['api_token_here'],
    'content': 'instrument',
    'format': 'json',
    'returnFormat': 'json'
}

r = requests.post(['api_url_here'], data)
print(r.text)

with open('instruments.json', 'w') as file:
    file.write(r.text)

"""
#####################################################################
##                                                                 ##
##       EXPORT WITH CSV FORMAT AND WRITE TO FILE                  ##
##                                                                 ##
#####################################################################
"""
import requests
import pandas as pd
from io import StringIO

data = {
    'token': ['api_token_here'],
    'content': 'instrument',
    'format': 'csv',
    'returnFormat': 'csv'
}

r = requests.post(['api_url_here'], data)
df = pd.read_csv(StringIO(r.text))
print(df)

with open('instruments.csv', 'w') as file:
    file.write(r.text)
