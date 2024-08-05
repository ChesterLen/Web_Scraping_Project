import psycopg2

connection = None

try:
    connection = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=postgres")
except psycopg2.Error as e:
    print("Error: Could not make connection to the Postgres database")
    print(e)

curser = None

try:
    curser = connection.cursor()
except psycopg2.Error as e:
    print("Error: Could not get curser to the Database")
    print(e)


connection.set_session(autocommit=True)

try:
    curser.execute("create database ws_database")
except psycopg2.Error as e:
    print(e)
    