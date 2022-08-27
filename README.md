# surfs_up

## Overview

"W. Avy likes your analysis, but he wants more information about temperature trends before opening the surf shop. Specifically, he wants temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round."

## Resources
### Data Source 
- hawaii.sqlite database []()

### Software
- Python 3.7.6
- Conda 4.13.0
- Visual Studio Code 1.69
- Dependencies:
  - Python JSON Library
  - Python Pandas Library
  - Python Numpy Library
  - sqlalchemy Module 
  - psycopg2 Module

## Results 
The full Jupyter Notebook for these deliverable can be referenced here: [SurfsUp_Challenge.ipynb]()

### Deliverable 1: Determine the Summary Statistics for June
Using Python, Pandas functions and methods, and SQLAlchemy, the date column of the Measurements table in the hawaii.sqlite database was filtered to retrieve all the temperatures for the month of June. The June temperatures were converted to a list, a DataFrame was created from the list, and the summary statistics were generated.

A working query was written to retrieve the June temperatures from the date column of the Measurement table:
<br /> ![image](https://user-images.githubusercontent.com/108038989/187010353-df075d89-0cfa-4521-b3bb-262b4b22075e.png)

The June temperatures were added to a list: 
<br /> ![image](https://user-images.githubusercontent.com/108038989/187010407-1608933a-895b-4603-8779-2ac47773312b.png)

The list of June temperatures was converted to a Pandas DataFrame: 
<br /> ![image](https://user-images.githubusercontent.com/108038989/187010432-c486fd2d-2e54-44fa-b243-7d03987601cc.png)
 
Summary statistics were generated for the DataFrame: 
<br /> ![image](https://user-images.githubusercontent.com/108038989/187010464-4bfc3c80-48e9-4f36-87c9-dceaf343b928.png)



### Deliverable 2: Determine the Summary Statistics for December
Using Python, Pandas functions and methods, and SQLAlchemy, you’ll filter the date column of the Measurements table in the hawaii.sqlite database to retrieve all the temperatures for the month of December. You’ll then convert those temperatures to a list, create a DataFrame from the list, and generate the summary statistics.

- A working query is written to retrieve the December temperatures from the date column of the Measurement table (10 pt)
- The temperatures are added to a list. (10 pt)
- The list of temperatures is converted to a Pandas DataFrame. (10 pt)
- Summary statistics are generated for the DataFrame. (10 pt)


There is a bulleted list that addresses the three key differences in weather between June and December.


## Summary
Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December.
