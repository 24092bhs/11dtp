# 24092 - theatresports database application

# imports
import sqlite3

# constants and variables
DATABASE = "theatresports.db"

# functions
# print all games
def print_all_games():
    '''print all games nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    print_games = "SELECT * FROM theatre_game;"
    cursor.execute(print_games)
    results = cursor.fetchall()
    # loop through all results
    print("Name:                                   Round:     Difficulty: Popularity: Min. People:")
    for game in results:
        print(f"{game[1]:<40}{game[2]:<12}{game[3]:<12}{game[4]:<12}{game[5]:<12}")
    # end of loop
    db.close()

# print blind round games
def print_blind_round():
    '''print all blind round games games nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    print_blind = "SELECT * FROM theatre_game WHERE round = 'Blind' ORDER BY game_name ASC;"
    cursor.execute(print_blind)
    results = cursor.fetchall()
    # loop through all results
    print("Name:                                   Round:     Difficulty: Popularity: Min. People:")
    for game in results:
        print(f"{game[1]:<40}{game[2]:<12}{game[3]:<12}{game[4]:<12}{game[5]:<12}")
    # end of loop
    db.close()

# print all choice round games
def print_choice_round():
    '''print all choice round games games nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    print_choice = "SELECT * FROM theatre_game WHERE round = 'Choice' ORDER BY game_name ASC;"
    cursor.execute(print_choice)
    results = cursor.fetchall()
    # loop through all results
    print("Name:                                   Round:     Difficulty: Popularity: Min. People:")
    for game in results:
        print(f"{game[1]:<40}{game[2]:<12}{game[3]:<12}{game[4]:<12}{game[5]:<12}")
    # end of loop
    db.close()

# find a student id
def find_id():
    '''find the student id of one of the team members''' # needs to be worked on!
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    find_student_id = "SELECT * FROM team_member WHERE first_name = 'Ashley';"
    cursor.execute(find_student_id)
    results = cursor.fetchall()
    # loop through all results
    for member in results:
        print(f"{member[1]} {member[2]}: Student ID {member[0]}")
    # end of loop
    db.close()

# sort all members by first name
def members_by_first_name():
    '''print all members nicely (first name)'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    order_first_name = "SELECT * FROM team_member ORDER BY first_name ASC;"
    cursor.execute(order_first_name)
    results = cursor.fetchall()
    # loop through all results
    print("First Name: Last Name:")
    for member in results:
        print(f"{member[1]:<12}{member[2]:<12}")
    # end of loop
    db.close()

# sort all members by last name
def members_by_last_name():
    '''print all members nicely (last name)'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    order_last_name = "SELECT * FROM team_member ORDER BY last_name ASC;"
    cursor.execute(order_last_name)
    results = cursor.fetchall()
    # loop through all results
    print("First Name: Last Name:")
    for member in results:
        print(f"{member[1]:<12}{member[2]:<12}")
    # end of loop
    db.close()

# sort all blind round games by difficulty (not done!)
def order_blind_by_difficulty():
    '''print all blind round games games nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    print_blind = "SELECT * FROM theatre_game WHERE round = 'Blind' ORDER BY game_name ASC;"
    cursor.execute(print_blind)
    results = cursor.fetchall()
    # loop through all results
    print("Name:                                   Round:     Difficulty: Popularity: Min. People:")
    for game in results:
        print(f"{game[1]:<40}{game[2]:<12}{game[3]:<12}{game[4]:<12}{game[5]:<12}")
    # end of loop
    db.close()

# sort all choice round games by difficulty

# sort all games by popularity

# print games that can be played with less than 4 players

# print games that can be played with 4 or more players

members_by_last_name()