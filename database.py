import sqlite3

connection = sqlite3.connect('habits.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS habits (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               Habits TEXT)
""")

cursor.execute("""CREATE TABLE IF NOT EXISTS completion (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               habit_id INTEGER,
                date TEXT)              
""")

connection.commit()
connection.close()

def add_habit(habit_name) :
    connection = sqlite3.connect('habits.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO habits (Habits) VALUES (?)", (habit_name,))
    connection.commit()
    connection.close()

def get_all_habits() :
    connection = sqlite3.connect('habits.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM habits")
    habits = cursor.fetchall()
    connection.close()
    return habits

def log_habit_completion(habit_id, date) :
    connection = sqlite3.connect('habits.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO completion (habit_id, date) VALUES (?, ?)", (habit_id, date))
    connection.commit()
    connection.close()

def get_completed_habits_by_date(date) :
    connection = sqlite3.connect('habits.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM completion WHERE date = (?)", (date,))
    habits_by_date = cursor.fetchall()
    connection.close()
    return habits_by_date

def get_habit_completion_count(habit_id) :
    connection = sqlite3.connect('habits.db')
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM completion WHERE habit_id = (?)", habit_id)
    count = cursor.fetchone()[0]
    connection.close()
    return count   

def get_today(date) :
    connection = sqlite3.connect('habits.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM completion WHERE date = (?)", (date,))
    today_habits = cursor.fetchall()
    connection.close()
    return today_habits    
