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

# print all team members
def print_all_members():
    '''print all members nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    print_members = "SELECT * FROM team_member;"
    cursor.execute(print_members)
    results = cursor.fetchall()
    # loop through all results
    print("First Name: Last Name:")
    for member in results:
        print(f"{member[1]:<12}{member[2]:<12}")
    # end of loop
    db.close()

# print blind round games
def print_blind_round():
    '''print all blind round games games nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    print_blind = "SELECT * FROM theatre_game WHERE round = 'Blind';"
    cursor.execute(print_blind)
    results = cursor.fetchall()
    # loop through all results
    print("Name:                                   Round:     Difficulty: Popularity: Min. People:")
    for game in results:
        print(f"{game[1]:<40}{game[2]:<12}{game[3]:<12}{game[4]:<12}{game[5]:<12}")
    # end of loop
    db.close()

# print all choice round games

# find a student id

# sort all names by alphabetical order

# sort all blind round games by difficulty

# sort all choice round games by difficulty

# sort all games by popularity

# print games that can be played with less than 4 players

# print games that can be played with 4 or more players

print_blind_round()