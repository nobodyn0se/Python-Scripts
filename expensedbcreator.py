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

    cur.execute('''CREATE TABLE IF NOT EXISTS Expense (Purpose TEXT, Expenditure INTEGER, Date TEXT)''')
    cur.execute('''INSERT INTO Expense (Purpose, Expenditure, Date) VALUES(?, ?, ?)''',
                (p, int(n), datetime.date.today().strftime("%d %b %Y")))

    con.commit()
    display()


def display():
    s = cur.execute('''SELECT SUM(Expenditure) FROM Expense''')
    print("------")
    print("Total expense so far: {}".format(s.fetchone()[0]))
    print("------")

    for _ in cur.execute('''SELECT Purpose, Expenditure, Date FROM Expense ORDER BY Expenditure DESC LIMIT 10'''):
        print("{} : Rs.{} on {}".format(str(_[0]), _[1], str(_[2])))

    cur.close()


def main():
    expense()


if __name__ == "__main__":
    main()
