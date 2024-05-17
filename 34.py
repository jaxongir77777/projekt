import sqlite3
db = sqlite3.connect("data.db")
cursor = db.cursor()
# table yaratish uchun sql so‘rov yuboramiz
cursor.execute("""CREATE TABLE texnika(
tartibi INT,
name TEXT,
surname TEXT,
age INTEGER)""")
db.commit()
cursor.execute("""
db.close()
