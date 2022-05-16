from multiprocessing import connection
from venv import create
import cx_Oracle 
#def create_db():
con=cx_Oracle.connect('sumit/abhinav')
print(con.version)
cur=con.cursor()
print(cur)

stat1="select email,password from singup"
cur.execute(stat1)

for i in cur:
    print(i)

cur.close()
con.close()
def conn():
    cur=connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid varchar primary key not null,nametext,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    connection.Commit()
conn()