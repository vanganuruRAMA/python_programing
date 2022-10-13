import pymysql

def mysql_con():
    conn=pymysql.connect(host='localhost',user='root',password='yasodhareddy432@gmail.com',database='august1st')
    cur=conn.cursor()
    return cur,conn
    
cur,mdb=mysql_con()
print(cur)
print(mdb)

def read_data(mycursor):
    query='select * from users'
    mycursor.execute(query)
    res=mycursor.fetchall()
    for i in res:
        print(i)
        
read_data(cur)

def insert_data_into_table(mycursor,mdb):
    query='insert into users(id, name, age) values(%s,%s,%s)'
    val=(1,'python',27)
    mycursor.execute(query,val)
    mdb.commit()
    print(mycursor.rowcount)
        
#insert_data_into_table(cur,mdb)
    
#using python 
'''
create dataase
create table
update tale data
delete table data

'''

