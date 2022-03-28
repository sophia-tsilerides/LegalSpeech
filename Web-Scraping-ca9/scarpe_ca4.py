from bs4 import BeautifulSoup
import requests
import re
import numpy as np
import pandas as pd

resp = requests.get('https://www.ca4.uscourts.gov/oral-argument/listen-to-oral-arguments')
soup = BeautifulSoup(resp.text,'html.parser')

tables = soup.findAll("table")
table = tables[0]

data = []
rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values
        
final_df = pd.DataFrame(data)
final_df.columns = ['ArgumentDate', 'CaseNumber', 'CaseName', 'Panel', 'Counsel']
