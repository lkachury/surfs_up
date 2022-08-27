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
The full Jupyter Notebook for these deliverables can be referenced here: [SurfsUp_Challenge.ipynb]()

### Deliverable 1: Determine the Summary Statistics for June
Using Python, Pandas functions and methods, and SQLAlchemy, the date column of the Measurements table in the hawaii.sqlite database was filtered to retrieve all the temperatures for the month of June, the June temperatures were converted to a list, a DataFrame was created from the list, and the summary statistics were generated.

A working query was written to retrieve the June temperatures from the date column of the Measurement table:
<br /> ![image](https://user-images.githubusercontent.com/108038989/187010769-f6571ea5-9bb5-4612-b793-6e26986a47dc.png)

The June temperatures were added to a list: 
<br /> ![image](https://user-images.githubusercontent.com/108038989/187010778-9012fb8b-ace3-40c5-ad9c-3fecafe19bd7.png)

The list of June temperatures was converted to a Pandas DataFrame: 
<br /> ![image](https://user-images.githubusercontent.com/108038989/187010432-c486fd2d-2e54-44fa-b243-7d03987601cc.png)
 
Summary statistics were generated for the DataFrame: 
<br /> ![image](https://user-images.githubusercontent.com/108038989/187010464-4bfc3c80-48e9-4f36-87c9-dceaf343b928.png)

### Deliverable 2: Determine the Summary Statistics for December
Using Python, Pandas functions and methods, and SQLAlchemy, the date column of the Measurements table in the hawaii.sqlite database was filtered to retrieve all the temperatures for the month of December, the December temperatures were converted to a list, a DataFrame was created from the list, and the summary statistics were generated.

A working query was written to retrieve the December temperatures from the date column of the Measurement table: 
<br /> ![image](https://user-images.githubusercontent.com/108038989/187010929-d6956f7a-dfd3-4df6-96cf-cdcfb7902933.png)

The December temperatures were added to a list: 
<br /> ![image](https://user-images.githubusercontent.com/108038989/187010967-82d88eb4-7af8-4ff5-b6ca-09a8f0e36ad4.png)

The list of December temperatures was converted to a Pandas DataFrame: 
<br /> ![image](https://user-images.githubusercontent.com/108038989/187010980-db1c51cb-c412-40d8-aaeb-9cd4ece93e94.png)

Summary statistics were generated for the DataFrame:
<br /> ![image](https://user-images.githubusercontent.com/108038989/187010991-c38bae50-b2d3-48f8-95df-1706a34d7d34.png)

### Three key differences in weather between June and December
To better understand the difference in temperature between the two months, each month was plotted on a histogram:
<br /> ![image](https://user-images.githubusercontent.com/108038989/187011347-07cebeb5-4251-40d6-9c48-5c85e51e94e2.png)![image](https://user-images.githubusercontent.com/108038989/187011389-1351cb99-4a6e-4eca-93ff-51be04ed955f.png)

- ?
- ?
- ?

## Summary
Provide a high-level summary of the results and two additional queries that you would perform to gather more weather data for June and December.
