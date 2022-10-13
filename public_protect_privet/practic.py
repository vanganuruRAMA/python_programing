
class sum:
    def __init__(self,name,age,speed):
        self.name=name
        self.age=age
        self.speed=speed
    def show(self):
        print('details:',self.name,self.age,self.speed)

object=sum('rama',25,200)
object.show()




class Banglore:
    def show(self):
        print("hello")
    def disply(self):
        print("rama",25)
obj=Banglore()
obj.show()
obj.disply()

#public_protect
class Public_data:
    def __init__(self,name,age,id):
        self.public_name=name
        self.public_age=age
        self.public_id=id
    def show(self):
        print('age:',self.public_age)


#print('name:',obj.public_name)

obj=Public_data("hi rama",25,278)

print('name:',obj.public_name)
print('id:',obj.public_id)

obj.show()

    