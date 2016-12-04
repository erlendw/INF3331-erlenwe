import csv
import json
import sys
import os
import numpy as np

from flask import Flask, send_from_directory, render_template
from flask import request
#from flask_cors import CORS


app = Flask(__name__)
'''
creates the flask app
'''
#CORS(app)# adds cross site support to the flask app


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):

    '''
    This is a "catchAll" method that ensures that flask is only loaded when valid api routes are loaded. This is to
    avoid conflict in the react router in the user interface.
    '''

    return render_template('index.html') #fetches the index file from "static"


@app.route('/docs/temperature_CO2_plotter')
def returnDocsTemp():
    '''
    Renders the docs for python module temperature_CO2_plotter
    '''
    return render_template('temperature_CO2_plotter.m.html')

@app.route('/docs/web_visualization')
def returnDocsFlask():
    '''
    Renders the docs for python module web_visualization
    '''
    return render_template('web_visualization.m.html')

@app.route('/<path:filename>')
def serve_static(filename):
    '''
    this method is responsible for returning all static files. The front end is transpiled and served as one large
    javascript file. But in theory any js, css etc could be placed in the static folder
    '''
    return send_from_directory(filename)



@app.route('/getCo2', methods=['POST', 'GET'])
def getCo2():
    '''
    This method extracts the co2 per year and returns it as to lists x and y to be rendered server side, parameters can
        be changed by posting data, otherwise the entire dataset is returned. Accepts post and get
    '''
    x = []
    y = []

    """
    Opens the csv and saves the data to a list
    """
    with open('co2.csv', 'r') as co2:
        readerofthecsv = csv.reader(co2, delimiter=',')
        readerofthecsv = list(readerofthecsv)
        readerofthecsv.pop(0)

    """
    list is itterated and every item is added to the list
    """
    for line in readerofthecsv:
        x.append(int(line[0]))
        y.append(int(line[1]))

    """"
    the x and y max min points are found, i do this so that the underlying data can be changed without having to change
    the code
    """
    y_min = (min(y))
    y_max = (max(y))

    x_min = (min(x))
    x_max = (max(x))

    """
    the values are added to a dictionary that can be compared with the posted dict
    """
    graph_dict = {'x_min': x_min, 'x_max': x_max, 'y_min': y_min, 'y_max': y_max}

    '''
    If the method is a post, we will check what has been supplied
    '''
    if (request.method == 'POST'):
        #pulls the json from the post from the front end
        result = request.get_json()
        #itterates over the supplied data and checks if any data in the graph dict should be overwritten
        for key in result:
            try:
                """"
                if the dict[key] excists it is replaced by the incoming max min
                """
                graph_dict[key] = int(result[key])
            except KeyError:
                print('not in dict')

    """
    x and y are cleared as we needed the initial max min numbers
    here a test can be added to check if the numbers have been modified
    """

    x.clear()
    y.clear()

    """
    x and y are rebuilt with apropriate bounderies
    """

    for line in readerofthecsv:
        x_line = (int(line[0]))
        y_line = (int(line[1]))

        if ((x_line >= graph_dict['x_min'] and x_line <= graph_dict['x_max']) and (
                y_line >= graph_dict['y_min'] and y_line <= graph_dict['y_max'])):
            x.append(int(line[0]))
            y.append(int(line[1]))

    """
    json is returned to end user
    """
    return json.dumps({'years': x, 'arbitraryCo2Units': y})


