"""
Author: Cindy Zheng and Solomon James Ador-Dionisio
Filename: graph.py
Date: 08/05/24
Description: In this module, the function sort_dic, convertdata_list,
linechart_year, piechart_developer, piechart_reg, and piechart_platform were
created. The first two functions are used to sort and configure the data given,
in the form of dictionaries. Linechart_year, piechart_developer, piechart_reg,
and piechart_platform are used to display graphs and calculate certain pieces of
data specifically from the csv file, video_games_sales.csv.
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
    Takes <dic_> and returns two parallel lists one being the keys and the other
    being the values.

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
    Takes <dic_>, sorts it, plots the data to a line-graph, and displays the
    graph.

    Parameter:
    dic_ -- dictionary of any values
    title -- title of the graph
    axisx -- label for the x-axis
    axisy -- label for the y-axis
    """
    # Prepares the data
    x, y = convertdata_list(sort_dic(dic_))

    # Creates the figure with the correct size
    f = matplotlib.pyplot.figure()
    f.set_figwidth(8)
    f.set_figheight(5)
    ax = f.add_subplot()

    # Plots the data on a line-graph
    matplotlib.pyplot.plot(x, y, color='pink')

    # Generates the appropriate labels, colors them accordingly for 'PPT'
    matplotlib.pyplot.title(title, fontsize='18', fontweight='bold',
                            color='white')
    matplotlib.pyplot.xlabel(axisx, fontsize='16', fontweight='bold',
                             color='white')
    matplotlib.pyplot.ylabel(axisy, fontsize='16', fontweight='bold',
                             color='white')
    matplotlib.pyplot.yticks(fontsize='15', color='white')
    matplotlib.pyplot.xticks(fontsize='15', color='white')
    ax.tick_params(axis='x', color='white')
    ax.tick_params(axis='y', color='white')
    ax.spines['left'].set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['top'].set_color('white')

    # Saves picture for 'PPT'
    matplotlib.pyplot.savefig('year_ppt.png', transparent=True,
                              bbox_inches='tight', dpi=200)

    # Reverses the colors to black for general display/report
    matplotlib.pyplot.title(title, fontsize='18', fontweight='bold',
                            color='black')
    matplotlib.pyplot.xlabel(axisx, fontsize='16', fontweight='bold',
                             color='black')
    matplotlib.pyplot.ylabel(axisy, fontsize='16', fontweight='bold',
                             color='black')
    matplotlib.pyplot.yticks(fontsize='15', color='black')
    matplotlib.pyplot.xticks(fontsize='15', color='black')
    ax.tick_params(axis='x', color='black')
    ax.tick_params(axis='y', color='black')
    ax.spines['left'].set_color('black')
    ax.spines['bottom'].set_color('black')
    ax.spines['right'].set_color('black')
    ax.spines['top'].set_color('black')

    # Saves picture for 'Report'
    matplotlib.pyplot.savefig('year_report.png', transparent=True,
                              bbox_inches='tight', dpi=200)

    # Displays the graph for 'Report'
    matplotlib.pyplot.show()


