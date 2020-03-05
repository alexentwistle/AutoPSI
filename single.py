import json
import requests
import pandas as pd
import requests
import io

# Define URL  
url = input("Enter the URL you'd like to test: ")

# API request url
r = requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}/&strategy=mobile'\
                                 .format(url))
print(r.text)