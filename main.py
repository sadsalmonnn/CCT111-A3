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

    linechart_year(year, "Total Sales per Year in the Gaming Industry", "Year", "Total Sales ($ Millions)")
    piechart_developer(publisher, "Average Sale for each Publisher in Comparison")
    piechart_reg(region, "Total Sales for each Region in Comparison")
    piechart_reg(genre, "Total Sales for each Genre in Comparison")
    bargraph_platform(platform, "Total Sales on each Platform", "Platforms", "Sales ($ Millions)")


if __name__ == "__main__":
    main()
