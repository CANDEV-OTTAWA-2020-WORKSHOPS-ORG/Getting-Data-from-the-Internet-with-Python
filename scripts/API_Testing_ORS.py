import requests
import sys
import json
sys.path.append('F:\Scripts\Credentials')
#import python file that contains personal API keys and proxy information:
import credentials #comment out if you run
#example 1: geocoding with ORS

#first, let's look up the University of Ottawa
params1={'api_key':credentials.ors, #replace with your own API key
        
        'text':'75 Laurier Ave E, Ottawa, Canada'
        }

coords=requests.get("https://api.openrouteservice.org/geocode/search?",
                    params=params1, proxies=credentials.proxy) #remove proxies parameter

#check that the request worked, want a status code in 200s
print(coords.status_code, coords.reason)
#it returns a json - we can take a look at what it contains

geo=coords.json()
print(json.dumps(geo, indent=2))
#
print(geo['features'][0]['geometry']['coordinates'])

lon1,lat1=geo['features'][0]['geometry']['coordinates']

#as another example, Shawarma Palace:
     
params2={'api_key':credentials.ors,
        
        'text':'464 Rideau St, Ottawa, Canada'
        }

coords=requests.get("https://api.openrouteservice.org/geocode/search?", 
                    params=params2, proxies=credentials.proxy)

print(coords.status_code, coords.reason)

geo=coords.json()
print(geo['features'][0]['geometry']['coordinates'])
lon2,lat2=geo['features'][0]['geometry']['coordinates']

#Now that we have two pairs of coordinates, we can also use OpenRouteService 
#to compute the network distance from OttawaU to Shawarma Palace

params3={'api_key':credentials.ors,
         'start':"{},{}".format(lon1,lat1),
         'end':"{},{}".format(lon2,lat2)}


call = requests.get('https://api.openrouteservice.org/v2/directions/foot-walking',
                    params=params3,proxies=credentials.proxy)

print(call.status_code, call.reason)
response=call.json()
#print(json.dumps(response, indent=2))
print(call.text)
print(response['features'][0]['properties']['summary'])