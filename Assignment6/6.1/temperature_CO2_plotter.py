import csv
import matplotlib.pyplot as plt



'''
Todo :: add time range, x and y min/max
'''
def plot_temperature(month):
    x = []
    y = []
    months = ["January", "February", "March", "April", "May",
  "June", "July", "August", "September", "October", "November", "December"]


    month = month

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
    plt.show()

def plot_co2():
    x = []
    y = []

    with open('co2.csv', 'r') as co2:
        readerofthecsv = csv.reader(co2, delimiter=',')

        readerofthecsv=list(readerofthecsv)

        readerofthecsv.pop(0)

        for i in range(len(readerofthecsv)):
            x.append(readerofthecsv[i][0])
            y.append(readerofthecsv[i][1])

    plt.plot(x,y)
    plt.show()


plot_temperature(3)