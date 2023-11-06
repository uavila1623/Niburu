import pandas as pd
import numpy as np
# importing plot libraries
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
# Training models import statements
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

#Importing pickle to save model:
import pickle

#retrieving the data
data = pd.read_csv('WeatherEvents_Jan2016-Dec2021.csv')
df = pd.DataFrame(data)

#Prepping the Data
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

#Prepping the training data:
# Code cell for Country Weather type occurence prediction:
def couOcur(type):
    i = 2016
    totalOcu = []
    while i <= 2021:
        group0 = newdf.groupby(['Year','Type'])
        group1 = group0.get_group((i,type))
        total = len(group1)
        totalOcu.append(total)
        i+=1
    return totalOcu
trainList2 = couOcur('Rain')
trainList2df = pd.DataFrame(trainList2, columns=['Year 2016-21'])
x1 = trainList2df.values
y1 = [100000,200045,567789,123456,546678,321123]
xtrain1, xtest1, ytrain1, ytest1 = train_test_split(x1,y1, test_size=0.2, random_state=42)
# RandomForestRegressor model
testList2 = [76672]
model = RandomForestRegressor()
model.fit(xtrain1, ytrain1)
pickle.dump(model, open('model2.pkl', 'wb'))
features = np.array(testList2)
pickle_model = pickle.load(open('model2.pkl', 'rb'))
prediction = int(pickle_model.predict(features.reshape(-1,1)))
print(prediction)
print('Script complete')