import sqlite3;

conn=sqlite3.connect('univ.db')
cur=conn.cursor()

dno=int(input('enter dno:'))
dname=input('enter dept name:')
#cur.execute('insert into dept values(10,"abc")')
#cur.execute('insert into dept(name,deptno) values("def",20)')
cur.execute(f'insert into dept values({dno},"{dname}")')
conn.commit()
cur.close()
conn.close()
