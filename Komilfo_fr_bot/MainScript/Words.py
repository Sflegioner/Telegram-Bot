import sqlite3
con = sqlite3.connect("C:\SQLite\words.db")
cur = con.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS words(
            id INTEGER, 
            word TEXT, 
            translate TEXT, 
            lvl TEXT) """)

cur.execute("INSERT INTO words VALUES('Bonjour','Привіт','A1')")
cur.execute("SELECT * FROM words")
listW = cur.fetchall()
print(listW)
con.commit()
con.close()