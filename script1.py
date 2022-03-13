import sqlite3
import pathlib

DB_FILE = "emploees.db"
DB_FOLDER = "DB1"
TABLE_NAME = "employees"
PATH_TO_DB = pathlib.Path(__file__).parent.joinpath(DB_FOLDER, DB_FILE)

SQL_CREATE_TABLE = f"""
CREATE TABLE "employees" (
	"id"	INTEGER UNIQUE,
	"first_name"	TEXT,
	"last_name"	TEXT,
	"email"	TEXT,
	"tel"	TEXT,
	"gender"	TEXT,
	"ip_address"	TEXT,
	"birthday"	INTEGER,
	"children"	INTEGER,
	"address"	TEXT,
	"city"	TEXT,
	"salary"	INTEGER,
	"employment_date"	TEXT,
	"department_id"	INTEGER,
	PRIMARY KEY("id")
);  
"""



with sqlite3.connect(PATH_TO_DB) as conn:
    cursor = conn.cursor()
    # cursor.execute(SQL_CREATE_TABLE)
    cursor.execute("""
        SELECT * FROM employees
        WHERE last_name = 'Brenston'
    """)
    for row in cursor.fetchall():
        print(row)
        pass
    

        
    