## BO Api Rest Example

### Overview
This demo Python application is designed to show how a developer can create an Rest API  that can be host within AWS to server data stemming from a database (i.e. MongoDb, SQl Server, DynamoDb etc.).

### Prerequisites
* Python (Python 3.11.4)
* Pip3 (pip 23.1.2 >)
  * pip3 install --upgrade pip
* Python Virtual Env
  * python3 -m venv {bo}
  * source bo/bin/activate (activates virtual environment)
* Mac/Linux OS

### Installation Instructions

1. setup virtual environment (see above)
2. pip3 install -r requirements.txt


More information...
> [Python SQL Driver - pyodbc](https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/python-sql-driver-pyodbc?view=sql-server-ver16)

### Microsoft Sql Server Installation

#### Mac

1. pip install --pre --no-binary :all: pyodbc

##### Troubleshooting:

* Choosing correct Python Interpreters (vscode)

* (Ctl+Shift+P) python
* Choose the correct interpreter

## Supported Databases

### Microsoft SQL Server

1. AWS Setup RDS Database (connection string information will be provided by AWS)
2. Create database on RDS Database Server
3. Test Connection
4. Follow database example under /sdk/sqlClient.py

### mongoDb (mac)

1. Install Mongodb Community Edition (for your OS)
2. mongosh start mongodb
3. vi /opt/homebrew/etc/mongod.conf

### DynamoDb

1. [AWS DynamoDb Resource](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html)
2. [Python Template Example](https://flask.palletsprojects.com/en/1.1.x/patterns/templateinheritance/)


## Docker Image/Container

### Docker Build Command

> docker build -t lernender/ln.py.bo .
> docker run -d -it --name ln_py_bo -p 5000:5000 -p 27017:27017 --net=host lernender/ln.py.bo:latest