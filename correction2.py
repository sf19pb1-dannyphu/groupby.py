"""
Print number of dog bites in each borough.
https://data.cityofnewyork.us/Health/DOHMH-Dog-Bite-Data/rsgh-akpg
"""

import sys
import pandas as pd

url = "https://data.cityofnewyork.us/api/views/rsgh-akpg/rows.csv"

try:
    df = pd.read_csv(url)   #df is a pandas DataFrame.
except BaseException as error:
    print(error, file = sys.stderr)
    sys.exit(1)
    
series = df["Borough"].value_counts().sort_index()   #alphabetical order
print(series)
sys.exit(0)
