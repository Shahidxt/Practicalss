import sqlite3
cnt = sqlite3.connect("database.db")


# cnt.execute('''CREATE TABLE USER(
#     NAME TEXT,
#     ID INTEGER,
#     CLASS INTEGER,
#     ROLLNO INTEGER,
#     PHONENO INETEGR,
#     ACCURACY REAL
#     );''')

# cnt.execute(""" INSERT INTO USER(NAME, ID , CLASS,ROLLNO,PHONENO) VALUES ('SHAHID SHAIKH',10,14,6055,9648857886) ;""")

# cnt.execute(""" delete from user;""")
# cnt.commit()

data=cnt.execute(""" SELECT * FROM USER;""")

# for i in data:
#     print(i)