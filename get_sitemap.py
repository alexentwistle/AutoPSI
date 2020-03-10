import json
import requests
import pandas as pd
from pandas import read_csv 
import io
from bs4 import BeautifulSoup

# Define Sitemap URL
url = "https://www.marketreach.co.uk/sitemap.xml"
page = requests.get(url)
print('Loaded page with: %s' % page)

sitemap_index = BeautifulSoup(page.content, 'html.parser')
print('Created %s object' % type(sitemap_index))

urls = [element.text for element in sitemap_index.findAll('loc')]
print(urls)

# Write sitemap URLs to CSV
with open('marketreach_without_header.csv', 'w') as f:
    for url in urls:
        f.write(url + '\n')

     
# Add column header 'URL' to CSV and re-save
df = read_csv('marketreach_without_header.csv')
df.columns = ['url']
df.to_csv('marketreach_urls.csv')

# TODO: Delete old (headerless) CSV

column_header='url'

response_object = {}

# Iterate through the df
for i in range(0, len(df)):

        #print('Requesting row #:', i)

        # Define request parameter
        url = df.iloc[i][column_header]

        # TODO: FIX THIS USING REQUESTS LIBRARY
        # Make request
        pagespeed_results = urllib.request.urlopen('https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={}&strategy=mobile'\
            .format(url)).read().decode('UTF-8')

        # Convert to json format
        pagespeed_results_json = json.loads(pagespeed_results)

        # Insert returned json response into response_object
        response_object[url] = pagespeed_results_json
        time.sleep(20)
        
        print(response_object[url])

        #Optional download of json files, comment out to skip this step 
        #with open('pagespeed_results_json', 'w') as outfile:
            #json.dump(response_object[url], outfile)
        
        #files.download('pagespeed_results_json')


# TODO: Create dataframe to store responses
# Create dataframe to store field data responses
df_pagespeed_results = pd.DataFrame(
columns=['url',
         'FCP_category',
         'FCP_percentile',
         'FID_category',
         'FID_percentile',
         'Time_to_Interactive',
         'Speed_Index',
         'First_CPU_Idle',
         'First_Meaningful_Paint',
         'TTFB',
         'Total_Blocking_Time'])  

print(df_pagespeed_results)





# Iterate through the response object to pull out desired metrics
