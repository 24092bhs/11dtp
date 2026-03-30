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
    print("Name                         Speed   Max_G Climb Range Payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finished here
    db.close()

#main code
while True:
    user_input = input("\nWhat would you like to do? \n1. Print all aircraft \n2. Exit the program \n")
    if user_input == "1":
        print_all_aircraft()
    elif user_input == '2':
        break
    else:
        print('That was not an option!')
