import json
import requests
import pandas as pd
import requests
import io

# Define URL  
#url = input("Enter the URL you'd like to test: ")
url = "https://www.marketreach.co.uk/"

# API request url
r = requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}/&strategy=mobile'\
                                 .format(url))
#print(r.text)



# Convert to json format
r_json = json.loads(r.text)

print(r_json)

with open('result.json', 'w') as outfile:
  json.dump(r_json, outfile)

