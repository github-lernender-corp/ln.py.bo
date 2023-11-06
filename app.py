
from flask import Flask, Response, request, json, jsonify, make_response, render_template
from werkzeug.exceptions import HTTPException
from dotenv import load_dotenv
from bson.json_util import dumps
from bson.objectid import ObjectId
import logging
#
# Modules
#
from sdk.mongo import GetDatabase
#
# Setup Logging
#
logging.basicConfig(level=logging.DEBUG)
#
# Load the environment information
#
load_dotenv()
#
# Setup Api app
#
app = Flask(__name__)
#
# Get a handle to the database
#
database = GetDatabase()
#
# Http(Get) Home
#
@app.get("/")
def getHome():
  #
  # Log Route
  #    
  app.logger.info("Route: /")
  #
  # Get information
  #
  info = list(database.info.find({}))  
  #
  # Return Home Page
  #
  return render_template("home.html", data=info[0])
#
# Setup Http(Put) sensor information
#
@app.get("/sensor")
def getSensor():
  #
  # Get Sensor Data
  #
  _data = list(database.sensor.find({}))
  #
  # Return Home Page
  #
  return render_template("sensor.html", data=_data)  
  #
  # Return HttpResponse Object with info.
  #
  #return Response(dumps(_data), status=200,  mimetype="application/json")

#
# Setup Http(Get) Info
#
@app.get("/api/info")
def getInfo():
  #
  # Log Route
  #    
  app.logger.info("Route: /api/info")
  #
  # Get information
  #
  info = list(database.info.find({}))
  #
  # Return HttpResponse Object with info.
  #
  return Response(dumps(info), status=200,  mimetype="application/json")

#
# Setup Http(Put) sensor information
#
@app.put("/api/sensor")
def putSensor():
  #
  # Get sensor Id
  #
  id = request.args.get('id')
  #
  # Destructor json payload
  #
  _data = request.json
  #
  # Update the sensor data
  #
  database.sensor.update_one({"_id": ObjectId(id)}, {"$set": _data})
  #
  # Return HttpResponse Object with info.
  #
  return Response(dumps(_data), status=200,  mimetype="application/json")
  
#
# Error Handling for Response Codes
#
@app.errorhandler(HTTPException)
def errorHandler(e):
    """Return JSON for HTTP errors."""
    #
    # Get Response
    #
    resp = e.get_response()
    resp.content_type = "application/json"
    #
    # Construct JSON Body
    #
    resp.data = json.dumps({
        "name": e.name,
        "description": errorCodeMessage(e.code),
        "code": e.code
    })
    #
    # Log Error
    #  
    app.logger.error(jsonify(resp.data));
    #
    # Return Response
    #
    return resp

#
# GetErrorCodeMessage
#
def errorCodeMessage(code):
    """Return more descriptive error code."""
    if code == 400:
        return "Bad request!"
    elif code == 404:
        return "Resource not found!"
    elif code == 500:
        return "Internal Server Error"
    else:
        return "Unknown error!"
      
      
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=int("5000"), debug=True)