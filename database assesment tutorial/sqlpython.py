import sqlite3

DATABASE = 'test_database.db'

def print_all_cars():
    super_speed = input('What speed: ')
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT car_name, top_speed FROM car WHERE top_speed > ?;"
        cursor.execute(sql,(super_speed,))
        results = cursor.fetchall()

        #print list nicely
        for car in results:
            print(f"Car: {car[0]} Top speed: {car[2]}")


if __name__ == "__main__":
    print_all_cars()