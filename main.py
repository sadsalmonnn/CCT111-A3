"""
Author: Solomon James Ador-Dionisio
Filename: main.py
Date: 08/05/24
Description: In this module, the main function is defined, where data is read from "video_games_sales.csv" and outputted
into different forms including line-charts, and pie-charts. This data is in the form of publisher, year, region, genre,
and platform.
"""
from dictparse import *
from graph import *


def main():
    """
    Main function to produce graphs and read data using dictparse and graph modules.
    """
    filename = "video_games_sales.csv"
    publisher, year, region, genre, platform = read(filename)

    linechart_year(year)
    piechart_developer(publisher)
    piechart_reg(region)
    piechart_reg(genre)
    piechart_platform(platform)


if __name__ == "__main__":
    main()
