# Prep data for script
import pandas as pd
import json
#Plotting graph libraries
import matplotlib.pyplot as plt 

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

#Code snippet to get preciptation:
def getPrecip():
    preData = []
    groupedbyYear = newdf.groupby('Year')
    for i in range(2016, 2022):
        curYear = groupedbyYear.get_group(i)
        totalPre = curYear['Precipitation(in)'].sum()
        preData.append(totalPre)
    return preData
yearList = getPrecip()
yearIndex = ['2016','2017','2018','2019','2020','2021']
preSer = pd.Series(data=yearList, index=yearIndex)
plt.plot(preSer.index, preSer.values,'o')
#Setting up Labels
plt.xlabel('Year')
plt.ylabel('Precipitation(inches)')
plt.title("Precipitation Chart")
plt.legend(['Preciptation'], loc='upper right')
plt.savefig('images/firstpic4.png')
print('Script Complete')
