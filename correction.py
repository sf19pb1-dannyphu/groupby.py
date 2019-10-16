"""
groupby.py

counts the number of cells within each column that is not blank
"""

import pandas as pd
 
df = pd.read_csv('https://data.cityofnewyork.us/api/views/rsgh-akpg/rows.csv?accessType=DOWNLOAD')

#line 1
series = df.groupby('Borough').count()

#line 2
series2 = df.groupby('Borough')['Species'].count()

print("Line 1 result, all columns in csv:")
print(series)
print()
print("Line 2 result, only counting "Species" column:")
print(series2)
