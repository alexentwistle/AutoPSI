import json
import requests
import pandas as pd
import urllib
import time
from google.colab import files
import io


# Define URL  
#url = input("Enter the URL you'd like to test: ")
url = "https://www.marketreach.co.uk/"

# API request url
r = requests.get('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}/&strategy=mobile'\
                                 .format(url))
print(r.text)