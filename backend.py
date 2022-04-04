import sqlite3

def connect():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE routine(Id INTEGER PRIMARY KEY, data TEXT, earnings INTEGER, exercise TEXT, study TEXT, diet TEXT, python TEXT)")
    conn.commit()
    conn.close()

def insert(date , earnings, exercise , study , diet , python):
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO routine VALUES(NULL , ?,?,?,?,?,?)",(date , earnings, exercise , study , diet , python))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM routine"))
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

def delete():
    conn = sqlite3.connect('routine.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM routine WHERE id=?", (id,)))
    conn.commit()
    conn.close()
