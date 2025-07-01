"""Student record management with SQLite"""
import sqlite3

def init():
    with sqlite3.connect('students.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS students(
            roll INTEGER PRIMARY KEY,
            name TEXT,
            marks REAL)''')

def add_student():
    roll=int(input("Roll: "))
    name=input("Name: ")
    marks=float(input("Marks: "))
    with sqlite3.connect('students.db') as conn:
        conn.execute('INSERT INTO students VALUES(?,?,?)',(roll,name,marks))
    print("Added.")

def list_students():
    with sqlite3.connect('students.db') as conn:
        for r in conn.execute('SELECT * FROM students'):
            print(r)

def main():
    init()
    while True:
        cmd=input("add/list/quit: ")
        if cmd=='add': add_student()
        elif cmd=='list': list_students()
        elif cmd=='quit': break

if __name__=='__main__':
    main()
