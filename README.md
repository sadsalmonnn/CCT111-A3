# Video Games Sales Analysis

**Authors:** Cindy Zheng and Solomon James Ador-Dionisio  
**Date:** August 5, 2024

---

## Overview

This project analyzes video game sales data from the `video_games_sales.csv` dataset. It extracts sales information by publisher, year, region, genre, and platform, then generates visualizations such as line charts, pie charts, and bar graphs to provide insights into the video game industry's sales trends.

---

## Features

- Reads and processes a CSV dataset of video game sales.
- Generates multiple graphs to visualize sales data:
  - Total sales per year (line chart)
  - Average sales per publisher (pie chart)
  - Total sales by region (pie chart)
  - Total sales by genre (pie chart)
  - Total sales by platform (bar graph)
- Saves charts optimized for both presentations (PPT) and reports.

---

## File Structure

- `main.py`  
  Main script to run the analysis and generate graphs.

- `dictparse.py`  
  Contains the `read` function that parses the CSV data and returns dictionaries for different sales metrics.

- `graph.py`  
  Contains functions for sorting data and generating different types of charts using `matplotlib`.

- `video_games_sales.csv`  
  Dataset containing sales data (not included in the repo).
