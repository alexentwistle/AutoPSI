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