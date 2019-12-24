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

#Flask Setup
app = Flask(__name__)

#Flask Routes

@app.route("/")
def welcome():
    """List of all the available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/Measurements<br/>"
        f"/Stations"
    )

if __name__ == '__main__':
    app.run(debug=True)