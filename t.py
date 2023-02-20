import mysql.connector as sql

db = sql.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Gourav@3172',
    database = "test_mtg"
)
cs = db.cursor()
cs.execute("select * from test1")

res  = cs.fetchall()

for i in res:
    print(i)
db.close()