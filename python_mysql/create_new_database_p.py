import pymysql

def create_table():
    db=pymysql.connect(host='localhost', user='root', 
    password='yasodhareddy432@gmail.com',
    database='Test_Books')
    create=db.cursor()
    return create,db

create,cdb=create_table()
print(create)
print(cdb)


def insert_data_into_table(write,cdb):

    #query='insert into Test_Books(s_no=1, bookname=english, prize=15)'
    query='insert into Test_Books(s_no, bookname, prize) values(%s,%s,%s)'
    for i in range(10,101):
        name='test'+str(i)
        val=(i,name,150)
        
        write.execute(query,val)
        cdb.commit()
        print(write.rowcount)
    

def read_data(read):
    query='select * from Test_Books'
    read.execute(query)
    res=read.fetchall()
    for i in res:
        print(i)


def update_data(update,cdb):

    query = "update Test_Books SET bookname = 'english' where s_no = 1"
    update.execute(query)
    cdb.commit()
    
def delete_table_row(delete,cdb):
    query="delete from test_books where s_no=1 "
    delete.execute(query)
    cdb.commit()
    

insert_data_into_table(create,cdb)
read_data(create)
#update_data(create,cdb)
#delete_table_row(create,cdb)