@app.route('/getTemp', methods=['POST', 'GET'])
@app.route('/getTemp/<int:month>')
def getTemp(month=1):
    """
    This method is responsible for getting the temperature per year given a specific month
    """
    if (request.method == 'POST'):
        #if the method is post, we try to extract month
        result = request.get_json()
        try:
            month = int(result['month'])
        except KeyError:
            month = 1

    print(month)

    #sets up empty lists for x and y
    x = []
    y = []

    #months are listed to return to the front end
    months = ["January", "February", "March", "April", "May",
              "June", "July", "August", "September", "October", "November", "December"]

    #opens the temperature data from the temperature.csv file
    with open('temperature.csv', 'r') as temp:
        readerofthecsv = csv.reader(temp, delimiter=',')
        readerofthecsv = list(readerofthecsv)
        #row 0 contains info of the rows, and it should not be sent back to the frontend
        readerofthecsv.pop(0)

    #itterates over the lines of the rows of the csv file
    for line in readerofthecsv:
        x.append(int(line[0]))
        y.append(float(line[month]))

    """"
    the x and y max min points are found
    """
    y_min = (min(y))
    y_max = (max(y))

    x_min = (min(x))
    x_max = (max(x))

    """
    the values are added to a dictionary that can be compared with the posted dict
    """
    graph_dict = {'x_min': x_min, 'x_max': x_max, 'y_min': y_min, 'y_max': y_max}

    #if the method is post, we itterate over the keys in the response
    if (request.method == 'POST'):
        for key in result:
            try:
                """"
                if the dict[key] excists it is replaced by the incoming max min
                """
                graph_dict[key] = int(result[key])
            except KeyError:
                print('not in dict')

    #clear and rebuild the x and y arrays
    x.clear()
    y.clear()

    """
    x and y are rebuilt with apropriate bounderies
    """

    for line in readerofthecsv:

        x_line = (int(line[0]))
        y_line = (float(line[month]))

        if ((x_line >= graph_dict['x_min'] and x_line <= graph_dict['x_max']) and (
                        y_line >= graph_dict['y_min'] and y_line <= graph_dict['y_max'])):
            x.append(int(line[0]))
            y.append(float(line[month]))

    return json.dumps({'years': x, 'meanTemperature': y, 'month': months[month - 1]})


def isBlank(myString):

    '''
    Helper function to check if a string is empty or blank
    '''

    if myString and myString.strip():
        # myString is not None AND myString is not empty or blank
        return False
    # myString is None OR myString is empty or blank
    return True


@app.route("/getCo2ByContry", methods=['POST', 'GET'])
@app.route('/getCo2ByContry/<int:year>')
def getCo2ByContry(year=1960):

    '''
    This method is responisble for for returning the co2 per capita in a given year. The min year is hardcoded as a paramater.
    '''

    MAX = sys.maxsize #sets an arbitrary min and max
    MIN = (-MAX)#


    #creates the graph dictionary
    graph_dict = {'x_min': MIN, 'x_max': MAX, 'y_min': MIN, 'y_max': MAX, 'year': year}

    #checks if the method is post
    if (request.method == 'POST'):
        #the result of the request
        result = request.get_json()

        print(result)

        #itterates and overwrites the apropriate data in the graph dict
        for key in result:
            try:
                """"
                if the dict[key] excists it is replaced by the incoming max min
                """
                graph_dict[key] = float(result[key])
            except KeyError:
                print('not in dict')

    #y_min and max is hardcoded //need to fix
    y_max = 100
    y_min = 0

    contry = []  # contry
    allCo2perContry = [] # all co2 data / contry
    availableYears = [] # all available years

    x = []  # contry
    y = []  # co2 / year_index

    #reads the csv file
    with open('CO2_by_country.csv', 'r') as co2:
        readerofthecsv = csv.reader(co2, delimiter=',')
        readerofthecsv = list(readerofthecsv)

        #itterates over the csv file
        for i in range(len(readerofthecsv)):
            dataPerYear = readerofthecsv[i][4:len(readerofthecsv)]  # this is all the available data for a contry
            # based on the year_index we want to add one data point from the list above
            #checks if the line is 0, if so we
            if (i == 0):
                availableYears = dataPerYear
                yearIndex = dataPerYear.index(str(int(graph_dict['year'])))

            else:
                #gets the current contry and appends it to the list
                contry.append(readerofthecsv[i][0])
                allCo2perContry.append(dataPerYear)

        # for every contry we want to get the data for a given year_index if all the fields are valid


        #itterates over the data
        for j in range(len(contry)):
            #checks that the datapoints are valid
            if (not isBlank(availableYears[yearIndex]) and not isBlank(contry[j]) and not isBlank(
                    allCo2perContry[j][yearIndex])):

                lessThanMax = (float(allCo2perContry[j][yearIndex]) <= graph_dict['y_max'])
                moreThanMin = (float(allCo2perContry[j][yearIndex]) >= graph_dict['y_min'])

                if (lessThanMax and moreThanMin):
                    x.append(contry[j])
                    y.append(float(allCo2perContry[j][yearIndex]))

    return json.dumps({'contry': x, 'arbitraryCo2Units': y, 'years': availableYears})

