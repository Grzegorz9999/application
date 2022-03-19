from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateDatabase, DuplicateTable

USER = "postgres"
HOST = "localhost"
PASSWORD = "coderslab"

CREATE_DB = "CREATE DATABASE application_db;"

CREATE_USERS_TABLE = """CREATE TABLE users(
    id serial PRIMARY KEY, 
    username varchar(255) UNIQUE,
    hashed_password varchar(80))"""

CREATE_MESSAGES_TABLE = """CREATE TABLE messages(
    id SERIAL, 
    from_id INT REFERENCES users(id),
    to_id INT REFERENCES users(id), 
    text varchar(255),
    creation_date TIMESTAMP)"""

try:
    cnx = connect(database="exercises_db", user=USER, password=PASSWORD, host=HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_DB)
        print("Database ready")
    except DuplicateDatabase as e:
        print("Database already exists")
    try:
        cursor.execute(CREATE_USERS_TABLE)
        print("Users table ready")
    except DuplicateTable as e:
        print("Users table already exists")
    try:
        cursor.execute(CREATE_MESSAGES_TABLE)
        print("Messages table ready")
    except DuplicateTable as e:
        print("Messages table already exists")
    cnx.close()
except OperationalError as e:
    print("Connection Error: ", e)
