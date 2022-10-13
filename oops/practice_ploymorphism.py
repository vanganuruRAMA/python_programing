#polymorphism


class Product:
    def __init__(self,name,brand,battery,ram):
        self.name= name
        self.brand= brand
        self.battery= battery
        self.ram= ram
    def show(self):
        print('deatails:',self.name,self.brand,self.battery,self.ram)
    def numberof_product(self):
        print("XI","relmi","nokia","samsung")
class India:
    def __init__(slef,telugu,english,hindi,kanada,tamil,maalayam,marati,kokani):
        slef.telugu= telugu
        slef.english= english
        slef.hindi= hindi
        slef.kanada= kanada
        slef.tamil= tamil
        slef.maalayam= maalayam
        slef.marati= marati
        slef.kokani= kokani
    def display(slef):
        print('details:',slef.telugu,slef.english,slef.hindi,slef.kanada,slef.tamil,slef.maalayam,slef.marati,slef.kokani)

object=Product("apple","tata",15,250)
object.show()
object.numberof_product()

object=India("AP","MG","GJ","KN","TM","MY","MAH","GOVA")
object.display()



class IndiAp:
    def capital(self):
        print("amaravati&vizag")
    def lang(self):
        print("telugu")
class Mah:
    def capital(self):
        print("mubai")
    def lang(self):
        print("marati")

obj_ind=IndiAp()
obj_may=Mah()
for staste in (obj_ind,obj_may):
    staste.capital()
    staste.lang()



class IndiaBestCity:
    def place(self):
        print("vizag","lepashi","badhrachalam","tadipatri")
    def lake(self):
        print("chitravathi","penna","godhavari","kollet")
    def crop(self):
        print("pady","groundnut","millet")
class Banglore:
    def place(self):
        print("chikmagulre","maysure","sangama")
    def lake(self):
        print("krushna","godhavari")
    def crop(self):
        print("sugarcan","cocanut")


ram_in=IndiaBestCity()
ram_ou=Banglore()
for india in (ram_in,ram_ou):
    india.place()
    india.lake()
    india.crop()



class Product:
    def __init__(self,name,color,size,ram,price,speed,camra,company):
        self.name= name
        self.color= color
        self.size= size
        self.ram= ram
        self.price= price
        self.speed= speed
        self.camra= camra
        self.company= company
    def show(self):
        print('details:',self.name,self.color,self.size,self.ram,self.price,self.speed,self.camra,self.company)
    def max_price(self):
        print("the maxmum price is 100000")
    def max_range(self):
        print("the net speed is a 5")
class Mobile(Product):
    def max_price(self):
        print("the price 25000")
    def max_range(self):
        print("tata")


jk_cm=Product('iphone','red',3,250,85000,5,2,'tata')
jk_cm.show()

jk_cm.max_price()
jk_cm.max_range()

jk_cm=Mobile('apple','white',8,750,98000,6,3,'nokia')
jk_cm.show()
jk_cm.max_price()
jk_cm.max_range()

class Vegatablu:
    def name(self):
        print("beens","mirch")
    def where(self):
        print("ap","tan")
class Non_Vegatablue:
    def name(self):
        print("whatermillon","banana")
    def where(self):
        print("panj","kerala")
def fun(obj):
        obj.name()
        obj.where()


obj_Vegatablu=Vegatablu()
obj_Non_Vegatablue=Non_Vegatablue()

fun(obj_Vegatablu)
fun(obj_Non_Vegatablue)