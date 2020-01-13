import sqlite3
import os
import datetime

path = "C:/Users/" + os.getlogin() + "/Desktop/Expense.sqlite"


def open_file():
    try:
        db = 'file:{}?mode=rwc'.format(path)
    except sqlite3.OperationalError:
        print("Unable to create database file")
    con = sqlite3.connect(db, uri=True)
    return con


def expense(con):
    cur = con.cursor()
    n = input("What was your latest expense? ")
    if n == "": pass

    p = input("What was your purpose of spending? ")
    if p == "":
        print("No inputs")
        display()
        exit(0)

    cur.execute('''CREATE TABLE IF NOT EXISTS Expense (Purpose TEXT, Expenditure INTEGER, Date TEXT)''')
    cur.execute('''INSERT INTO Expense (Purpose, Expenditure, Date) VALUES(?, ?, ?)''',
                (p, int(n), datetime.date.today().strftime("%d %b %Y")))

    con.commit()
    display(con, cur)


def display(con, cur):
    s = cur.execute('''SELECT SUM(Expenditure) FROM Expense''')
    print("------")
    print("Total expense so far: {}".format(s.fetchone()[0]))
    print("------")

    for _ in cur.execute('''SELECT Purpose, Expenditure, Date FROM Expense ORDER BY Expenditure DESC'''):
        print("{} : Rs.{} | {}".format(str(_[0]), _[1], str(_[2])))
    con.commit()
    cur.close()
    con.close()


def main():
    c = open_file()
    expense(c)


if __name__ == "__main__":
    main()
