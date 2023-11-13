from os import environ
import pyodbc
#
# Modules
#
from model.user import User
  
#
# Get a handle to the database
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

    connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={user};PWD={password};Encrypt=no;TrustServerCertificate=no;'
       
    #
    # Log the connection string and database
    #
    # print(f'server: {server}')    
    # print(f'database: {database}')    
    # print(f'user: {user}')    
    # print(f'password: {password}')    
    print(f'connectionString: {connectionString}')    

 
    return pyodbc.connect(connectionString)
  
  return None

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
    TOP 5 x.First, x.Last 
    FROM 
    [dbo].[User] x 
    ORDER BY 
    x.Last, x.First;
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