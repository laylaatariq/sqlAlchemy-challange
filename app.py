import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt

#Getting the database
engine = create_engine("sqlite:///Resources//hawaii.sqlite")

base = automap_base()

base.prepare(engine, reflect=True)

Measurement = base.classes.measurement
Station = base.classes.station

#Create a session link
session = Session(engine)

#Flask Setup
app = Flask(__name__)

#Flask Routes

@app.route("/")
def welcome():
    """List of all the available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/Measurements<br/>"
        f"//api/v1.0/stations<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/startDate<br/>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/Measurements")
def measurements():

    #Query all the results
    results = session.query(Measurement.id, Measurement.station, Measurement.date, Measurement.prcp, Measurement.tobs)

    #Closing the session
    session.close()

    #Creating a dictionary with the measurement table results
    data_measurements = []
    for id, station, date, prcp, tobs in results:
        measurements_dict = {}
        measurements_dict["id"] = id
        measurements_dict['station'] = station
        measurements_dict['date'] = date
        measurements_dict['precipitation'] = prcp
        measurements_dict['temperature'] = tobs
        data_measurements.append(measurements_dict)

    return jsonify(data_measurements)    

@app.route("/api/v1.0/stations")
def stations():  

    #Query all the results
    results = session.query(Station.id, Station.station, Station.name, Station.longitude, Station.latitude, Station.elevation)

    #Closing the session
    session.close()

    #Creating a dictionary with the measurement table results
    data_station = []
    station_dict = {}
    for id, station, name, longitude, latitude, elevation in results:
        station_dict['id'] = id
        station_dict['station'] = station
        station_dict['name'] = name
        station_dict['longitude'] = longitude
        station_dict['latitude'] = latitude
        station_dict['elevation'] = elevation
        data_station.append(station_dict)

    return jsonify(data_station)

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    #Query all the results
    results = session.query(Measurement.date, Measurement.prcp).all()

    #Close the session
    session.close()

    #Creating a dictionary
    data_prcp = []
    prcp_dict = {'date' : 'prcp'}
    for date, prcp in results:
        prcp_dict = {date : prcp}
        data_prcp.append(prcp_dict)

    return jsonify(data_prcp)

@app.route("/api/v1.0/tobs")
def tobs():

    #Query the results
    results = session.query(Measurement.tobs, Measurement.date).\
        filter(func.strftime("%Y-%m-%d", Measurement.date) >= "2016-08-23").\
        order_by((func.strftime("%Y-%m-%d", Measurement.date)).desc()).all()

    #Close the sesiion
    session.close()

    #Creating the dictionary
    data_tobs = []
    tobs_dict = {}
    for tobs, date in results:
        tobs_dict['date'] = date
        tobs_dict['temperature'] = tobs
        data_tobs.append(tobs_dict)

    return jsonify(data_tobs)

@app.route("/api/v1.0/<start>")
def byDate(start):

    #Changing the input to date format
    # startDate = dt.datetime.strptime(start, "%Y-%m-%d")

    #Querying the resuls
    results =  session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs) ).\
                filter((func.strftime("%Y-%m-%d", Measurement.date) >= start)).all()

    data_stats = []
    stats_dict = {}
    for minTemp, maxTemp, AvgTemp in results:
        stats_dict['Minimum Temperature'] = minTemp
        stats_dict['Maximum Temperature'] = maxTemp
        stats_dict['Average Temperature'] = AvgTemp
        data_stats.append(stats_dict)

    return jsonify(data_stats)

@app.route("/api/v1.0/<start>/<end>")
def inBetween(start, end):

    #Changing the input to date format
    # startDate = dt.datetime.strptime(start, "%Y-%m-%d")

    #Querying the resuls
    results =  session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs) ).\
                filter((func.strftime("%Y-%m-%d", Measurement.date) >= start)).\
                filter((func.strftime("%Y-%m-%d", Measurement.date) <= end)).all()

    new_stats = []
    new_dict = {}
    for minTemp, maxTemp, AvgTemp in results:
        new_dict['Minimum Temperature'] = minTemp
        new_dict['Maximum Temperature'] = maxTemp
        new_dict['Average Temperature'] = AvgTemp
        new_stats.append(new_dict)

    return jsonify(new_stats)

if __name__ == '__main__':
    app.run(debug=True)