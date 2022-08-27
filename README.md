# surfs_up

## Overview
W. Avy is an investor in a new Surf n'Shake shop, serving surfboards and ice cream to locals and tourists in Oahu, Hawaii. The purpose of this analysis is to gather temperature data for the months of June and December in Oahu, to determine if this business venture is sustainable year-round based on weather criteria.

## Resources
### Data Source 
- [hawaii.sqlite](https://github.com/lkachury/surfs_up/blob/main/hawaii.sqlite) database file

### Software
- Python 3.7.6
- Conda 4.13.0
- Visual Studio Code 1.69
- SQLite and SQLAlchemy
- Jupyter Notebook
- Dependencies:
  - Python JSON Library
  - Python Pandas Library
  - Python Numpy Library
  - sqlalchemy Module 
  - psycopg2 Module

## Results 
The full Jupyter Notebook for these deliverables can be referenced here: [SurfsUp_Challenge.ipynb](https://github.com/lkachury/surfs_up/blob/main/SurfsUp_Challenge.ipynb)

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

- The average temperature in June is roughly 75 while the average temperature in December is roughly 71. The difference in these temperatures is almost 4 degrees. June has a smaller standard deviation than December, so most of their data is centered around 75 degrees in June while only a small portion of the data in centered around 71 degrees in December. 
- The maximum temperature in June is 85 while the maximum temperature in December is 83. The difference in temperature is 2 degrees. The max temperature in June was closer to its average temperature than in December. 
- The minimum temperature in June is 64 while the minimum temperature in December is 56. The difference in these temperatures is 8 degrees. December has more temperatures near their minimum than June, which means that temperatures are lower more in December than in June. 

## Summary
Based on the summary statistics generated, the difference in metrics between June and December temperatures are minimal. However, December has almost 200 less reported temperatures than June. June has a smaller standard deviation than December, which means it has less variability in its temperatures and has more days around warmer weather. 

Two additional queries that we can perform to gather more weather data for June and December is to collect the summary statistics for precipitation data.

The following code describes the working query to retrieve the June precipitation summary statistics:
<br /> ![image](https://user-images.githubusercontent.com/108038989/187013894-730d1647-9139-4b01-8923-0ec887e6f91e.png)

The following code describes the working query to retrieve the December precipitation summary statistics:
<br /> ![image](https://user-images.githubusercontent.com/108038989/187013927-4d4e0e53-7bd5-48a0-8122-f6bdf5dc41ca.png)
