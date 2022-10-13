#multiple
class Mobile:
    def __init__(self):
        pass
class Brand(Mobile):
    def name(self):
        print("apple phone")
class Battery(Brand):
    def volt(self):
        print("15A")
class Ram(Battery):
    def storge(self):
        print("storge 150")
class Company(Ram):
    def tata(self):
        print("tata is a good company")
class City(Company):
    def bng(self):
        print("that is banglore")

object=City()
object.name()
object.volt()
object.storge()
object.tata()
object.bng()



#Miltiple

class A:
    def _init_(self):
        pass
    def emp_name(self):
        print("rama")
    def emp_id(self):
        print("1452")
    def emp_slary(self):
        print("25000")
    def emp_mailid(self):
        print("rama1@gmail.com")
        print("--------------")
class B:
    def emp1_name(self):
        print("sree")
    def emp1_id(self):
        print("1245")
    def emp1_slary(self):
        print("52000")
    def emp1_mailid(self):
        print("sree1@gmail.com")
class C(A,B):
    def company(self,name):
        print("name is:{}".format(name))

object=C()
object.company("tata")
object.emp_name()
object.emp_id()
object.emp_slary()
object.emp_mailid()


object.emp1_name()
object.emp1_id()
object.emp1_slary()
object.emp1_mailid()