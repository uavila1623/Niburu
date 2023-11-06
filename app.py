from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import csv
from random import *
# importing training libraries for prediction
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.cluster import KMeans
# libraries for charts
import matplotlib.pyplot as plt
import io
import base64
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
# open the data:
data = pd.read_csv('my_dataframe.csv')
data2 = pd.read_csv('stateKd.csv')
data3 = pd.read_csv('cityKd.csv')
data4 = pd.read_csv('clusterD.csv')
maindf = pd.DataFrame(data)
secdf = pd.DataFrame(data2)
thirdf = pd.DataFrame(data3)
fourdf = pd.DataFrame(data4)
# helper Methods


def getOccur(type, city, county, state):
    totalOcur = []
    i = 2016
    while i <= 2021:
        group1 = maindf.groupby(['Year', 'Type', 'City', 'County', 'State'])
        group2 = group1.get_group((i, type, city, county, state))
        total = len(group2)
        totalOcur.append(total)
        i += 1
    return totalOcur


def couOcur(type):
    i = 2016
    totalOcu = []
    while i <= 2021:
        group0 = maindf.groupby(['Year', 'Type'])
        group1 = group0.get_group((i, type))
        total = len(group1)
        totalOcu.append(total)
        i += 1
    return totalOcu


def stateOcur(type, state):
    totalOcur = []
    i = 2016
    while i <= 2021:
        group1 = maindf.groupby(['Year', 'Type', 'State'])
        group2 = group1.get_group((i, type, state))
        total = len(group2)
        totalOcur.append(total)
        i += 1
    return totalOcur


def getPrecip():
    precData = []
    groupedbyYear = maindf.groupby('Year')
    for i in range(2016, 2022):
        curYear = groupedbyYear.get_group(i)
        totalPre = curYear['Precipitation(in)'].sum()
        precData.append(totalPre)
    return precData


def natOcur(type):
    totalOcur = []
    i = 2016
    while i <= 2021:
        group1 = maindf.groupby(['Year', 'Type'])
        group2 = group1.get_group((i, type))
        total = len(group2)
        totalOcur.append(total)
        i += 1
    return totalOcur


# Create the flask app
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/charts')
def charts():
    return render_template('charts.html')


@app.route('/kcharts')
def kcharts():
    return render_template('kcharts.html')


@app.route('/data')
def data():
    return render_template('data.html')


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        try:
            state = request.form.get("state")
            type = request.form.get("type")
            county = request.form.get("county")
            city = request.form.get("city")
            pred1 = request.form['pred1']
            pred2 = request.form['pred2']
            pred3 = request.form['pred3']
            pred4 = request.form['pred4']
            pred5 = request.form['pred5']
            pred6 = request.form['pred6']
            tempLis = [pred1, pred2, pred3, pred4, pred5, pred6]
            predList = list(map(int, tempLis))
            trainList = getOccur(type, city, county, state)
            traindf = pd.DataFrame(trainList, columns=['Year 2016-21'])
            x = traindf.values
            y = predList
            xtrain, xtest, ytrain, ytest = train_test_split(
                x, y, test_size=0.2, random_state=42)
            ranNum = randint(1, 260)
            testList1 = [ranNum]
            model = RandomForestRegressor()
            model.fit(xtrain, ytrain)
            features = np.array(testList1)
            prediction = int(model.predict(features.reshape(-1, 1)))
            return render_template("index.html", output=prediction, error=None)
        except Exception as e:
            app.logger.error(e, exc_info=True)
            return render_template("index.html", error="An error occurred while processing your request. Please enter the request again or report the issue.")
    else:
        return render_template('index.html')


@app.route('/counPredict', methods=['GET', 'POST'])
def counPredict():
    if request.method == "POST":
        try:
            type1 = request.form.get("counType")
            counpred1 = request.form['counpred1']
            counpred2 = request.form['counpred2']
            counpred3 = request.form['counpred3']
            counpred4 = request.form['counpred4']
            counpred5 = request.form['counpred5']
            counpred6 = request.form['counpred6']
            tempLis2 = [counpred1, counpred2, counpred3,
                        counpred4, counpred5, counpred6]
            predList2 = list(map(int, tempLis2))
            trainList2 = couOcur(type1)
            traindf2 = pd.DataFrame(trainList2, columns=['Year 2016-21'])
            x1 = traindf2.values
            y1 = predList2
            xtrain, xtest, ytrain, ytest = train_test_split(
                x1, y1, test_size=0.2, random_state=42)
            ranNum1 = randint(1, 260)
            testList2 = [ranNum1]
            model = RandomForestRegressor()
            model.fit(xtrain, ytrain)
            features = np.array(testList2)
            prediction1 = int(model.predict(features.reshape(-1, 1)))
            return render_template("index.html", output2=prediction1, error2=None)
        except Exception as e:
            app.logger.error(e, exc_info=True)
            return render_template("index.html", error2="An error occurred while processing your request. Please try entering the request again or report the issue.")
    else:
        return render_template("index.html")


