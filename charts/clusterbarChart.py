import pandas as pd
import json
#Plotting graph libraries
from plotly.subplots import make_subplots
import plotly.graph_objects as go
#Importing the machine learning models:
from sklearn.cluster import KMeans
# weatherData = 'models/WeatherEvents_Jan2016-Dec2021.csv'
data = pd.read_csv('WeatherEvents_Jan2016-Dec2021.csv')
df = pd.DataFrame(data)
newdf = df.drop('AirportCode',axis='columns')
newdf.rename(columns={'EventId':'Year'},inplace=True)
datetimeFormat = '%Y-%m-%d %H:%M:%S'
newdf['StartTime(UTC)'] = pd.to_datetime(newdf['StartTime(UTC)'], format=datetimeFormat)
newdf['EndTime(UTC)'] = pd.to_datetime(newdf['EndTime(UTC)'], format=datetimeFormat)
newdf['Year'] = newdf['StartTime(UTC)'].dt.year
newdf['Duration'] = newdf['EndTime(UTC)'] - newdf['StartTime(UTC)']
#Formatting the Duration Data
newdf['Duration'] = newdf['Duration'].dt.total_seconds()
newdf['Duration'] = newdf['Duration']/(60*60)
newdf = newdf[(newdf['Duration']< 30*24) & (newdf['Duration'] != 0)]
newdf = newdf.dropna(axis=0)
newdf.groupby(['Year', 'Type', 'Severity', 'StartTime(UTC)', 'EndTime(UTC)',
       'Precipitation(in)', 'TimeZone', 'LocationLat', 'LocationLng', 'City',
       'County', 'State', 'ZipCode'],)

#Creating new dataframe with adjustments:
newdf2 = newdf.groupby(['ZipCode','City','State', 
                  'LocationLat', 'LocationLng','Type']).agg({'Duration':['sum']}).reset_index()
newdf2.columns=pd.MultiIndex.from_tuples((("ZipCode", " "),("City", " "),
                                       ("State", " "), ("LocationLat", " "),
                                       ("LocationLng", " "), ("Type", " "), ("Duration", " ")))
newdf2.columns = newdf2.columns.get_level_values(0)
newdf2['Duration'] = newdf2['Duration']/(24*4*3.65) #yearly percentage  
newdf2 = newdf2.sort_values(by='Duration')

#Prepping data:
newdf_flat = newdf2.pivot_table(index='ZipCode', columns='Type', values=['Duration']).reset_index().fillna(0)
newdf_flat.columns=pd.MultiIndex.from_tuples(((' ', 'ZipCode'),(' ', 'Cold'),(' ', 'Fog'),
            (' ',  'Hail'),(' ', 'Precipitation'),(' ', 'Rain'),(' ', 'Snow'),(' ', 'Storm')))
newdf_flat.columns = newdf_flat.columns.get_level_values(1)
uniqueKey = newdf2[['ZipCode', 'City', 
                 'State', 'LocationLat', 'LocationLng']].sort_values(by='ZipCode').drop_duplicates()
weatherinfo = pd.merge(newdf_flat, uniqueKey, how='inner', on='ZipCode')

#Prepping training data:
X = newdf_flat.drop(['ZipCode','Cold', 'Hail'], axis=1)

distortions = []
K = range(1,20)
for i in K:
    kmean = KMeans(n_clusters=i, random_state=0, n_init=50, max_iter=500)
    kmean.fit(X)
    distortions.append(kmean.inertia_)

# Creating the clusters for state wide distributions
kmeans = KMeans(n_clusters=4, random_state=0).fit(X)

newdf_flat['Cluster'] = (kmeans.labels_).astype(str)
newdf_cluster = pd.merge(newdf_flat[['ZipCode','Cluster']], weatherinfo.drop(['Cold','Hail'], axis=1), 
                      how='inner', on='ZipCode')

#creating the cluster Properties:
prop = newdf_cluster[['Cluster', 'Fog',
                   'Precipitation','Rain', 'Snow', 'Storm']].groupby(['Cluster']).mean().reset_index()
prop2 = prop.transpose().reset_index()
prop2 = prop2[(prop2['index'] !='Cluster')].sort_values(by=0)

# #Creating the bar chart for the properties:
fig_prop=make_subplots(rows=1, cols=4, shared_yaxes=True,horizontal_spacing=0)

fig_prop.add_trace(go.Bar(x=prop2['index'], y=prop2[0], name='Cluster 0'), row=1, col=1)
fig_prop.add_trace(go.Bar(x=prop2['index'], y=prop2[1], name='Cluster 1'), row=1, col=2)
fig_prop.add_trace(go.Bar(x=prop2['index'], y=prop2[2], name='Cluster 2'), row=1, col=3)
fig_prop.add_trace(go.Bar(x=prop2['index'], y=prop2[3], name='Cluster 3'), row=1, col=4)

fig_prop.update_yaxes(title_text="duration%/year", row=1, col=1)
fig_prop.update_layout(title_text="Weather distribution in each cluster")
fig_prop.update_layout(height=500, width=500)
fig_prop.write_image("images/fig3.png")
# prop2.to_csv('clusterD.csv', index=False)
print('Script Complete')