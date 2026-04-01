# 24092 - airplane database application
# imports
import sqlite3

# constants and variables
DATABASE = "fighter.db"

# functions
# printing all aircraft
def print_all_aircraft():
    '''print all aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    print_aircraft = "SELECT * FROM fighter;"
    cursor.execute(print_aircraft)
    results = cursor.fetchall()
    # loop through all results first
    print("Name                         Speed   Max_G Climb Range Payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finished here
    db.close()

# print all aircraft, but sort by speed
def sort_by_speed():
    '''sort all aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sort_with_speed = "SELECT * FROM fighter ORDER BY speed DESC;"
    cursor.execute(sort_with_speed)
    results = cursor.fetchall()
    # loop through all results first
    print("Name                         Speed   Max_G Climb Range Payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finished here
    db.close()

# print all aircraft, but sort by speed
def sort_by_max_g():
    '''sort all aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sort_with_max_g = "SELECT * FROM fighter ORDER BY max_g DESC;"
    cursor.execute(sort_with_max_g)
    results = cursor.fetchall()
    # loop through all results first
    print("Name                         Speed   Max_G Climb Range Payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finished here
    db.close()

# print all aircraft, but sort by climb rate   
def sort_by_climbrate():
    '''sort all aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sort_with_climbrate = "SELECT * FROM fighter ORDER BY climb_rate DESC;"
    cursor.execute(sort_with_climbrate)
    results = cursor.fetchall()
    # loop through all results first
    print("Name                         Speed   Max_G Climb Range Payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finished here
    db.close()

# print all aircraft, but sort by range
def sort_by_range():
    '''sort all aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sort_with_range = "SELECT * FROM fighter ORDER BY range DESC;"
    cursor.execute(sort_with_range)
    results = cursor.fetchall()
    # loop through all results first
    print("Name                         Speed   Max_G Climb Range Payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finished here
    db.close()

# print all range, but sort by payload
def sort_by_payload():
    '''sort all aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sort_with_payload = "SELECT * FROM fighter ORDER BY payload DESC;"
    cursor.execute(sort_with_payload)
    results = cursor.fetchall()
    # loop through all results first
    print("Name                         Speed   Max_G Climb Range Payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    # loop finished here
    db.close()

# main code
while True:
    user_input = input(
    '''What would you like to do?
    1. Print all aircraft
    2. Sort all aircraft by speed
    3. Sort all aircraft by max g force
    4. Sort all aircraft by climb rate
    5. Sort all aircraft by range
    6. Sort all aircraft by payload
    7. Exit the program

    ''')
    if user_input == "1":
        print_all_aircraft()
    elif user_input == '2':
        sort_by_speed()
    elif user_input == '3':
        sort_by_max_g()
    elif user_input == '4':
        sort_by_climbrate()
    elif user_input == '5':
        sort_by_range()
    elif user_input == '6':
        sort_by_payload()
    elif user_input == "7":
        break
    else:
        print('That was not an option!')
