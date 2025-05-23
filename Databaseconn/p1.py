import sqlite3;

conn=sqlite3.connect('univ.db')

cur=conn.cursor()

cur.execute('create table dept(deptno integer primary key,name text )')

conn.commit()
cur.close()
conn.close()