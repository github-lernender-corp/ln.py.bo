## Api Application

### Overview
This demo Python application is designed to show how a developer can create an API application that can be host within AWS.

### Prerequisites
* Python (Python 3.11.4)
* Pip3 (pip 23.1.2 >)
  * pip3 install --upgrade pip
* Python Virtual Env
  * python3 -m venv {bo}
  * source bo/bin/activate (activates virtual environment)
* Mac/Linux OS

### Installation Instructions

1. pip3 install -r requirements.txt

### mongoDb COmmands

1. mongosh start mongodb
2. vi /opt/homebrew/etc/mongod.conf


### Docker Build Command

> docker build -t lernender/ln.py.bo .
> docker run -d -it --name ln_py_bo -p 5000:5000 -p 27017:27017 --net=host lernender/ln.py.bo:latest


### DynamoDb Resource

1. [AWS DynamoDb Resource](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html)
2. [Python Template Example](https://flask.palletsprojects.com/en/1.1.x/patterns/templateinheritance/)
