#24092 - airplane database application
#imports
import sqlite3

#constants and variables
DATABASE = "fighter.db"

#functions
def print_all_aircraft():
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter;"
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
    db.close()

#main code
