import sqlite3
import pathlib

DB_FILE = "emploees.db"
DB_FOLDER = "DB1"
TABLE_NAME = "employees"
PATH_TO_DB = pathlib.Path(__file__).parent.joinpath(DB_FOLDER, DB_FILE)


SQL_GET_ALL_RECORDS = f"SELECT * FROM {TABLE_NAME}"


with sqlite3.connect(PATH_TO_DB) as conn:
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM employees
        WHERE last_name = 'Brenston'
    """)
    for row in cursor.fetchall():
        print(row)
        pass
    
    cursor.execute(SQL_GET_ALL_RECORDS)
    res = cursor.fetchall()
    
print(type(res))
print(len(res))
print(res[0])
print(res[0][3])
 
        
    