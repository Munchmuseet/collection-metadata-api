# GET /{module}/{api-format}

import http.client
import mimetypes
conn = http.client.HTTPSConnection("munch.emuseum.com")
payload = ''
headers = {}
conn.request("GET", "/objects/json?key={key}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


# GET /{module}/{id}/{api-format}

import http.client
import mimetypes
conn = http.client.HTTPSConnection("munch.emuseum.com")
payload = ''
headers = {}
conn.request("GET", "/objects/4714/json?key={key}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


# GET /search/{keyword}/{module}/{api-format}

import http.client
import mimetypes
conn = http.client.HTTPSConnection("munch.emuseum.com")
payload = ''
headers = {}
conn.request("GET", "/search/skrik/objects/json?key={key}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


# GET /advancedsearch/{module}/{field}:{field-value}/{api-format}

import http.client
import mimetypes
conn = http.client.HTTPSConnection("munch.emuseum.com")
payload = ''
headers = {}
conn.request("GET", "/advancedsearch/objects/title:skrik/json?key={key}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


# GET /{module}/{api-format}?filter

import http.client
import mimetypes
conn = http.client.HTTPSConnection("munch.emuseum.com")
payload = ''
headers = {}
conn.request("GET", "/objects/json?filter=thesfilter:1545220&key={key}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


# GET /{search}/{keyword}/{module}/{api-format}?filter

import http.client
import mimetypes
conn = http.client.HTTPSConnection("munch.emuseum.com")
payload = ''
headers = {}
conn.request("GET", "/search/skrik/objects/json?filter=department:Munch-samlingen&key={key}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


# GET /{module}/{api-format}?page

import http.client
import mimetypes
conn = http.client.HTTPSConnection("munch.emuseum.com")
payload = ''
headers = {}
conn.request("GET", "/objects/json?page=2&key={key}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


# GET /{module}/{api-format}?sort

import http.client
import mimetypes
conn = http.client.HTTPSConnection("munch.emuseum.com")
payload = ''
headers = {}
conn.request("GET", "/objects/json?sort=displayDate-asc&key={key}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


# GET /search/{keyword}/{module}/{api-format}?sort

import http.client
import mimetypes
conn = http.client.HTTPSConnection("munch.emuseum.com")
payload = ''
headers = {}
conn.request("GET", "/search/skrik/objects/json?sort=invno-asc&key={key}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


# GET /advancedsearch/{module}/{field}:{field-value}/{api-format}?sort

import http.client
import mimetypes
conn = http.client.HTTPSConnection("munch.emuseum.com")
payload = ''
headers = {}
conn.request("GET", "/advancedsearch/objects/title:skrik/json?sort=displayDate-asc&key={key}", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
