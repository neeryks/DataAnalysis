import plotly.express as px
import pandas as pd
import json


india_map = json.load(open('INDIA_STATES.json','r'))
df = pd.read_excel("data.xlsx")
df_s = pd.DataFrame({'Stats':df['Unnamed: 7'][3:38]})
#print(df_s)
df = pd.concat([df['Unnamed: 1'][3:38],df_s],axis=1,ignore_index=True)
#print(df)

"""
for state in india_map['features']:
    for state_name in df[0]:

    if state['properties']['STATE'] == df[0].upper
"""
print(df[0])