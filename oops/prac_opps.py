#inherincetan
#single level
#multiple
#miltilevel


#single
class MarchBatch:
    def _init_(self):
        print("there is a paramaterised method")
    def show(self,name):
        print("name is :{}".format(name))
object=MarchBatch()
object.show("rama")

#multiple
class Father:
    def _init_(self):
        pass
    def leader(self):
        print("I love daddy")
class Mother:
    def cooking(self):
        print("she is cooking")
class Child(Father,Mother):
    def sports(self):
        print("he is good boy")

object=Child()
object.cooking()
object.sports()
object.leader()

#multilevel
class Animals:            #is called based
    def _init_(self):
       pass
    def eat(self):
        print("it was a eating")
class Dog(Animals):
    def bark(self):
        print("it is barking")
class BabyDog(Dog):        #is called deraived
    def weep(self):
        print("it was weeping")
object=BabyDog()
object.bark()
object.weep()
object.eat()

#object=Animals()     #this type wrong object but only multilevel
#object.bark()