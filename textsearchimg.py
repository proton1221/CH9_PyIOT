# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RCTMpHh2qUuCkMI6mwrdeoizMOspriPz
"""

pip install google-api-python-client

api_key = "AIzaSyB_nnQaFjo6E1LVwhGmVRq0CXbJA4jaFNI"

from apiclient.discovery import build
resource = build("customsearch", 'v1', developerKey=api_key).cse()

result = resource.list(q='parth shinde', cx='016706604653895416842:9gmnojn1ucw').execute()
result['items'][0]

len(result['items'])

for item in result['items']:
    print(item['title'], item['link'])

result = resource.list(q='parth shinde', cx='016706604653895416842:9gmnojn1ucw', searchType='image').execute()
print(result)

for item in result['items']:
    print(item['title'], item['link'])
