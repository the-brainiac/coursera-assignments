import json
import urllib.request, urllib.parse, urllib.error
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')

parms = dict()
parms['address'] = url
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
# print('Retrieved', len(data), 'characters')

info = json.loads(data)
# print('User count:', len(info))
# print(json.dumps(data,ident=2))
sum=0
for i in info['comments']:
  sum+=int(i['count'])
print(sum)