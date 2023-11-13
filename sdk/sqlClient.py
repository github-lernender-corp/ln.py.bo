from os import environ
import pyodbc
#
# Modules
#
from model.user import User
#
# Get database connection
#
def GetConnection():
  #
  # Get the MongoDb Connection String
  #
  server = str(environ.get("MSSQL_SERVER"))
  database = str(environ.get("MSSQL_DATABASE"))
  user = str(environ.get("MSSQL_USERNAME"))
  password = str(environ.get("MSSQL_PASSWORD")) 
  #
  # If we have a valid url/database name
  #
  if (isinstance(server, str) and 
      isinstance(database, str) and
      isinstance(user, str) and
      isinstance(password, str)):
    #
    # Construct Connection String
    #
    connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={user};PWD={password};Encrypt=no;TrustServerCertificate=no;'
    #
    # Log the connection string and database
    #
    print(f'connectionString: {connectionString}') 
    #
    #   Return database connection string
    #
    return pyodbc.connect(connectionString)
  
  return None
#
# Get list of users
#
def QueryUser():
  users = []
  #
  # Get a connection
  #
  conn = GetConnection()
  #
  # Construct SQL Statement
  #  
  SQL_QUERY = """
    SELECT 
    x.First, x.Last 
    FROM [dbo].[User] x 
    ORDER BY  x.Last, x.First;
    """
  #
  # Get a cursor()
  #  
  cursor = conn.cursor()
  #
  # Execute Statement
  #
  cursor.execute(SQL_QUERY)
  #
  # Get all Rows
  #  
  rows = cursor.fetchall()
  for r in rows:
    users.append(User(r.First, r.Last))
  #
  # Close Cursor
  #
  cursor.close()
  #
  # Close Connection
  #  
  conn.close()
  #
  # Return Users
  #
  return users

#
# Get list of users
#
def UpdateUser(user):
  users = []
  #
  # Get a connection
  #
  conn = GetConnection()
  #
  # Construct SQL Statement
  #  
  SQL_QUERY = """
    UPDATE [dbo].[User] 
    SET First = ,
    Last = ;
    """
  #
  # Get a cursor()
  #  
  cursor = conn.cursor()
  #
  # Execute Statement
  #
  cursor.execute(SQL_QUERY)
  #
  # Get all Rows
  #  
  rows = cursor.fetchall()
  for r in rows:
    users.append(User(r.First, r.Last))
  #
  # Close Cursor
  #
  cursor.close()
  #
  # Close Connection
  #  
  conn.close()
  #
  # Return Users
  #
  return users