@app.route('/precChart', methods=['POST'])
def precChart():
    if request.method == "POST":
        try:
            chartType = request.form['chart-type']
            precList = getPrecip()
            yearIndex = ['2016', '2017', '2018', '2019', '2020', '2021']
            preSer = pd.Series(data=precList, index=yearIndex)
            plt.switch_backend('agg')
            # Generate chart type
            if chartType == 'line':
                plt.plot(preSer.index, preSer.values)
            if chartType == 'scatter':
                plt.scatter(preSer.index, preSer.values)
            if chartType == 'bar':
                plt.bar(preSer.index, preSer.values)
            # Create the chart:
            plt.xlabel('Year')
            plt.ylabel('Precipitation(inches)', labelpad=-0.4)
            plt.title("Precipitation Chart")
            plt.legend(['Preciptation'], loc='upper right')
            # Save the Chart:
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            # Encode the buffer in base64
            chart_data = base64.b64encode(buffer.read()).decode()
            return render_template('charts.html', chartType=chartType, chart_data=chart_data, error=None)
        except Exception as e:
            app.logger.error(e, exc_info=True)
            return render_template('charts.html', error='An error occurred while processing the request. Try making the request again or report the issue.')
    else:
        return render_template('charts.html')


@app.route('/specChart', methods=['POST'])
def specChart():
    if request.method == "POST":
        try:
            state = request.form["state"]
            type = request.form["type"]
            county = request.form["county"]
            city = request.form["city"]
            chartType = request.form['chart-type2']
            specData = getOccur(type, city, county, state)
            yearIndex = ['2016', '2017', '2018', '2019', '2020', '2021']
            natSer = pd.Series(data=specData, index=yearIndex)
            plt.switch_backend('agg')
            if chartType == 'line':
                plt.plot(natSer.index, natSer.values)
            if chartType == 'scatter':
                plt.scatter(natSer.index, natSer.values)
            if chartType == 'bar':
                plt.bar(natSer.index, natSer.values)
            # Create a Chart
            plt.xlabel('Year')
            plt.ylabel('Occurences of Weather Event')
            plt.title('Weather Chart')
            plt.legend([type], loc='upper left')
            # Save the chart
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            # Encode the buffer in base64
            spec_data = base64.b64encode(buffer.read()).decode()
            return render_template('charts.html', chartType=chartType, spec_data=spec_data, error2=None)
        except Exception as e:
            app.logger.error(e, exc_info=True)
            return render_template('charts.html', error2='An error occurred while processing the request. Try making the request again or report the issue.')
    else:
        return render_template('charts.html')


@app.route('/stateChart', methods=['POST'])
def stateChart():
    if request.method == "POST":
        try:
            state = request.form["state2"]
            type = request.form["type2"]
            chartType = request.form["chart-type3"]
            staData = stateOcur(type, state)
            yearIndex = ['2016', '2017', '2018', '2019', '2020', '2021']
            natSer = pd.Series(data=staData, index=yearIndex)
            plt.switch_backend('agg')
            if chartType == 'line':
                plt.plot(natSer.index, natSer.values)
            if chartType == 'scatter':
                plt.scatter(natSer.index, natSer.values)
            if chartType == 'bar':
                plt.bar(natSer.index, natSer.values)
            # Create a Chart
            plt.xlabel('Year')
            plt.ylabel('Occurences of Weather Event')
            plt.title('Weather Chart')
            plt.legend([type], loc='upper left')
            # Save the chart
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            # Encode the buffer in base64
            sta_data = base64.b64encode(buffer.read()).decode()
            return render_template('charts.html', chartType=chartType, sta_data=sta_data, error3=None)
        except Exception as e:
            app.logger.error(e, exc_info=True)
            return render_template('charts.html', error3='An error occurred while processing the request. Try making the request again or report the issue.')
    else:
        return render_template('charts.html')


@app.route('/nationChart', methods=['POST'])
def nationChart():
    if request.method == "POST":
        try:
            type = request.form['type3']
            chartType = request.form['chart-type4']
            natData = natOcur(type)
            yearIndex = ['2016', '2017', '2018', '2019', '2020', '2021']
            natSer = pd.Series(data=natData, index=yearIndex)
            plt.switch_backend('agg')
            if chartType == 'line':
                plt.plot(natSer.index, natSer.values)
            if chartType == 'scatter':
                plt.scatter(natSer.index, natSer.values)
            if chartType == 'bar':
                plt.bar(natSer.index, natSer.values)
            # Create chart:
            plt.xlabel('Year')
            plt.ylabel('Occurences of Weather Event')
            plt.title('Weather Chart')
            plt.legend([type], loc='upper left')
            # Save the chart:
            buffer = io.BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            # Encode the buffer in base64
            nat_data = base64.b64encode(buffer.read()).decode()
            return render_template('charts.html', chartType=chartType, nat_data=nat_data, error4=None)
        except Exception as e:
            app.logger.error(e, exc_info=True)
            return render_template('charts.html', error4='An error occurred while processing the request. Try making the request again or report the issue.')
    else:
        return render_template('charts.html')


