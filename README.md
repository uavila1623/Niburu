# Niburu

<p align="center">
Machine Learning weather prediction web app.

**Note**: The application is slightly sluggish, this is mostly due to the application using 3 data sets. I have optimized the application by cutting the processing time by 70% but it is still quite noticiable. Please feel free to share any suggestions to improve the application. ^•ﻌ•^ฅ

<p align="center">
<img src="./assets/Image 11-3-23 at 5.50 PM.jpg"/>
 </p>
</p>

## Features

- **The ML libraries**: This web app uses numpy, pandas, and scikit-learn libraries. For the learning models I used RandomForestRegressor and train_test_split from scikit-learn.

- **Predictions**: You have the ability to base the prediction on the country as whole or on a specific region.

- **Charts & Searching**: Capable of producing a few types of charts to better understand and visualize the data that is being used. It also has the ability to search through the data and find valid prediction entries.

- **Data Used**: The data being used is from a dataset of different weather events that occurred in the United states from 2016-2022 that I obtained from here: https://www.kaggle.com/datasets/sobhanmoosavi/us-weather-events. The data has been modified to better fit the model and removed uneccessary entries like null values or data that was not used.

## Usage

1. clone repo
2. download any dependencies
3. You might need to create a conda environment.
4. Once you created the environment type python3 app.py(Mac) python app.py. And enjoy the web app.
