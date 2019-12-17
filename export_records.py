#####################################################################
##                                                                 ##
##       EXPORT WITH JSON FORMAT AND WRITE TO FILE                  ##
##                                                                 ##
#####################################################################

import requests

data = {
    'token': ['api_token_here'],
    'content': 'record',
    'format': 'json',
    'returnFormat': 'json'
}

r = requests.post(['api_url_here'], data)
print(r.text)

with open('records.json', 'w') as file:
    file.write(r.text)
