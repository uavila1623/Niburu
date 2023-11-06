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
#This is code cell is used to create a chart of the occurences of a certain weather event
def getOccur(type,state):
    totalOcur = []
    i = 2016
    while i <= 2021:
        group1 = newdf.groupby(['Year','Type','State'])
        group2 = group1.get_group((i,type,state))
        total = len(group2)
        totalOcur.append(total)
        i+=1
    return totalOcur
yearIndex = ['2016','2017','2018','2019','2020','2021']
serData = getOccur('Rain','CA')
charser = pd.Series(data=serData,index=yearIndex)
plt.plot(charser.index, charser.values)
plt.xlabel('Year')
plt.ylabel('Occurences of Weather Event')
plt.title('Weather Chart')
plt.legend(['Rain'], loc='upper left')
plt.savefig('images/firstpic3.png')
print('Script Complete')

