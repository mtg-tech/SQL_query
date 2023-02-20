import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Gourav@3172',
    database = "test_mtg"
)

cs  = db.cursor()
query = """
        insert into test1  (id, name, gender, phone) 
            values (%s, %s, %s, %s)
"""
val1 = ("1", "Gourav", "male", "111")
val2 = ("2", "Priyanka", "Female", "222")

cs.execute(query, val1)
cs.execute(query, val2)

    
db.commit()
db.close()