
from flask import Flask, Response, request, json, jsonify, make_response, render_template
from werkzeug.exceptions import HTTPException
from dotenv import load_dotenv
import logging
#
# Modules
#
from sdk.sqlClient import QueryUser
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
# Http(Get) Home
#
@app.get("/")
def getHome():
    #
    # Return Home Page
    #
    return render_template("home.html", data={})
#
# Http(Get) sensor information
#
@app.get("/team")
def getTeam():
    #
    # Get User Data
    #
    users = QueryUser()
    #
    # Return Home Page
    #
    return render_template("team.html", len=len(users), data=users)

#
# Http(Get) sensor information
#
@app.get("/sensor")
def getSensor():
    #
    # Get Sensor Data
    #
    data = [] #QuerySensor()
    #
    # Return Home Page
    #
    return render_template("sensor.html", len=len(data), data=data)

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
    app.logger.error(jsonify(resp.data))
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
