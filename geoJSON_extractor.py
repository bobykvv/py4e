address = input('Enter location: ')
service_url = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42
params = dict()
params['address'] = address
params['key'] = api_key
url = service_url + urllib.parse.urlencode(params)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
js = json.loads(data)
print(js['results'][0]['place_id'])
