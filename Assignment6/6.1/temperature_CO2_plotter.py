import csv

import matplotlib.pyplot as plt

import matplotlib
matplotlib.style.use('ggplot')

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
Given a year_index: say 1960 we want to wxtract all valid datasets x:contry and y:co2 for that year_index
"""

def plot_co2_by_contry(year="2012", y_min="0",y_max ="100"):

    contry = []#contry
    allCo2perContry = []
    availableYears = []

    x = []#contry
    y = []#co2 / year_index
    y_indexes = []
    yindex = 0
    with open('CO2_by_country.csv', 'r') as co2:
        readerofthecsv = csv.reader(co2, delimiter=',')
        readerofthecsv = list(readerofthecsv)

        for i in range(len(readerofthecsv)):
            dataPerYear = readerofthecsv[i][4:len(readerofthecsv)] # this is all the available data for a contry
            #based on the year_index we want to add one data point from the list above

            if(i == 0 ):
                availableYears = dataPerYear
                yearIndex = availableYears.index(year)

            else:
                contry.append(readerofthecsv[i][0])
                allCo2perContry.append(dataPerYear)

        # for every contry we want to get the data for a given year_index if all the fields are valid
        for j in range(len(contry)):
            if (not isBlank(availableYears[yearIndex]) and not isBlank(contry[j]) and not isBlank(allCo2perContry[j][yearIndex])):
                # print(x[i],contry[j], y[j][i])
                lessThanMax = (float(allCo2perContry[j][yearIndex] ) < float(y_max))
                moreThanMin = (float(allCo2perContry[j][yearIndex]) > float(y_min))
                if(lessThanMax and moreThanMin):
                    x.append(contry[j])
                    y.append(float(allCo2perContry[j][yearIndex]))
                    y_indexes.append(yindex)
                    yindex+=1


    print(y)

    plt.xticks(y_indexes, x, rotation='vertical')
    plt.bar(y_indexes, y, width=1 , align='center')

    mng = plt.get_current_fig_manager()
    mng.resize(*mng.window.maxsize())

    plt.show()





def isBlank (myString):
    if myString and myString.strip():
        #myString is not None AND myString is not empty or blank
        return False
    #myString is None OR myString is empty or blank
    return True



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

#assume that temperature is roughly a linear function of CO2 emission
#f(x)=ax+b

def predictingTheFuture(month = 1):

    y = [] # temp
    x = [] # co2

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
            x_years.append(int(readerofthecsv[i][0]))
            x.append(readerofthecsv[i][1])




    startyear_temp = min(y_years)
    startyear_co2 = min(x_years)

    endyear_temp = max(y_years)
    endyear_co2 = max(x_years)




    if(startyear_temp>startyear_co2):
        x = x[x_years.index(startyear_temp):]

    elif((startyear_temp<startyear_co2)):

        y = y[y_years.index(startyear_co2):]



    if (endyear_temp > endyear_co2):
        x = x[x_years.index(endyear_temp):]

    elif (endyear_temp < endyear_co2):
        y = y[:y_years.index(endyear_co2)]

    print(len(x))
    print(len(y))



    plt.scatter(x, y)

    plt.show()

#ax+b



predictingTheFuture()