@app.route("/predictingTheFuture", methods=['GET','POST'])
@app.route('/predictingTheFuture/<int:month>/<int:years>')
def predictingTheFuture(month=1, years=100):

    y = []  # temp
    x = []  # co2

    y_years = []
    x_years = []

    with open('temperature.csv', 'r') as temp:
        readerofthecsv = csv.reader(temp, delimiter=',')
        readerofthecsv = list(readerofthecsv)
        readerofthecsv.pop(0)

    for i in range(len(readerofthecsv)):
        y_years.append(int(readerofthecsv[i][0]))
        y.append(readerofthecsv[i][month])

    with open('co2.csv', 'r') as co2:
        readerofthecsv = csv.reader(co2, delimiter=',')

        readerofthecsv = list(readerofthecsv)

        readerofthecsv.pop(0)

        for i in range(len(readerofthecsv)):
            x_years.append(float(readerofthecsv[i][0]))
            x.append(round(float(readerofthecsv[i][1]),2))

    print(x)

    startyear_temp = min(y_years)
    startyear_co2 = min(x_years)

    endyear_temp = max(y_years)
    endyear_co2 = max(x_years)

    if (startyear_temp > startyear_co2):
        x = x[x_years.index(startyear_temp):]

    elif ((startyear_temp < startyear_co2)):

        y = y[y_years.index(startyear_co2):]

    if (endyear_temp > endyear_co2):
        x = x[x_years.index(endyear_temp):]

    elif (endyear_temp < endyear_co2):
        y = y[:y_years.index(endyear_co2)]

    print(len(x))
    print(len(y))

    x_np = np.asarray(x, dtype=float)
    y_np = np.asarray(y, dtype=float)

    slope, intercept = np.polyfit(x_np, y_np, 1)

    '''
    Further, assume that the rate of increase of CO2 emissions is going to be the
    same as it is today (i.e. if there were X tons more CO2 emissions in 2016 than
    in 2015, there will be X tons more CO2 emissions in 2017 than in 2016). Using
    this, you will be able to get an estimate of the CO2 emissions and temperature
    in later years.
    '''
    increase = x[len(x) - 1] / x[len(x) - 2]
    finalrealyear = y_years[len(y_years)-1]
    for i in range(years):
        x.append((x[len(x) - 1] * increase))
        y_years.append(y_years[len(y_years) - 1] + 1)
        increase = x[len(x) - 1] / x[len(x) - 2]

    print(x)

    x_np = np.asarray(x, dtype=float)

    linearfunc = slope * x_np + intercept
    print(y_years)

    return json.dumps({'years': y_years,'meanTemperature' : linearfunc.tolist() , 'finalrealyear' : finalrealyear})

#    return json.dumps({'years': x, 'meanTemperature': y, 'month': months[month - 1]})



@app.errorhandler(500)
def internal_error(error):
    '''
    Handles 500 error
    '''
    return "500 error"


@app.errorhandler(404)
def not_found(error):
    '''
    Handles 404 //todo add custom
    '''
    return "404 error", 404


if __name__ == "__main__":
    '''
    I am main, hear me roar
    '''
    app.debug = True
    app.run()
