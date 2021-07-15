import pandas as pd
import requests
import json

soc_codes = [2136, 2231, 3542, 3543, 3544, 3545, 3562, 4159, 4216, 5434, 6121, 6145, 7111, 7129, 7219, 9272, 9273, 9274]

regions = {1: "London", 3: "East of England", 2: "South East (England)", 4: "South West (England)", 10: "Wales", 7: "Yorkshire and the Humber", 11: "Scotland", 6: "East Midlands (England)", 9: "North East (England)", 8: "North West (England)", 12: "Northern Ireland", 5: "West Midlands (England)"}
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


overall4 = []
for soc in soc_codes:
  for number in numbers:
    r = requests.get(f"http://api.lmiforall.org.uk/api/v1/ess/region/{number}/{soc}?year=2019&coarse=false")
    response = r.json()
    if len(response) != 1:
      temp = []
      temp.append(soc)
      temp.append(regions[number])
      temp.append(round(response["percentSSV"]))
      temp.append(round(response["percentHTF"]))
      temp.append(response["reliability"])
      overall4.append(temp)

df4 = pd.DataFrame(overall4, columns = ['soc', 'region', 'skill shortage vacancies', 'hard to find vacancies', 'reliability'])
