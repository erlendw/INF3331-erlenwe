import csv

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.style.use('ggplot')


def plot_temperature(month=1, x_min=None, x_max=None, y_min=None, y_max=None):
    '''
    This method is responsible for returning a plot of temperature per year based on month, x,y min and max are optional.
    if a range is supplied that does not makes sanse given the data, the nearest available max / min will be set.
    '''

    # x and y are set as empty lists
    x = []
    y = []

    # These are to set the month as a label on the plot
    months = ["January", "February", "March", "April", "May",
              "June", "July", "August", "September", "October", "November", "December"]

    # temperature.csv is loaded from the file and read line by line
    with open('temperature.csv', 'r') as temp:
        readerofthecsv = csv.reader(temp, delimiter=',')
        readerofthecsv = list(readerofthecsv)
        # line 0 contains information about the rows, this is removed from the list before the itteration begins
        readerofthecsv.pop(0)

        for i in range(len(readerofthecsv)):
            # extracting the year
            x.append(readerofthecsv[i][0])
            # extracting the data for a given month
            y.append(readerofthecsv[i][month])

    # plot is created
    plt.plot(x, y, label=months[month - 1])
    plt.xlabel("years")
    plt.ylabel("Deg C")
    # legend is added
    plt.legend()

    '''
    This part of the program does some extra logic to find min max so that it is not hardcoded as a methos parameter
    this means that the list can be expanded or reduced without having to change anything in the code
    '''
    if (x_min == None):
        x_min = (min([n for n in x]))

    if (x_max == None):
        x_max = (max([n for n in x]))

    if (y_max == None):
        y_max = (max([n for n in y]))
        y_max = round(float(y_max)) + 1

    if (y_min == None):
        y_min = (max([n for n in y if float(n) < 0]))
        y_min = round(float(y_min)) + - 1

    # limits y
    plt.ylim((y_min, y_max))
    # limits x
    plt.xlim((int(x_min), int(x_max)))
    # shows the plot
    plt.show()


def plot_co2(x_min=None, x_max=None, y_min=None, y_max=None):
    '''
    This method is responsible for plotting co2 per year, x and y min/max are optional
    '''

    # x and y are set as empty lists
    x = []
    y = []

    # co2.csv is loaded from the file and read line by line
    with open('co2.csv', 'r') as co2:
        readerofthecsv = csv.reader(co2, delimiter=',')

        readerofthecsv = list(readerofthecsv)
        # line 0 contains information about the rows, this is removed from the list before the itteration begins
        readerofthecsv.pop(0)
        # itterates
        for i in range(len(readerofthecsv)):
            # current year is extracted
            x.append(readerofthecsv[i][0])
            # co2 emission is extracted
            y.append(readerofthecsv[i][1])

    '''
    This part of the program does some extra logic to find min max so that it is not hardcoded as a method parameters
    this means that the list can be expanded or reduced without having to change anything in the code
    '''

    if (x_min == None):
        x_min = (min([n for n in x]))


    if (x_max == None):
        x_max = (max([n for n in x]))


    if (y_max == None):
        y_max = (max([int(n) for n in y]))


    if (y_min == None):
        y_min = (min([int(n) for n in y]))


    # plot is created
    plt.plot(x, y)
    # x and y are limited
    plt.ylim((y_min, y_max))
    plt.xlim((int(x_min), int(x_max)))

    plt.xlabel("years")
    plt.ylabel("Co2")
    # plot is shown
    plt.show()

def isBlank(myString):

    '''
    Helper function to check if a string is empty or blank
    '''

    if myString and myString.strip():
        # myString is not None AND myString is not empty or blank
        return False
    # myString is None OR myString is empty or blank
    return True



def plot_co2_by_contry(year="2012", y_min="0", y_max="100"):
    '''
    This method is responsible for plotting co2 emission per capita in a given contry in a supplied year, x and y min/max are hardcoded as
    parameters.
    '''


    contry = []  # holds the name of a contry

    allCo2perContry = [] # holds data about the datasets of a given contry
    availableYears = [] # these are the available years

    x = []  # contry
    y = []  # co2 / year_index

    #this is needed because pyplot does not accept a string as a datapoint for y
    y_indexes = []
    #variable for keeping track of the current y index
    yindex = 0

    #reads CO2_by_country.csv
    with open('CO2_by_country.csv', 'r') as co2:
        readerofthecsv = csv.reader(co2, delimiter=',')
        readerofthecsv = list(readerofthecsv)

        for i in range(len(readerofthecsv)):
            dataPerYear = readerofthecsv[i][4:len(readerofthecsv)]  # this is all the available data for a contry
            # based on the year_index we want to add one data point from the list above

            if (i == 0):
                availableYears = dataPerYear
                yearIndex = availableYears.index(year)

            else:
                contry.append(readerofthecsv[i][0])
                allCo2perContry.append(dataPerYear)

        # for every contry we want to get the data for a given year_index if all the fields are valid
        for j in range(len(contry)):
            #chacks that all the data that will be added to the set is valid
            if (not isBlank(availableYears[yearIndex]) and not isBlank(contry[j]) and not isBlank(
                    allCo2perContry[j][yearIndex])):
                #checks that the point is within supplied min max
                lessThanMax = (float(allCo2perContry[j][yearIndex]) < float(y_max))
                moreThanMin = (float(allCo2perContry[j][yearIndex]) > float(y_min))
                if (lessThanMax and moreThanMin):
                    #appends and inrements the data that the plot uses
                    x.append(contry[j])
                    y.append(float(allCo2perContry[j][yearIndex]))
                    y_indexes.append(yindex)
                    yindex += 1

    #creates the tics that are added to the y indexes
    plt.xticks(y_indexes, x, rotation='vertical')
    #creates the barchart
    plt.bar(y_indexes, y, width=1, align='center')

    plt.xlabel("contry")
    plt.ylabel("Co2/capita")

    #not to great full screen setup
    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())

    #plot is shown
    plt.show()




