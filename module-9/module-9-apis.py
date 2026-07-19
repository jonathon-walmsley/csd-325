# Jonathon Walmsley
# 07/19/2026
# Module 9.2
# Purpose: Demonstrate usage of APIs

import requests
import json

def jprint(obj):  
    text = json.dumps(obj, sort_keys=True, indent=4) 
    print(text) 

#
site = 'http://api.open-notify.org/astros.json'
response = requests.get(site)
print('Connecting to ', site)
print('Connection status code:', response.status_code)
print('Response:')
print(response.json())
print('Formatted Response:')    
jprint(response.json())

site = 'https://swapi.dev/api/people/?search=r2'
response = requests.get(site)
print('Connecting to ', site)
print('Connection status code:', response.status_code)
print('Response:')
print(response.json())
print('Formatted Response:')    
jprint(response.json())