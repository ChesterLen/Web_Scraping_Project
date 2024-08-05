import psycopg2

from databse_connection import curser

try:
    curser.execute(
        "CREATE TABLE IF NOT EXISTS students (student_id int, name varchar, age int, gender varchar, subject varchar, marks int);")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    curser.execute("INSERT INTO students (student_id, name, age, gender, subject, marks) \
    VALUES (%s, %s, %s, %s, %s, %s)", \
                   (1, "Ivan", 23, "Male", "Python", 85))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)


try:
    curser.execute("INSERT INTO students (student_id, name, age, gender, subject, marks) \
    VALUES (%s, %s, %s, %s, %s, %s)", \
                   (2, "Mariya", 22, "Female", "Python", 86))
except psycopg2.Error as e:
    print("Error: Inserting Rows")
    print(e)