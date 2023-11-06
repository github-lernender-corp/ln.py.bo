import os
from pymongo import MongoClient as Mongo
#
# Get a handle to the database
#
def GetDatabase():

  #
  # Get the MongoDb Connection String
  #
  url = str(os.environ.get("MONGO_CONNECTION_STRING"))
  #
  # Get the MongoDb Connection String
  #
  database = str(os.environ.get("MONGO_DATABASE"))
  #
  # If we have a valid url/database name
  #
  if (isinstance(url, str) and isinstance(database, str)): 
    #
    # Log the connection string and database
    #
    print(f'MongoConStr: {url}')    
    print(f'Database: {database}')    
    #
    # Get a handle to the mongo client.
    #
    client = Mongo(url)
    #
    # Return handle to the database
    #
    return client[database]

  return None
  