import pandas as pd
 
df = pd.read_csv('https://data.cityofnewyork.us/api/views/rsgh-akpg/rows.csv?accessType=DOWNLOAD')

#returns counts for all columns grouped by Borough
df.groupby('Borough').count() 

#line below returns total count for a specified column
#df.groupby('Borough')['Species'].count()
