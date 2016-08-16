import urllib
import json

#Url
#serviceurl = 'http://url/json?'

address = raw_input('Enter location: ')
if len(address) < 1 : exit

url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

try: js = json.loads(str(data))
except: js = None


if 'status' not in js or js['status'] != 'OK':
    print data
    exit

place = js['results'][0]['place_id']
print 'Place id %s' % place

