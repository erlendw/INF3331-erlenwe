import csv
import matplotlib.pyplot as plt
import numpy as np



'''
Todo :: add time range, x and y min/max
'''
def plot_temperature(month, year_start=None, year_end=None, y_min=None, y_max=None):
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

    plt.plot(x,y, label=months[month-1])
    plt.legend()

    if (year_start == None):
        year_start = (min([n for n in x]))
        print(year_start)

    if (year_end == None):
        year_end = (max([n for n in x]))
        print(year_end)

    if(y_max == None):
        y_max = (max([n for n in y]))
        print(y_max)
        y_max = round(float(y_max)) + 1

    if(y_min == None):
        y_min = (max([n for n in y if float(n)<0]))
        y_min = round(float(y_min)) +- 1
        print(y_min)



    plt.ylim((y_min,y_max))
    plt.xlim((int(year_start), int(year_end)))
    plt.show()

def plot_co2(year_start=None, year_end=None, y_min=None, y_max=None):
    x = []
    y = []

    with open('co2.csv', 'r') as co2:
        readerofthecsv = csv.reader(co2, delimiter=',')

        readerofthecsv=list(readerofthecsv)

        readerofthecsv.pop(0)

        for i in range(len(readerofthecsv)):
            x.append(readerofthecsv[i][0])
            y.append(readerofthecsv[i][1])

    if (year_start == None):
        year_start = (min([n for n in x]))
        print(year_start)

    if (year_end == None):
        year_end = (max([n for n in x]))
        print(year_end)

    if (y_max == None):
        y_max = (max([int(n) for n in y]))

        print(y_max)


    if (y_min == None):
        y_min = (min([int(n) for n in y]))
        print(y_min)

    plt.plot(x,y)

    plt.ylim((y_min, y_max))
    plt.xlim((int(year_start), int(year_end)))

    plt.show()

