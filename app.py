# Set Up the Flask Weather App

# Import dependencies
import datetime as dt
import numpy as np
import pandas as pd
# Import dependencies for SQLAlchemy, which will help us access our data in the SQLite database. 
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
#  Import the Flask dependency
from flask import Flask, jsonify

# Set Up the Database
# access the SQLite database 
engine = create_engine("sqlite:///hawaii.sqlite")
# Reflect the database
Base = automap_base()
Base.prepare(engine, reflect=True)
# save the references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create a session link from Python to the database 
session = Session(engine)

# Set Up Flask
# create a Flask application called "app."
app = Flask(__name__)

#Create the Welcome Route
# define the welcome route
@app.route("/")
# create the welcome() function
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Precipitation Route
# create the route
@app.route("/api/v1.0/precipitation")
# create the precipitation() function
def precipitation():
    # add the line of code that calculates the date one year ago from the most recent date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # write a query to get the date and precipitation for the previous year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    # create a dictionary with the date as the key and the precipitation as the value
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

# Stations Route  
# create the route
@app.route("/api/v1.0/stations")
# create a new function called stations()
def stations():
    # create a query that will allow us to get all of the stations in our database
    results = session.query(Station.station).all()
    # convert our unraveled results into a list
    stations = list(np.ravel(results))
    # jsonify the list and return it as JSON
    return jsonify(stations=stations)

# Monthly Temperature Route
# create the route
@app.route("/api/v1.0/tobs")
# create a new function called temp_monthly()
def temp_monthly():
    # calculate the date one year ago from the last date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    # query the primary station for all the temperature observations from the previous year
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    # unravel the results into a one-dimensional array and convert that array into a list
    temps = list(np.ravel(results))
    # jsonify the list and return our results
    return jsonify(temps=temps)

# Statistics Route
# create the routes
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
# create a function called stats() and add parameters
def stats(start=None, end=None):
    # create a query to select the minimum, average, and maximum temperatures from our SQLite database
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    # add an if-not statement to determine the starting and ending date
    if not end:
        # query our database using the list that we just made
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        # unravel the results into a one-dimensional array and convert them to a list
        temps = list(np.ravel(results))
        # jsonify our results and return them
        return jsonify(temps)
    # calculate the temperature minimum, average, and maximum with the start and end dates
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)