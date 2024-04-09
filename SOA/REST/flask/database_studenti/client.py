import requests
import json

address = 'http://127.0.0.1:6000'

response = requests.get(address + '/api/v1/resources/students/all')
print('-'*80)
print('RESPONSE')
print(response)
print('-'*80)
print('RESPONSE.CONTENT')
print(response.content)
print('-'*80)
print('RESPONSE.TEXT')
print(response.text)
print('-'*80)
print('RESPONSE.JSON()')
print(response.json())


query = {'id': 3}
response = requests.get(address + '/api/v1/resources/students', params=query)
print('-'*80)
print(json.dumps(response.json(), indent=4, sort_keys=True))

newData = {
    'id': 2,
    'nome': 'Carlo',
    'cognome': 'Neri',
    'immatricolazione': 2015,
    'esami_sostenuti': 24
}

response = requests.post(address + '/api/v1/resources/students', params=newData)
print('-'*80)
print(json.dumps(response.json(), indent=4, sort_keys=True))

response = requests.get(address + '/api/v1/resources/students/all')
print('-'*80)
print(json.dumps(response.json(), indent=4, sort_keys=True))
