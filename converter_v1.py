# create db table:
# date
# currency
# amount
import sqlite3
import pathlib
import json

JS_FILE = "exchange.json"
PATH_TO_FILE = pathlib.Path(__file__).parent.joinpath(JS_FILE)
DB_FILE = "emploees.db"
DB_FOLDER = "DB1"
TABLE_NAME = "employees"
PATH_TO_DB = pathlib.Path(__file__).parent.joinpath(DB_FOLDER, DB_FILE)
TABLE_NAME = "exchange"


def create_db_table_from_json(file, db):
    # STEP 1: read json file

    with open(file) as f:
        json_data = json.load(f)

    date_to_write = json_data["date"]
    print(date_to_write)
    rates_to_write = json_data["rates"].items()

    # STEP 2: create db table
    SQL_CREATE_TABLE = f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
	"code"	TEXT NOT NULL UNIQUE,
	"rate_to_euro"	REAL,
	"date"	TEXT,
	PRIMARY KEY("code")
);
    """

    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute(SQL_CREATE_TABLE)

     # STEP 3: insert data into db table
     # STEP 3.1:
        SQL_POPULATE_TABLE = f"""
    INSERT INTO {TABLE_NAME} (code, rate_to_euro, date) VALUES
    (?, ?, DATE('{date_to_write}'))
    """
     # STEP 3.2:
    with sqlite3.connect(db) as conn:
        try:
            cursor = conn.cursor()
            cursor.executemany(SQL_POPULATE_TABLE, rates_to_write)
        except sqlite3.IntegrityError:
            print("Error: ID already exists")
    pass


def convert(from_currency, to_currency, amount):
    SQL_QUERY_FROM_CUURENCY = f"""
    SELECT rate_to_euro FROM {TABLE_NAME}
    WHERE code = '{from_currency}'
    """
    SQL_QUERY_TO_CUURENCY = f"""
    SELECT rate_to_euro FROM {TABLE_NAME}
    WHERE code = '{to_currency}'
    """
    
    # with try and except
    with sqlite3.connect(PATH_TO_DB) as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(SQL_QUERY_FROM_CUURENCY)
            from_rate = cursor.fetchone()[0]
            cursor.execute(SQL_QUERY_TO_CUURENCY)
            to_rate = cursor.fetchone()[0]
        except sqlite3.OperationalError:
            print("Error: currency not found")
    return to_rate / from_rate * amount

create_db_table_from_json(PATH_TO_FILE, PATH_TO_DB)
print(f"Res: {convert('ILS', 'EUR', 1000):10.2f}")