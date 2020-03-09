import json
import requests
import pandas as pd
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
with open('marketreach_urls.csv', 'w') as f:
    for url in urls:
        f.write(url + '\n')