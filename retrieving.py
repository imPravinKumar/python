import sqlite3
md=sqlite3.connect("md.db")
cur=md.cursor()
sql="SELECT * FROM stu;"
cur.execute(sql)

#using fetchall()
r=cur.fetchall()
print(r)