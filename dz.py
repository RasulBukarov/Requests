import requests
from pprint import pprint
max = 0
name = ''
response_Hulk = requests.get('https://superheroapi.com/api/2619421814940190/332')
response_Captain_America = requests.get('https://superheroapi.com/api/2619421814940190/149')
response_Thanos = requests.get('https://superheroapi.com/api/2619421814940190/655')
hulk_int = response_Hulk.json()['powerstats']['intelligence']
capitan_int = response_Captain_America.json()['powerstats']['intelligence']
thanos_int = response_Thanos.json()['powerstats']['intelligence']

if (int(hulk_int) > max):
    max = int(hulk_int)
    name = 'Hulk'
if (int(capitan_int) > max):
    max = int(capitan_int)
    name = 'capitantain America'
if (int(thanos_int) > max):
    max = int(thanos_int)
    name = 'Thanos'
print(f'Самый умный - {name}')
