import requests
import sys

sys.path.append('F:\Scripts\Credentials')
#import python file that contains personal API keys and proxy information:
import credentials 

f=requests.get('https://www.octranspo.com/files/google_transit.zip',proxies=credentials.proxy)
g=open('GTFS.zip','wb') 
g.write(f.content)
g.close()


