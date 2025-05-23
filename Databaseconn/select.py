import sqlite3;

conn=sqlite3.connect('univ.db')

cur=conn.cursor()

row=cur.execute('select * from dept')
row1=cur.execute("select name from dept where deptno='abc' ")
print(row)
print(row.fetchone())
print(row.fetchmany(2))
print(row.fetchall())
print(row1.fetchone())

cur.close()
conn.close()