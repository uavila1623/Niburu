import pandas as pd
import json
#Plotting graph libraries
import plotly.express as px
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
weatherinfo.to_csv('tempdf.csv',index=False)
#Prepping training data:
X = newdf_flat.drop(['ZipCode','Cold', 'Hail'], axis=1)

distortions = []
K = range(1,20)
for i in K:
    kmean = KMeans(n_clusters=i, random_state=0, n_init=50, max_iter=500)
    kmean.fit(X)
    distortions.append(kmean.inertia_)

# Creating the clusters for city wide distributions
kmeans = KMeans(n_clusters=4, random_state=0).fit(X)

newdf_flat['Cluster'] = (kmeans.labels_).astype(str)
newdf_cluster = pd.merge(newdf_flat[['ZipCode','Cluster']], weatherinfo.drop(['Cold','Hail'], axis=1), 
                      how='inner', on='ZipCode')

# #Creating the Scatter Chart:
# fig_cluster = px.scatter_geo(newdf_cluster, lat='LocationLat', lon='LocationLng',
#                       hover_name=weatherinfo['City'] + ', ' + weatherinfo['State'],
#                       scope="usa",
#                       color_discrete_sequence =['#AB63FA', '#EF553B', '#00CC96','#636EFA'],
#                       color = 'Cluster',
#                       title ='City wide weather cluster distribution')
# fig_cluster.update_layout(height=400, width=400)
# fig_cluster.write_image("images/fig1.png")
newdf_cluster.to_csv('cityKd.csv', index=False)
print('Script Complete')