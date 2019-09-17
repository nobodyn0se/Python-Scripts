import sqlite3
import os
import datetime

con = sqlite3.connect("C:/Users/" + os.getlogin() + "/Desktop/Expense.sqlite")
cur = con.cursor()


def expense():
    n = input("What was your latest expense? ")
    if n == "": pass

    p = input("What was your purpose of spending? ")
    if p == "":
        print("No inputs")
        display()
        exit(0)

    cur.execute('''CREATE TABLE IF NOT EXISTS Expense (Purpose TEXT, Expenditure INTEGER)''')
    cur.execute('''INSERT INTO Expense (Purpose, Expenditure) VALUES(?, ?)''', (p, int(n)))

    con.commit()
    display()


def display():
    s = cur.execute('''SELECT SUM(Expenditure) FROM Expense''')
    print("------")
    print("Total expense so far: {}".format(s.fetchone()[0]))
    print("------")
    for _ in cur.execute('''SELECT Purpose, Expenditure FROM Expense ORDER BY Expenditure DESC LIMIT 10'''):
        print("{} : Rs.{}".format(str(_[0]), _[1]))
    cur.close()


def main():
    expense()


if __name__ == "__main__":
    main()
