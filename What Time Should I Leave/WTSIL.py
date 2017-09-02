#!/usr/bin/env python
import urllib.request
import json
from twilio.rest import TwilioRestClient
from math import modf
import config
from datetime import datetime
import calendar

# variables that allow for text to be sent. account_sid, auth_token from twilio.
client = TwilioRestClient(config.account_sid, config.auth_token)

# parameters for urlMaps. keyMaps from google API.
mode = "&mode=transit"

# calculates time
d = datetime.utcnow()
actual_arrival_time = calendar.timegm(d.utctimetuple())
arrival_time = "&arrival_time=" + str(actual_arrival_time)
transit_mode = "&transit_mode=subway"

# urls used for text
urlWeather = "http://api.openweathermap.org/data/2.5/weather?q="+config.city+"&appid="+config.keyWeather
urlMaps = "https://maps.googleapis.com/maps/api/distancematrix/json?"+config.origins+config.destinations+mode+arrival_time+transit_mode+"&key="+config.keyMaps


# functions to convert minutes to hours
def convert_hours(time):
    hour, minute = time.split('hour')
    return int(hour) + (int(minute) / 60)
    
# reads the information received from openweathermap.org
with urllib.request.urlopen (urlWeather) as url:
    responseWeather = url.read()

# reads the information received from google maps
with urllib.request.urlopen(urlMaps) as url:
    responseMaps = url.read()
   
# parses data to only receive weather and description
parsedDataWeather = json.loads(responseWeather.decode())
desc = parsedDataWeather['weather'][0]['description']
temp = parsedDataWeather['main']['temp']

# parses data to only receive travel time
parsedDataMaps = json.loads(responseMaps.decode())
travelTime = parsedDataMaps['rows'][0]['elements'][0]['duration']['text']
departureTime = parsedDataMaps['rows'][0]['elements'][0]['duration']['text']

# converts the travel time to time to leave
departureTime = departureTime[:-5]  # gets rid of 'mins'
leaveAt = 10 - convert_hours(departureTime)  # 10 AM is always the time I have to arrive, so I just leave it at 10
secondHalf, firstHalf = modf(leaveAt)  # splits the number before/after the decimal
secondHalf = (secondHalf * 60) / 100  # converts to a XX:XX format for time
leaveAt = '%.2f' % round(secondHalf + firstHalf, 2)  # rounds to 2 decimals
leaveAt = leaveAt.replace('.', ':')  # replaces . with :

# sends text message
msg = "The weather in " + str(config.city) + " is " + str(int(temp)-273) + " with " + str(desc) + \
      ". You should leave at " + str(leaveAt) + " and it will take "+str(travelTime)+" to get school."
message = client.messages.create(to=config.phone1, from_=config.phone2, body=msg)
