"""
#####################################################################
##                                                                 ##
##       EXPORT WITH JSON FORMAT                                   ##
##                                                                 ##
#####################################################################
"""
import requests

data = {
    'token': ['api_token_here'],
    'content': 'version',
    'format': 'json',
    'returnFormat': 'json'
}

r = requests.post(['api_url_here'], data)
print(r.text)
