import sqlite3 as sq


con = sq.connect("test.dbs")

mycursor = con.cursor()

#mycursor.execute(""" create table pass (id integer primary key autoincrement, name text)""")


mycursor.execute("""insert into pass(name) values('aymen')""")
mycursor.execute("""insert into pass(name) values('mohamed')""")
mycursor.execute("""insert into pass(name) values('bilel')""")

mycursor.execute("""select * from pass""")
res = mycursor.fetchall()
for r in res:
    print(r)
con.close()