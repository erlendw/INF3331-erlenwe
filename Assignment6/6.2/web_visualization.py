import csv
import json
import sys
import os

from flask import Flask,make_response, send_from_directory, render_template
from flask import request
from flask_cors import CORS


app = Flask(__name__)
'''
creates the flask app
'''
CORS(app)# adds cross site support to the flask app


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):

    '''
    This is a "catchAll" method that ensures that flask is only loaded when valid api routes are loaded. This is to
    avoid conflict in the react router in the user interface.
    '''

    return render_template('index.html') #fetches the index file from "static"


@app.route('/docs/temperature_CO2_plotter')
def returnDocs():
    return render_template('temperature_CO2_plotter.m.html')



@app.route('/js/<path:filename>')
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
    if (request.method == 'POST'):

        result = request.get_json()

        print(result)

        try:
            month = int(result['month'])
        except KeyError:
            month = 1

    print(month)

    x = []
    y = []

    months = ["January", "February", "March", "April", "May",
              "June", "July", "August", "September", "October", "November", "December"]

    with open('temperature.csv', 'r') as temp:
        readerofthecsv = csv.reader(temp, delimiter=',')
        readerofthecsv = list(readerofthecsv)
        readerofthecsv.pop(0)

    for line in readerofthecsv:
        x.append(int(line[0]))

        y.append(float(line[month]))

    print(y)

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

    if (request.method == 'POST'):

        for key in result:
            try:
                """"
                if the dict[key] excists it is replaced by the incoming max min
                """

                graph_dict[key] = int(result[key])
            except KeyError:
                print('not in dict')

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
    MAX = sys.maxsize
    MIN = (-MAX)

    print(MIN, MAX)

    graph_dict = {'x_min': MIN, 'x_max': MAX, 'y_min': MIN, 'y_max': MAX, 'year': year}

    if (request.method == 'POST'):

        result = request.get_json()

        print(result)

        for key in result:
            try:
                """"
                if the dict[key] excists it is replaced by the incoming max min
                """
                graph_dict[key] = float(result[key])
            except KeyError:
                print('not in dict')

    y_max = 100
    y_min = 0

    contry = []  # contry
    allCo2perContry = []
    availableYears = []

    x = []  # contry
    y = []  # co2 / year_index

    with open('CO2_by_country.csv', 'r') as co2:
        readerofthecsv = csv.reader(co2, delimiter=',')
        readerofthecsv = list(readerofthecsv)

        for i in range(len(readerofthecsv)):
            dataPerYear = readerofthecsv[i][4:len(readerofthecsv)]  # this is all the available data for a contry
            # based on the year_index we want to add one data point from the list above

            if (i == 0):
                availableYears = dataPerYear
                yearIndex = dataPerYear.index(str(int(graph_dict['year'])))

            else:
                contry.append(readerofthecsv[i][0])
                allCo2perContry.append(dataPerYear)

        # for every contry we want to get the data for a given year_index if all the fields are valid



        for j in range(len(contry)):

            if (not isBlank(availableYears[yearIndex]) and not isBlank(contry[j]) and not isBlank(
                    allCo2perContry[j][yearIndex])):

                lessThanMax = (float(allCo2perContry[j][yearIndex]) <= graph_dict['y_max'])
                moreThanMin = (float(allCo2perContry[j][yearIndex]) >= graph_dict['y_min'])

                if (lessThanMax and moreThanMin):
                    x.append(contry[j])
                    y.append(float(allCo2perContry[j][yearIndex]))

    return json.dumps({'contry': x, 'arbitraryCo2Units': y, 'years': availableYears})


@app.errorhandler(500)
def internal_error(error):
    return "500 error"


@app.errorhandler(404)
def not_found(error):
    return "404 error", 404


if __name__ == "__main__":
    app.debug = True
    app.run()
