import pyodbc

CONNECTION_STRING=(
'DRIVER={ODBC Driver 17 for SQL Server};'
'SERVER=localhost,1433;'
'DATABASE = appdb;'
'UID=sa;'
'PWD=examlyMssql@123'
)

def get_connection():
    conn=pyodbc.connect(CONNECTION_STRING)
    _IN