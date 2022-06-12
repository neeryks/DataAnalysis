import plotly.express as px
import pandas as pd
import json


india_map = json.load(open('states_india.geojson','r'))
df = pd.read_excel("data.xlsx")
df_s = pd.DataFrame({'Stats':df['Unnamed: 8'][3:38]},)
#print(df_s)
df = pd.concat([df['Unnamed: 1'][3:38],df_s],axis=1,ignore_index=True)
df.reset_index(drop=True,inplace=True)
df = df.rename(columns={df.columns[0]:"State",df.columns[1]:"StateWise Population (Crore)"})
#print(df)
state_id_json = []
state_name_json = []

for st in india_map['features']:
    state_name_json.append(st['properties']['st_nm'])
    #state_id_json.append(st['_id'])

#state_name_json = list(map(lambda x:x.upper(),state_name_json))
#df['State'] = list(map(lambda x:x.upper(),df['State']))
state_id = pd.DataFrame({"State":state_name_json}).sort_values(by=['State'])
#print(state_id,df)
df = pd.merge(df,state_id,on='State')
df = df.append({"State":"Telangana","StateWise Population (Crore)":35003},ignore_index=True)
df['StateWise Population (Crore)'] = list(map(lambda x:x/10000 ,df['StateWise Population (Crore)']))
print(df)

fig = px.choropleth(df,geojson=india_map,locations='State',color='StateWise Population (Crore)',featureidkey="properties.st_nm",scope='asia')
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(
    height=800,
    title_text='StateWise Population Distribution INDIA')
fig.show()

#print(df)

