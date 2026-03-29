#24092 - airplane database application
#imports
import sqlite3

#constants and variables
DATABASE = "fighter.db"

#functions
def print_all_aircraft():
    '''print all aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM fighter;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop through all results first
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<5}{fighter[3]:<4}{fighter[4]:<4}{fighter[5]:<4}{fighter[6]:<4}")
    #loop finished here
    db.close()

#main code
print_all_aircraft()