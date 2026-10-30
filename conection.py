import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",   # пустой пароль
    database="gastro"
)

print("CONNECTED!")

cursor = conn.cursor()

cursor.execute("SELECT * FROM kunde")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()