import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Gourav@3172',
    database = "test_mtg"
)

c = db.cursor()

query = """
        create table test2 (id int not null,
         name varchar(255),
         gender varchar(255),
         phone int not null,
         primary key (id))"""

c.execute(query)
db.close()