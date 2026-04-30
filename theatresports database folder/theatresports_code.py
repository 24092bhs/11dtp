# 24092 - theatresports database application

# imports
import sqlite3

# constants and variables
DATABASE = "theatresports.db"
number_one = 1
number_two = 2
number_three = 3
number_four = 4
number_five = 5
number_six = 6
number_seven = 7

# functions
# print all games
def print_all_games():
    '''print all games nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    print_games = "SELECT * FROM theatre_game ORDER BY game_name ASC;"
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

# sort all blind round games by difficulty
def order_blind_by_difficulty():
    '''print all blind round games games nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    blind_difficulty = "SELECT * FROM theatre_game WHERE round = 'Blind' ORDER BY difficulty ASC;"
    cursor.execute(blind_difficulty)
    results = cursor.fetchall()
    # loop through all results
    print("Name:                                   Round:     Difficulty: Popularity: Min. People:")
    for game in results:
        print(f"{game[1]:<40}{game[2]:<12}{game[3]:<12}{game[4]:<12}{game[5]:<12}")
    # end of loop
    db.close()

# sort all blind round games by popularity
def order_blind_by_popularity():
    '''print all blind round games games nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    blind_popularity = "SELECT * FROM theatre_game WHERE round = 'Blind' ORDER BY popularity, game_name ASC;"
    cursor.execute(blind_popularity)
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

# sort all choice round games by difficulty
def order_choice_by_difficulty():
    '''print all blind round games games nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    choice_popularity = "SELECT * FROM theatre_game WHERE round = 'Choice' ORDER BY difficulty ASC;"
    cursor.execute(choice_popularity)
    results = cursor.fetchall()
    # loop through all results
    print("Name:                                   Round:     Difficulty: Popularity: Min. People:")
    for game in results:
        print(f"{game[1]:<40}{game[2]:<12}{game[3]:<12}{game[4]:<12}{game[5]:<12}")
    # end of loop
    db.close()

# sort all choice round games by popularity
def order_choice_by_popularity():
    '''print all blind round games games nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    choice_difficulty = "SELECT * FROM theatre_game WHERE round = 'Choice' ORDER BY popularity ASC;"
    cursor.execute(choice_difficulty)
    results = cursor.fetchall()
    # loop through all results
    print("Name:                                   Round:     Difficulty: Popularity: Min. People:")
    for game in results:
        print(f"{game[1]:<40}{game[2]:<12}{game[3]:<12}{game[4]:<12}{game[5]:<12}")
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

# find a student id (NEEDS TO BE FINISHED)
def find_id():
    '''find the student id of one of the team members'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    while True:
        try:
            member_name = int(input('''What student's information do you need?
                                1. Ashley
                                2. Charlotte
                                3. Eileen
                                4. Fiona
                                5. Hannah
                                6. Isabelle\n'''))
            if member_name == number_one:
                find_student_id = "SELECT * FROM team_member WHERE first_name = 'Ashley';"
                break
            elif member_name == number_two:
                find_student_id = "SELECT * FROM team_member WHERE first_name = 'Charlotte';"
                break
            elif member_name == number_three:
                find_student_id = "SELECT * FROM team_member WHERE first_name = 'Eileen';"
                break
            elif member_name == number_four:
                find_student_id = "SELECT * FROM team_member WHERE first_name = 'Fiona';"
                break
            elif member_name == number_five:
                find_student_id = "SELECT * FROM team_member WHERE first_name = 'Hannah';"
                break
            elif member_name == number_six:
                find_student_id = "SELECT * FROM team_member WHERE first_name = 'Isabelle';"
                break
            else:
                print("That is not a member of the Theatresports team! Please enter a number from 1-6.")
        except ValueError: 
            print("Please enter a number from 1-6.")
    cursor.execute(find_student_id)
    results = cursor.fetchall()
    # loop through all results
    for member in results:
        print(f"{member[1]} {member[2]}: Student ID {member[0]}")
    # end of loop
    db.close()

# print games that can be played with less than 4 players
def two_or_three_players():
    '''print all games nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    less_than_four = "SELECT * FROM theatre_game WHERE min_people < 4 ORDER BY min_people ASC;"
    cursor.execute(less_than_four)
    results = cursor.fetchall()
    # loop through all results
    print("Name:                                   Round:     Difficulty: Popularity: Min. People:")
    for game in results:
        print(f"{game[1]:<40}{game[2]:<12}{game[3]:<12}{game[4]:<12}{game[5]:<12}")
    # end of loop
    db.close()

# print games that can be played with 4 or more players
def four_plus_players():
    '''print all games nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    four_or_more = "SELECT * FROM theatre_game WHERE min_people >= 4;"
    cursor.execute(four_or_more)
    results = cursor.fetchall()
    # loop through all results
    print("Name:                                   Round:     Difficulty: Popularity: Min. People:")
    for game in results:
        print(f"{game[1]:<40}{game[2]:<12}{game[3]:<12}{game[4]:<12}{game[5]:<12}")
    # end of loop
    db.close()

# main code
while True:
    # ask the player what they would like to do
    user_input = int(input('''\nWelcome to the Theatresports Database!
      What would you like to search?
      1. All of the games in the database
      2. All of the blind round games
      3. All of the choice round games
      4. Find what games can be played with all the members of my team
      5. The names of the BHS Theatresports team
      6. The information (name or student ID) of a team member
      7. Exit the program

    '''))
    # all of the games in the database printed
    if user_input == number_one:
        print_all_games()
    # blind round games: if and elif statements for different ways of sorting the data (need to include invalid inputs and more functions!)
    elif user_input == 2:
        blind_data_sorted = int(input('''How would you like the data sorted?
              1. By difficulty
              2. By popularity
              3. I just want to the see the data as it is\n'''))
        if blind_data_sorted == number_one:
            order_blind_by_difficulty()
        elif blind_data_sorted == number_two:
            order_blind_by_popularity()
        elif blind_data_sorted == number_three:
            print_blind_round()
    # choice round games: if and elif statements for different ways of sorting the data (need to include invalid inputs and more functions!)
    elif user_input == number_three:
        choice_data_sorted = int(input('''How would you like the data sorted?
              1. By difficulty
              2. By popularity
              3. I just want to the see the data as it is\n'''))
        if choice_data_sorted == number_one:
            order_choice_by_difficulty()
        elif choice_data_sorted == number_two:
            order_choice_by_popularity()
        elif choice_data_sorted == number_three:
            print_choice_round()
    # find games that can be played with certain numbers of players
    elif user_input == number_four:
        number_of_players = int(input('How many people are in your team?\n'))
        if number_of_players < number_four:
            two_or_three_players()
        elif number_seven > number_of_players >= number_four:
            four_plus_players()
        elif number_of_players >= number_seven:
            print("Sorry, I cannot help you! You can only have up to six players per team.")
    # sorting members: if and elif statements for different was of sorting the data (need to include invalid inputs!)
    elif user_input == number_five:
        sorted_by = int(input('''\nDo you want it sorted by:
                              1. First name
                              2. Last name\n'''))
        if sorted_by == number_one:
            members_by_first_name()
        elif sorted_by == number_two:
            members_by_last_name()
    # finding member information (needs to be updated)
    elif user_input == number_six:
        find_id()
    # exit the program
    elif user_input == number_seven:
        print("Thank you for using the Theatresports Database!")
        break
    # catches all invalid inputs
    else:
        print('That is not an option! Please put one of the numbers provided.')
        break
