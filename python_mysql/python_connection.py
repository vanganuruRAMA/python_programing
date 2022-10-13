import pymysql

def mysql_con():
    conn=pymysql.connect(host='localhost',user='root',password='Rama123@',database='rama')
    cur=conn.cursor()
    return cur,conn

mdb,cur=mysql_con()
print(mdb)
print(cur)

def read_data(mycursor):
    query='select * from rama'
    mycursor.execute(query)
    res=mycursor.fetchall()
    for i in res:
        print(i)


def insert_data_into_table(mycursor,mdb):
    query='insert into rama(id,name,age) values(%s,%s,%s)'
    val=(3,'ramudu',26)
    mycursor.execute(query,val)
    mdb.commit()
    print(mycursor.rowcount)
    

insert_data_into_table(cur,mdb)    


#read_data