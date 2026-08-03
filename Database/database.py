import sqlite3

#create a newdatabase and open a database connection to allow sqlite3 to work with it.

connection = sqlite3.connect("discipline_tracker.db")

#to execure SQL statments, and fetch results, we need to use a database cursor. Call connection.cursor()

cursor = connection.cursor()

print("Database connected successfull.")

connection.close()
