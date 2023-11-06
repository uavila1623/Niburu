import pandas as pd
import numpy as np
from random import *
# Training models import statements
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

#Importing pickle to save model:
import pickle
#retrieving the data
data = pd.read_csv('WeatherEvents_Jan2016-Dec2021.csv')
df = pd.DataFrame(data)

#Prepping the Data
newdf = df
newdf.rename(columns={'EventId':'Year'},inplace=True)
datetimeFormat = '%Y-%m-%d %H:%M:%S'
newdf['StartTime(UTC)'] = pd.to_datetime(newdf['StartTime(UTC)'], format=datetimeFormat)
newdf['EndTime(UTC)'] = pd.to_datetime(newdf['EndTime(UTC)'], format=datetimeFormat)
newdf['Year'] = newdf['StartTime(UTC)'].dt.year
newdf = df.drop(['AirportCode','Severity','StartTime(UTC)','EndTime(UTC)','TimeZone','LocationLat','LocationLng','ZipCode'],axis=1)
newdf = newdf.dropna(axis=0)
newdf.groupby(['Year', 'Type', 'City', 'County','State'])
newdf.to_csv('my_dataframe.csv',index=False)
#Prepping the training data:
def getOccur(type,city,county,state):
    totalOcur = []
    i = 2016
    while i <= 2021:
        group1 = newdf.groupby(['Year','Type','City','County','State'])
        group2 = group1.get_group((i,type,city,county,state))
        total = len(group2)
        totalOcur.append(total)
        i+=1
    return totalOcur
trainList1 = getOccur('Rain','Lander','Fremont','WY')
traindf = pd.DataFrame(trainList1, columns=['Year 2016-21'])
x = traindf.values
y = [123,456,231,333,111,667]
xtrain, xtest, ytrain, ytest = train_test_split(x,y, test_size=0.2, random_state=42)
ranNum = randint(1,260)
testList1 = [ranNum]
model = RandomForestRegressor()
model.fit(xtrain, ytrain)
features = np.array(testList1)
print('Script complete')