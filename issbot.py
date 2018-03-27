import json
import turtle
import urllib.request

print()

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print('People in Space: ', result['number'])
print()

people = result['people']
for p in people:
	print(p['name'] + ' in ' + p['craft'])	

print()

url = 'http://api.open-notify.org/iss-now.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

location = result['iss_position']
lat = location['latitude']
lon = location['longitude']
print('Latitude: ', lat)
print('Longiude: ', lon)

print()

screen = turtle.Screen()
screen.bgpic('map.jpg')


