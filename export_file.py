"""
#####################################################################
##                                                                 ##
##       EXPORT A FILE                                             ##
##                                                                 ##
#####################################################################
"""

import requests

data = {
    'token': ['api_token_here'],
    'content': 'file',
    'action': 'export',
    'record': ['record_id'],
    'field': ['field_name'],
    'event': ['event_arm']
}

r = requests.post(['api_url_here'], data)
print(r.text)