def piechart_developer(dic_, title):
    """
    Takes <dic_>, sorts it, calculates the average sale for each developer,
    displays it to a pie-chart in comparison to other developers.

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

    # Calculates the average sale for each developer by taking the total sales
    # divided by the total amount of games published
    avg_y = [(z[0]) / z[1] for z in y]

    # Custom colours
    color = ["#F8C0C8", "#EFE7D3", "#D3BBDD", "#ECE3F0"]

    # Creates the figure with the correct size
    f = matplotlib.pyplot.figure()
    f.set_figwidth(15)
    f.set_figheight(10)

    # Plots the calculated data onto a pie-chart
    chunk, label = matplotlib.pyplot.pie(avg_y, labels=x,
                                         wedgeprops={'linewidth': 3.0,
                                                     'edgecolor': 'white'},
                                         textprops={'size': 'medium'},
                                         colors=color,
                                         explode=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                                  0, 0, 0, 0, 0.0678, 0, 0, 0,
                                                  0, 0, 0, 0, 0, 0, 0, 0])

    # Customizes the chart for 'PPT'
    matplotlib.pyplot.title(title, fontsize='18', color='white',
                            fontweight='bold')
    matplotlib.pyplot.setp(label, color='white', fontweight='bold')

    # Saves the chart for 'PPT'
    matplotlib.pyplot.savefig('developer_ppt.png', transparent=True,
                              bbox_inches='tight')

    # Reverses the colors to black for general display/report
    matplotlib.pyplot.title(title, fontsize='18', color='black',
                            fontweight='bold')
    matplotlib.pyplot.setp(label, color='black', fontweight='normal')

    # Saves the chart for 'Report'
    matplotlib.pyplot.savefig('developer_report.png', transparent=True,
                              bbox_inches='tight')

    # Displays the graph for 'Report'
    matplotlib.pyplot.show()


def piechart_genre(dic_, title):
    """
    Takes <dic_>, sorts the data accordingly, displays it to a pie-chart

    Parameter:
    dic_ -- dictionary of any values
    title -- title of the graph
    """
    # Prepares the data
    x, y, = convertdata_list(dic_)

    # Custom colours
    color = ["#5D59AF", "#A072BE", "#BE81B6", "#E390C8"]

    # Plots the calculated data onto a pie-chart
    chunk, label = matplotlib.pyplot.pie(y, labels=x,
                                         wedgeprops={'linewidth': 3.0,
                                                     'edgecolor': 'white'},
                                         textprops={'size': 'x-large'},
                                         colors=color,
                                         explode=[0, 0, 0, 0, 0, 0, 0, 0, 0.07,
                                                  0, 0, 0])

    # Customizes the chart for 'PPT'
    matplotlib.pyplot.title(title, fontsize='18', color='black',
                            fontweight='bold')
    matplotlib.pyplot.setp(label, color='white', fontweight='normal')
    matplotlib.pyplot.title(title, fontsize='18', color='white',
                            fontweight='bold')

    # Saves the chart for 'PPT'
    matplotlib.pyplot.savefig('genre_ppt.png', transparent=True,
                              bbox_inches='tight', dpi=200)

    # Reverses the colors to black for general display/report
    matplotlib.pyplot.setp(label, color='black', fontweight='normal')
    matplotlib.pyplot.title(title, fontsize='18', color='black',
                            fontweight='bold')

    # Saves the chart for 'Report'
    matplotlib.pyplot.savefig('genre_report.png', transparent=True,
                              bbox_inches='tight')

    # Displays the graph for 'Report'
    matplotlib.pyplot.show()


def piechart_region(dic_, title):
    """
    Takes <dic_>, sorts the data accordingly, displays it to a pie-chart

    Parameter:
    dic_ -- dictionary of any values
    title -- title of the graph
    """
    # Prepares the data
    x, y, = convertdata_list(dic_)

    # Custom colours
    color = ['#BEC3EA', '#D7C8E9', '#DFC3E3', '#E7B5D3']

    # Plots the calculated data onto a pie-chart
    # autopct: generate percentage to 1 decimal
    # wedgeprops: creates a space between each chunk
    # textprops: makes the words larger
    # colors: changes the chunk colors
    # explode: pops out one slice
    chunk, label, number = matplotlib.pyplot.pie(y, labels=x, autopct='%.1f%%',
                                                 wedgeprops={'linewidth': 3.0,
                                                             'edgecolor':
                                                                 'white'},
                                                 textprops={'size': 'x-large'},
                                                 colors=color,
                                                 explode=[0.01, 0, 0, 0])

    # Customizes the graph for 'PPT'
    matplotlib.pyplot.title(title, fontsize='18', color='white',
                            fontweight='bold')
    matplotlib.pyplot.setp(number, color='white', fontweight='bold')
    for i in range(len(label)):
        matplotlib.pyplot.setp(label[i], color=color[i], fontweight='bold')

    # Saves the graph for 'PPT'
    matplotlib.pyplot.savefig('region_ppt.png', transparent=True,
                              bbox_inches='tight')

    # Reverses the colors to black for general display/report
    matplotlib.pyplot.title(title, fontsize='18', color='black',
                            fontweight='bold')
    matplotlib.pyplot.setp(number, color='black', fontweight='normal')

    # Saves the graph for 'Report'
    matplotlib.pyplot.savefig('region_report.png', transparent=True,
                              bbox_inches='tight')

    # Displays the graph for 'Report'
    matplotlib.pyplot.show()


def bargraph_platform(dic_, title, axisx, axisy):
    """
    Takes <dic_>, sorts the data accordingly, displays it to a bargraph in
    comparison to other platforms.

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

    # Creates the figure with the correct size
    f = matplotlib.pyplot.figure()
    f.set_figwidth(15)
    f.set_figheight(10)
    ax = f.add_subplot()

    # Custom colours
    color = ["#FF5353", "#FF7979", "#FFA5A5"]

    # Plots the data onto a bargraph
    matplotlib.pyplot.bar(x, height=y, color=color)

    # Generates the appropriate labels and colors them accordingly for ppt
    matplotlib.pyplot.title(title, fontsize='18', fontweight='bold',
                            color='white')
    matplotlib.pyplot.xlabel(axisx, fontsize='16', fontweight='bold',
                             color='white')
    matplotlib.pyplot.ylabel(axisy, fontsize='16', fontweight='bold',
                             color='white')
    matplotlib.pyplot.yticks(fontsize='15', color='white')
    matplotlib.pyplot.xticks(fontsize='15', color='white')
    ax.tick_params(axis='x', color='white')
    ax.tick_params(axis='y', color='white')
    ax.spines['left'].set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['top'].set_color('white')

    # Saves the chart for 'PPT'
    matplotlib.pyplot.savefig('platform_ppt.png', transparent=True,
                              bbox_inches='tight')

    # Reverses the colors to black for general display/report
    matplotlib.pyplot.title(title, fontsize='18', fontweight='bold',
                            color='black')
    matplotlib.pyplot.xlabel(axisx, fontsize='16', fontweight='bold',
                             color='black')
    matplotlib.pyplot.ylabel(axisy, fontsize='16', fontweight='bold',
                             color='black')
    matplotlib.pyplot.yticks(fontsize='15', color='black')
    matplotlib.pyplot.xticks(fontsize='15', color='black')
    ax.tick_params(axis='x', color='black')
    ax.tick_params(axis='y', color='black')
    ax.spines['left'].set_color('black')
    ax.spines['bottom'].set_color('black')
    ax.spines['right'].set_color('black')
    ax.spines['top'].set_color('black')

    # Saves the chart for 'Report'
    matplotlib.pyplot.savefig('platform_report.png', transparent=True,
                              bbox_inches='tight')

    # Displays the graph for 'Report'
    matplotlib.pyplot.show()
