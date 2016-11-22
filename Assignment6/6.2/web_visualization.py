from flask import Flask
from flask import Request
from flask import jsonify
from flask_cors import CORS, cross_origin
import csv
import json

app = Flask(__name__)
CORS(app)

#the crunching is supposed to happen in python
@app.route("/getCo2")
def getCo2():
    x = []
    y = []

    with open('co2.csv', 'r') as co2:
        readerofthecsv = csv.reader(co2, delimiter=',')

        readerofthecsv=list(readerofthecsv)

        readerofthecsv.pop(0)

        for i in range(len(readerofthecsv)):
            x.append(readerofthecsv[i][0])
            y.append(readerofthecsv[i][1])

    return json.dumps({'years':x, 'arbitraryCo2Units':y})


#the crunching is supposed to happen in python
@app.route('/getTemp/<int:month>')

def getTemp(month):

    x = []
    y = []
    months = ["January", "February", "March", "April", "May",
    "June", "July", "August", "September", "October", "November", "December"]

    if(month <= 12):
        month = month

        print(month)

        with open('temperature.csv', 'r') as temp:
            readerofthecsv = csv.reader(temp, delimiter=',')
            readerofthecsv = list(readerofthecsv)
            readerofthecsv.pop(0)

            for i in range(len(readerofthecsv)):
                x.append(readerofthecsv[i][0])
                y.append(readerofthecsv[i][month])

        return json.dumps({'years':x, 'meanTemperature':y, 'month':months[month-1]})
    else:
        return "har du fler en 12 mndr i året du da?"



if __name__ == "__main__":
    app.run()