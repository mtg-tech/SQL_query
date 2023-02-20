import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Gourav@3172',
    database = "test_mtg"
)

cs = db.cursor()

cs.execute("select name, id from test1 where id > 1")

res = cs.fetchall()

print(res)

for i in res:
    print("Name : "+i[0]+" ID : "+str(i[1]))



db.close()