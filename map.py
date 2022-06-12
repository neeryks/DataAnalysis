import plotly.express as px
import pandas as pd
import json


india_map = json.load(open('india_statenew.geojson','r'))
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
    state_name_json.append(st['properties']['ST_NM'])
    #state_id_json.append(st['_id'])

#state_name_json = list(map(lambda x:x.upper(),state_name_json))
#df['State'] = list(map(lambda x:x.upper(),df['State']))
state_id = pd.DataFrame({"State":state_name_json}).sort_values(by=['State'])
#print(state_id,df)
df = pd.merge(df,state_id,on='State')
df = pd.concat([df,pd.DataFrame({"State":["Telangana","Ladakh"],"StateWise Population (Crore)":[35003,274]})],ignore_index=True)
df['StateWise Population (Crore)'] = list(map(lambda x:x/10000 ,df['StateWise Population (Crore)']))
print(df)

fig = px.choropleth(df,geojson=india_map,locations='State',color='StateWise Population (Crore)',featureidkey="properties.ST_NM",template="seaborn")
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(
    height=800,
    title_text='StateWise Population Distribution INDIA')
fig.update_traces(marker_line_width=1, marker_opacity=1,marker_line_color = "white")
fig.show()

#print(df)

