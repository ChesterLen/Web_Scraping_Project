import psycopg2

from databse_connection import curser

try:
    curser.execute("CREATE TABLE IF NOT EXIST students (student_id int, name varchar, age int, gender varchar, subject varchar, marks int);")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)