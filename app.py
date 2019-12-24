import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

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


if __name__ == '__main__':
    app.run(debug=True)