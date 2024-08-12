"""
Author: Cindy Zheng and Solomon James Ador-Dionisio
Filename: main.py
Date: 08/05/24
Description: In this module, the main function is defined, where data is read
from "video_games_sales.csv" and outputted into different forms including
line-charts, and pie-charts. This data is in the form of publisher, year,
region, genre, and platform.
"""
from dictparse import *
from graph import *


def main():
    """
    Main function to produce graphs and read data using dictparse and graph
    modules.
    """
    filename = "video_games_sales.csv"

    # Data is extracted from the csv file
    publisher, year, region, genre, platform = read(filename)

    # The functions take input on the data, the required title, and axis labels
    # where necessary, to output a graph
    linechart_year(year, "Total Sales Per Year in the Gaming Industry",
                   "Year", "Total Sales ($ Millions)")
    piechart_developer(publisher, "Average Sale Per Publisher")
    piechart_region(region, "Total Sales Per Region")
    piechart_genre(genre, "Total Sales Per Genre")
    bargraph_platform(platform, "Total Sales Per Platform", "Platforms",
                      "Sales ($ Millions)")


if __name__ == "__main__":
    main()
