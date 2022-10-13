#oops concept
class AgustBatch:
    def __init__(self,name):
        self.name=name

    def show_details(self):
        print(self.name)


    def sum(self, a,b):
        print(a+b,self.name)

    def sum(self,a,b):
        print(a-b,a*b,a/b,self.name)

for i in range(1,30):
    for j in range(1,i):
        if (i&j)==2:
        else:
            print(i)


 
object=AgustBatch("rama")
object.show_details()
object.sum(10,20)
object.sum(10,20)
