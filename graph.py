"""
Author: Solomon James Ador-Dionisio
Filename: graph.py
Date: 08/05/24
Description: In this module, the function sort_dic, convertdata_list, linechart_year, piechart_developer, piechart_reg,
and piechart_platform were created. The first two functions are used to sort and configure the data given, in the form
of dictionaries. Linechart_year, piechart_developer, piechart_reg, and piechart_platform are used to display graphs and
calculate certain pieces of data specifically from the csv file, video_games_sales.csv.
"""
import matplotlib.pyplot


def sort_dic(dic_):
    """
    Takes <dic_> and returns it sorted

    Parameter:
    dic_ -- dictionary of any values

    Return:
    sorted_dict -- sorted dic_
    """
    # Takes all the keys and puts them into a list to be sorted
    keys = list(dic_.keys())
    keys.sort()

    # Creates a new dictionary with the sorted keys, and their values
    sorted_dict = {x: dic_[x] for x in keys}
    return sorted_dict


def convertdata_list(dic_):
    """
    Takes <dic_> and returns two parallel lists one being the keys and the other being the values.

    Parameter:
    dic_ -- dictionary of any values

    Return:
    x -- list of keys
    y -- list of values
    """
    x = list(dic_.keys())

    # Loops through each element in the dictionary and returns the values
    y = [dic_[key] for key in x]

    return x, y


def linechart_year(dic_, title, axisx, axisy):
    """
    Takes <dic_>, sorts it, plots the data to a line-graph, and displays the graph.

    Parameter:
    dic_ -- dictionary of any values
    title -- title of the graph
    axisx -- label for the x-axis
    axisy -- label for the y-axis
    """
    # Prepares the data
    x, y = convertdata_list(sort_dic(dic_))

    # Plots the data on a line-graph
    matplotlib.pyplot.plot(x, y)

    # Generates the appropriate labels
    matplotlib.pyplot.title(title)
    matplotlib.pyplot.xlabel(axisx)
    matplotlib.pyplot.ylabel(axisy)

    # Displays the graph
    matplotlib.pyplot.show()


def piechart_developer(dic_, title):
    """
    Takes <dic_>, sorts it, calculates the average sale for each developer, displays it to a pie-chart in comparison to
    other developers.

    Parameter:
    dic_ -- dictionary of any values
    title -- title of the graph
    """
    # Creates a new data for the section of "Other"
    dic_["Other"] = [0, 0]
    remove = []

    # Determines which keys in the dictionary must be removed and added to other
    for x in dic_:
        if dic_[x][1] <= 130:
            dic_["Other"][0] += dic_[x][0]
            dic_["Other"][1] += dic_[x][1]
            remove.append(x)

    # Extra data is removed
    for x in remove:
        dic_.pop(x)

    # Prepares the data
    x, y = convertdata_list(sort_dic(dic_))

    # Calculates the average sale for each developer by taking the total sales divided by the total amount of games
    # published
    avg_y = [(z[0])/z[1] for z in y]

    # Plots the calculated data onto a pie-chart
    matplotlib.pyplot.pie(avg_y, labels=x)

    # Generates the appropriate labels, legend is custom-ly fitted
    matplotlib.pyplot.legend(bbox_to_anchor=(0.5, -0.05), ncol=5, loc="center")
    matplotlib.pyplot.title(title)

    # Displays the graph
    matplotlib.pyplot.show()


def piechart_reg(dic_, title):
    """
    Takes <dic_>, sorts the data accordingly, displays it to a pie-chart

    Parameter:
    dic_ -- dictionary of any values
    title -- title of the graph
    """
    # Prepares the data
    x, y, = convertdata_list(dic_)

    # Plots the calculated data onto a pie-chart
    matplotlib.pyplot.pie(y, labels=x)

    # Generates the appropriate labels
    if len(x) <= 5:
        matplotlib.pyplot.legend(ncol=2)
    else:
        matplotlib.pyplot.legend(bbox_to_anchor=(0.5, -0.05), ncol=5, loc="center")
    matplotlib.pyplot.title(title)

    # Displays the graph
    matplotlib.pyplot.show()


def bargraph_platform(dic_, title, axisx, axisy):
    """
    Takes <dic_>, sorts the data accordingly, displays it to a bargraph in comparison to
    other platforms.

    Parameter:
    dic_ -- dictionary of any values
    title -- title of the graph
    axisx -- label for the x-axis
    axisy -- label for the y-axis
    """
    # Creates a new data for the section of "Other"
    dic_["Other"] = 0
    remove = []

    # Determines which keys in the dictionary must be removed and added to other
    for x in dic_:
        if dic_[x] <= 100:
            dic_["Other"] += dic_[x]
            remove.append(x)

    # Extra data is removed
    for x in remove:
        dic_.pop(x)

    # Prepares the data
    x, y, = convertdata_list(dic_)

    # Plots the  data onto a bargraph
    matplotlib.pyplot.bar(x, height=y)

    # Generates the appropriate labels
    matplotlib.pyplot.title(title)
    matplotlib.pyplot.xlabel(axisx)
    matplotlib.pyplot.ylabel(axisy)

    # Displays the graph
    matplotlib.pyplot.show()


if __name__ == "__main__":
    # Testing
    dic = {2006: 521.04, 1985: 53.94, 2008: 678.9, 2009: 667.3, 1996: 199.15, 1989: 73.45, 1984: 50.36, 2005: 459.94,
           1999: 251.27, 2007: 611.13, 2010: 600.45, 2013: 368.11, 2004: 419.31, 1990: 49.39, 1988: 47.22, 2002: 395.52,
           2001: 331.47, 2011: 515.99, 1998: 256.47, 2015: 264.44, 2012: 363.54, 2014: 337.05, 1992: 76.16, 1997:
               200.98, 1993: 45.98, 1994: 79.17, 1982: 28.86, 2003: 357.85, 1986: 37.07, 2000: 201.56, 1995: 88.11,
           2016: 70.93, 1991: 32.23, 1981: 35.77, 1987: 21.74, 1980: 11.38, 1983: 16.79, 2020: 0.29, 2017: 0.05}

    linechart_year(dic)
    piechart_developer({'Nintendo': (611.17, 22), 'Microsoft Game Studios': (21.82, 1),
                        'Take-Two Interactive': (74.74, 4)})
