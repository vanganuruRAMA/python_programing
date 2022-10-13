import pymysql

def create_table():
    db=pymysql.connect(host='localhost', user='root', 
    password='Rama123@',
    database='textbook')
    create=db.cursor()
    return create,db

create,cdb=create_table()
print(create)
print(cdb)


def insert_data_into_table(write,cdb):

    query='insert into textbook(id=3, name=puneeth, price=15)'
    query='insert into textbook(id, name, price) values(%s,%s,%s)'
    for i in range(1,5):
        name='puneeth'+str(i)
        val=(3,name,15)
        
        write.execute(query,val)
        cdb.commit()
        #print(write.rowcount)
    

def read_data(read):
    query='select * from textbook'
    read.execute(query)
    res=read.fetchall()
    for i in res:
        print(i)


def update_data(update,cdb):

    query = "update textbook SET name = 'puneeth' where id= 4"
    update.execute(query)
    cdb.commit()
    
def delete_table_row(delete,cdb):
    query="delete from textbook where id=1 "
    delete.execute(query)
    cdb.commit()
    

insert_data_into_table(create,cdb)
read_data(create)
update_data(create,cdb)
#delete_table_row(create,cdb)
