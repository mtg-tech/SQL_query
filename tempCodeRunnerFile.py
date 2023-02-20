import mysql.connector as sql

db = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Gourav@3172',
    database = "test_mtg"
)

print(db)
db.close()