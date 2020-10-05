# GET /{module}/{api-format}

import requests

url = "https://munch.emuseum.com/objects/json?key={key}"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))



# GET /{module}/{id}/{api-format}

import requests

url = "https://munch.emuseum.com/objects/4714/json?key={key}"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))



# GET /search/{keyword}/{module}/{api-format}

import requests

url = "https://munch.emuseum.com/search/skrik/objects/json?key={key}"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))



# GET /advancedsearch/{module}/{field}:{field-value}/{api-format}

import requests

url = "https://munch.emuseum.com/advancedsearch/objects/title:skrik/json?key={key}"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))



# GET /{module}/{api-format}?filter

import requests

url = "https://munch.emuseum.com/objects/json?filter=thesfilter:1545220&key={key}"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))



# GET /{search}/{keyword}/{module}/{api-format}?filter

import requests

url = "https://munch.emuseum.com/search/skrik/objects/json?filter=department:Munch-samlingen&key={key}"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))



# GET /{module}/{api-format}?page

import requests

url = "http://munch.emuseum.com/objects/json?page=2&key={key}"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))



# GET /{module}/{api-format}?sort

import requests

url = "https://munch.emuseum.com/objects/json?sort=displayDate-asc&key={key}"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))



# GET /search/{keyword}/{module}/{api-format}?sort

import requests

url = "https://munch.emuseum.com/search/skrik/objects/json?sort=invno-asc&key={key}"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))



# GET /advancedsearch/{module}/{field}:{field-value}/{api-format}?sort

import requests

url = "https://munch.emuseum.com/advancedsearch/objects/title:skrik/json?sort=displayDate-asc&key={key}"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