@app.route('/cityKGraph', methods=['GET', 'POST'])
def cityKGraph():
    if request.method == 'POST':
        try:
            # Creating the scatter plot:
            fig_cluster = px.scatter_geo(thirdf, lat='LocationLat', lon='LocationLng',
                                         hover_name=thirdf['City'] +
                                         ', ' + thirdf['State'],
                                         scope="usa",
                                         color_discrete_sequence=[
                                             '#AB63FA', '#EF553B', '#00CC96', '#636EFA'],
                                         color='Cluster',
                                         title='City wide weather cluster distribution')
            fig_cluster.update_layout(height=460, width=600)
            # Create the graph HTML and return it:
            city_html = fig_cluster.to_html(full_html=False)
            return render_template('kcharts.html', city_html=city_html, error=None)
        except Exception as e:
            app.logger.error(e, exc_info=True)
            return render_template('kcharts.html', error='An error occurred while processing the request. Try making the request again or report the issue.')
    else:
        return render_template('kcharts.html')


@app.route('/stateKGraph', methods=['GET', 'POST'])
def stateKGraph():
    if request.method == 'POST':
        try:
            # Creating the scatter plot:
            fig_clusterS = px.scatter_geo(secdf, lat='LocationLat', lon='LocationLng',
                                          color='Cluster',
                                          size='Count',
                                          color_discrete_sequence=[
                                              '#636EFA', '#AB63FA', '#EF553B', '#00CC96'],
                                          hover_name='State',
                                          scope="usa",
                                          title='State wide weather cluster distribution')
            fig_clusterS.update_layout(height=460, width=600)
            # Create the graph HTML and return it:
            state_html = fig_clusterS.to_html(full_html=False)
            return render_template('kcharts.html', state_html=state_html, error2=None)
        except Exception as e:
            app.logger.error(e, exc_info=True)
            return render_template('kcharts.html', error2='An error occurred while processing the request. Try making the request again or report the issue.')
    else:
        return render_template('kcharts.html')


@app.route('/barChart', methods=['GET', 'POST'])
def barChart():
    if request.method == 'POST':
        try:
            fig_prop = make_subplots(
                rows=1, cols=4, shared_yaxes=True, horizontal_spacing=0)
            fig_prop.add_trace(
                go.Bar(x=fourdf['index'], y=fourdf['0'], name='Cluster 0'), row=1, col=1)
            fig_prop.add_trace(
                go.Bar(x=fourdf['index'], y=fourdf['1'], name='Cluster 1'), row=1, col=2)
            fig_prop.add_trace(
                go.Bar(x=fourdf['index'], y=fourdf['2'], name='Cluster 2'), row=1, col=3)
            fig_prop.add_trace(
                go.Bar(x=fourdf['index'], y=fourdf['3'], name='Cluster 3'), row=1, col=4)
            fig_prop.update_yaxes(title_text="duration%/year", row=1, col=1)
            fig_prop.update_layout(
                title_text="Weather distribution in each cluster")
            fig_prop.update_layout(height=460, width=600)
            bar_html = fig_prop.to_html(full_html=False)
            return render_template('kcharts.html', bar_html=bar_html, error3=None)
        except Exception as e:
            app.logger.error(e, exc_info=True)
            return render_template('kcharts.html', error3='An error occurred while processing the request. Try making the request again or report the issue.')
    else:
        return render_template('kcharts.html')


@app.route('/searchBar', methods=['GET', 'POST'])
def searchBar():
    if request.method == 'GET':
        try:
            # Get the search request
            search = request.args.get("search", "")
            rowSize = request.args.get("results-len", default=10, type=int)
            # Open the CSV file and read its contents
            with open("my_dataframe.csv", newline="") as csvfile:
                reader = csv.reader(csvfile)
                data = [row for row in reader if search.lower() in [cell.lower()
                                                                    for cell in row]]
            # Slice the data to only display a certain number of rows
            data = data[:rowSize]
            # Determine the message to display based on the search results
            if data:
                message = f"{len(data)} results found for '{search}'"
            else:
                message = f"No results found for '{search}'"
            # Render the HTML template with the data and message variables
            return render_template("data.html", data=data, message=message, search=search, error=None)
        except Exception as e:
            app.logger.error(e, exc_info=True)
            return render_template('data.html', error='An error occurred while processing the request. Try making the request again or report the issue.')


if __name__ == "__main__":
    app.run(debug=True)
