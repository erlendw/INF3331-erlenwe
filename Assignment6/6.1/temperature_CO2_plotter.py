import csv

import matplotlib.pyplot as plt

import numpy as np

import pandas as pd


'''
Todo :: add time range, x and y min/max
'''


def plot_temperature(month, x_min=None, x_max=None, y_min=None, y_max=None):
    x = []
    y = []
    months = ["January", "February", "March", "April", "May",
              "June", "July", "August", "September", "October", "November", "December"]
    print(month)

    with open('temperature.csv', 'r') as temp:
        readerofthecsv = csv.reader(temp, delimiter=',')
        readerofthecsv = list(readerofthecsv)
        readerofthecsv.pop(0)

        for i in range(len(readerofthecsv)):
            x.append(readerofthecsv[i][0])
            y.append(readerofthecsv[i][month])

    plt.plot(x, y, label=months[month - 1])
    plt.legend()

    if (x_min == None):
        x_min = (min([n for n in x]))
        print(x_min)

    if (x_max == None):
        x_max = (max([n for n in x]))
        print(x_max)

    if (y_max == None):
        y_max = (max([n for n in y]))
        print(y_max)
        y_max = round(float(y_max)) + 1

    if (y_min == None):
        y_min = (max([n for n in y if float(n) < 0]))
        y_min = round(float(y_min)) + - 1
        print(y_min)

    plt.ylim((y_min, y_max))
    plt.xlim((int(x_min), int(x_max)))
    plt.show()


def plot_co2(x_min=None, x_max=None, y_min=None, y_max=None):
    x = []
    y = []

    with open('co2.csv', 'r') as co2:
        readerofthecsv = csv.reader(co2, delimiter=',')

        readerofthecsv = list(readerofthecsv)

        readerofthecsv.pop(0)

        for i in range(len(readerofthecsv)):
            x.append(readerofthecsv[i][0])
            y.append(readerofthecsv[i][1])

    if (x_min == None):
        x_min = (min([n for n in x]))
        print(x_min)

    if (x_max == None):
        x_max = (max([n for n in x]))
        print(x_max)

    if (y_max == None):
        y_max = (max([int(n) for n in y]))

        print(y_max)

    if (y_min == None):
        y_min = (min([int(n) for n in y]))
        print(y_min)

    plt.plot(x, y)

    plt.ylim((y_min, y_max))
    plt.xlim((int(x_min), int(x_max)))

    plt.show()


"""
Given a year: say 1960 we want to wxtract all valid datasets x:contry and y:co2 for that year
"""

def plot_co2_by_contry(year="1960", y_min="0",y_max ="3"):

    contry = []#contry
    allCo2perContry = []
    availableYears = []

    x = []#contry
    y = []#co2 / year
    y_indexes = []

    with open('CO2_by_country.csv', 'r') as co2:
        readerofthecsv = csv.reader(co2, delimiter=',')
        readerofthecsv = list(readerofthecsv)

        for i in range(len(readerofthecsv)):
            dataPerYear = readerofthecsv[i][4:len(readerofthecsv)] # this is all the available data for a contry
            #based on the year we want to add one data point from the list above

            if(i == 0 ):
                availableYears = dataPerYear
                yearIndex = availableYears.index(year)

            else:
                contry.append(readerofthecsv[i][0])
                allCo2perContry.append(dataPerYear)


        # for every contry we want to get the data for a given year if all the fields are valid
        for j in range(len(contry)):
            if (not isBlank(availableYears[yearIndex]) and not isBlank(contry[j]) and not isBlank(allCo2perContry[j][yearIndex])):
                # print(x[i],contry[j], y[j][i])


                lessThanMax = (float(allCo2perContry[j][yearIndex] ) < float(y_max))

                moreThanMin = (float(allCo2perContry[j][yearIndex]) > float(y_min))

                if(lessThanMax and moreThanMin):
                    x.append(contry[j])
                    y.append(float(allCo2perContry[j][yearIndex]))
                    y_indexes.append(j)


    print(y)

    plt.bar(y_indexes, y, width=0.35 , align='center')

    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())

    plt.show()





def isBlank (myString):
    if myString and myString.strip():
        #myString is not None AND myString is not empty or blank
        return False
    #myString is None OR myString is empty or blank
    return True


plot_co2_by_contry()