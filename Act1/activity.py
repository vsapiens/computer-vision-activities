import json
import requests
from bs4 import BeautifulSoup
from slimit import ast
from slimit import minify
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0'}
URL = 'https://www.worldometers.info/coronavirus/'

page = requests.get(URL, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
contents = soup.find_all('script',type="text/javascript")
i = 1

for content in contents:
    if(content.text):
      text = str(content.text)
      i += 1
      if "Daily Cases" not in text:
        continue
      table = minify(text, mangle=True, mangle_toplevel=True)
      table = table.split(':')
      values1 = table[8].replace("\"","").replace("]","").replace("[","").replace("{","").replace("}","").split(",")
      values2 = table[22].replace("\"","").replace("]","").replace("[","").replace("{","").replace("}","").split(",")
      values1 = values1[:-1]
      values2 = values2[:-1]

print(values1)
print(values2)