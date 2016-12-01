from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import csv
import json



app = Flask(__name__)
CORS(app)

"""
Should inputs of y_min be lower than the smallest number?
"""
@app.route('/getCo2', methods=['POST', 'GET'])
def getCo2():

    """
    empty x and y axis
    """
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
    the x and y max min points are found
    """
    y_min = (min(y))
    y_max = (max(y))

    x_min = (min(x))
    x_max = (max(x))


    """
    the values are added to a dictionary that can be compared with the posted dict
    """
    graph_dict = {'x_min':x_min,'x_max':x_max,'y_min':y_min,'y_max':y_max}

    if (request.method == 'POST'):

        for key in request.form:
            try:
                """"
                if the dict[key] excists it is replaced by the incoming max min
                """

                graph_dict[key] = int(request.form[key])
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

        if((x_line >= graph_dict['x_min'] and x_line <= graph_dict['x_max']) and (y_line >= graph_dict['y_min'] and y_line <= graph_dict['y_max']) ):
            x.append(int(line[0]))
            y.append(int(line[1]))

    """
    json is returned to end user
    """
    return json.dumps({'years': x, 'arbitraryCo2Units': y})


@app.route('/getTemp', methods=['POST','GET'])
@app.route('/getTemp/<int:month>')
def getTemp(month=1):


    if (request.method == 'POST'):
        try:
            month = int(request.form['month'])
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
    graph_dict = {'x_min':x_min,'x_max':x_max,'y_min':y_min,'y_max':y_max}

    if (request.method == 'POST'):

        for key in request.form:
            try:
                """"
                if the dict[key] excists it is replaced by the incoming max min
                """

                graph_dict[key] = int(request.form[key])
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


@app.errorhandler(500)
def internal_error(error):

    return "500 error"

@app.errorhandler(404)
def not_found(error):
    return "404 error",404


if __name__ == "__main__":
    app.run()