"""
 assume that temperature is roughly a linear function of CO2 emission,
estimating the coefficients of the linear function from recent data points (using
the past 2 is fine, as is using the past 10 or so if you want to be more thorough).
Further, assume that the rate of increase of CO2 emissions is going to be the
same as it is today (i.e. if there were X tons more CO2 emissions in 2016 than
in 2015, there will be X tons more CO2 emissions in 2017 than in 2016). Using
this, you will be able to get an estimate of the CO2 emissions and temperature
in later years.
"""


# assume that temperature is roughly a linear function of CO2 emission
# f(x)=ax+b

def predictingTheFuture(month=1, years = 100):

    """
    This method predicts the grim frim future. It is based on a making a best fit plot on the scattered data of co2 x and
    tmperature y, From that we are able to calculate our ax+b and create a linear function where x is the co2 per year
    after 2012 the line is made from the estimated data
    """

    #sets up the empty arrays
    y = []
    x = []

    #contains the years of each of the datasets
    y_years = []
    x_years = []

    #opens the csv file
    with open('temperature.csv', 'r') as temp:
        readerofthecsv = csv.reader(temp, delimiter=',')
        readerofthecsv = list(readerofthecsv)
        readerofthecsv.pop(0)

    #itterates the csv file
    for i in range(len(readerofthecsv)):
        y_years.append(int(readerofthecsv[i][0]))
        y.append(readerofthecsv[i][month])

    #opens the csv file
    with open('co2.csv', 'r') as co2:
        readerofthecsv = csv.reader(co2, delimiter=',')

        readerofthecsv = list(readerofthecsv)

        readerofthecsv.pop(0)

        #itterates the csv file
        for i in range(len(readerofthecsv)):
            x_years.append(float(readerofthecsv[i][0]))
            x.append(float(readerofthecsv[i][1]))

    #finding min and max of the years
    startyear_temp = min(y_years)
    startyear_co2 = min(x_years)

    endyear_temp = max(y_years)
    endyear_co2 = max(x_years)

    #cheks the datasets and removes the data that does not have a corresponing entry in the other dataset
    if (startyear_temp > startyear_co2):
        x = x[x_years.index(startyear_temp):]

    elif ((startyear_temp < startyear_co2)):

        y = y[y_years.index(startyear_co2):]

    if (endyear_temp > endyear_co2):
        x = x[x_years.index(endyear_temp):]

    elif (endyear_temp < endyear_co2):
        y = y[:y_years.index(endyear_co2)]


    #converts to numpy array for polyfit
    x_np = np.asarray(x,dtype=float)
    y_np = np.asarray(y,dtype=float)

    #calculates the slope and intercept (ax+b) where a = slope and b = intercept
    slope , intercept = np.polyfit(x_np,y_np,1)

    '''
    Further, assume that the rate of increase of CO2 emissions is going to be the
    same as it is today (i.e. if there were X tons more CO2 emissions in 2016 than
    in 2015, there will be X tons more CO2 emissions in 2017 than in 2016). Using
    this, you will be able to get an estimate of the CO2 emissions and temperature
    in later years.
    '''

    #creates n new data points as specified by the number of years submitted by the end user
    increase = x[len(x)-1]/x[len(x)-2]
    for i in range(years):
        x.append((x[len(x)-1] * increase))
        y_years.append(y_years[len(y_years)-1] + 1)
        increase = x[len(x) - 1] / x[len(x) - 2]

    # creates a new line based on the co2 data x
    x_np = np.asarray(x,dtype=float)
    linearfunc = slope * x_np + intercept


    #limits the plots for real and predicted data, plots them in different colors
    plt.plot(y_years[:len(y_years) - years], linearfunc[:len(y_years) - years] , 'g')
    plt.plot(y_years[len(y_years) - years:], linearfunc[len(y_years) - years:], 'r')
    plt.xlabel("year")
    plt.ylabel("Co2")

    plt.show()


