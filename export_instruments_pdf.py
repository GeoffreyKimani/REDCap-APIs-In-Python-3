"""
#####################################################################
##                                                                 ##
##       EXPORT INSTRUMENTS PDF                                    ##
##                                                                 ##
#####################################################################
"""
import io

import pycurl

data = {
    'token': ['api_token_here'],
    'content': 'pdf',
    'format': 'json'
}

buf = io.BytesIO()

ch = pycurl.Curl()
ch.setopt(ch.URL, ['api_url_here'])
ch.setopt(ch.HTTPPOST, list(data.items()))
ch.setopt(ch.WRITEFUNCTION, buf.write)
ch.perform()
ch.close()

f = open('instruments.pdf', 'wb')
f.write(buf.getvalue())
f.close()

buf.close()
