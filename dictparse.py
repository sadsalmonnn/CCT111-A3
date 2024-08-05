"""
Author: Cindy Zheng
Filename: dictparse.py
Date: 08/05/24
Description: In this module, the function read was defined. read takes in data from a csv file,
namely video_games_sales.csv.
"""
import csv


def read(filename: str):
    """

    Parameter:
    filename -- csv file to be read from, video_games_sales.csv to be specific

    Return:
    publisher -- a dictionary containing the publisher name, a list containing their total sales, and number of games
    year -- a dictionary containing the year and amount of games released that year
    region -- a dictionary containing the different regions and the total amount of sales for that region
    genre -- a dictionary containing the different genres and the total amount of sales for that genre
    platform -- a dictionary containing the different platforms and the total amount of sales for that platform
    """

    # publisher name: [total sale, # of games]
    publisher = {}

    # year: # of games
    year = {}

    # region: total sales
    region = {"NA": 0.0, "EU": 0.0, "JP": 0.0, "OTHER": 0.0}

    # genre: total sales
    genre = {}

    # platform: total sales
    platform = {}

    with open(filename, "r") as file:
        csv_file = csv.reader(file)

        # The csv file is opened as an object and the header is skipped
        header = next(csv_file)

        # Loops through each line in the csv file
        for line in csv_file:

            # Adds the publisher to the publisher dictionary
            if line[5] not in publisher:
                publisher[line[5]] = [0.0, 0]

            # Adds and calculates the total sales and total games
            publisher[line[5]] = [round(publisher[line[5]][0] + float(line[10]), 2), publisher[line[5]][1] + 1]

            # Try-except is used to ensure empty years are skipped
            try:
                # Adds the year to the year dictionary
                if int(float(line[3])) not in year:
                    year[int(float(line[3]))] = 0.0

                # Adds and calculates the total sales and total games
                year[int(float(line[3]))] = round(year[int(float(line[3]))] + float(line[10]), 2)
            except ValueError:
                continue

            # Adds and calculates the total sales for each region
            region["NA"] = round(region["NA"] + float(line[6]), 2)
            region["EU"] = round(region["EU"] + float(line[7]), 2)
            region["JP"] = round(region["JP"] + float(line[8]), 2)
            region["OTHER"] = round(region["OTHER"] + float(line[9]), 2)

            # Adds the genre to the genre dictionary
            if line[4] not in genre:
                genre[line[4]] = 0.0

            # Adds and calculates the total sales for each genre
            genre[line[4]] = round(genre[line[4]] + float(line[10]), 2)

            # Adds the genre to the platform dictionary
            if line[2] not in platform:
                platform[line[2]] = 0.0

            # Adds and calculates the total sales for each platform
            platform[line[2]] = round(platform[line[2]] + float(line[10]), 2)

    # Once the entire csv file is read, the dictionaries are returned
    return publisher, year, region, genre, platform


if __name__ == "__main__":
    # Testing
    filename_ = "video_games_sales.csv"
    # filename_ = "Test.csv"

    publisher_, year_, region_, genre_, platform_ = read(filename_)

    # print(publisher_)
    # print(year_)
    # print(region_)
    # print(genre_)
    # print(platform_)
