#overriding
'''
Method overriding is an ability of any object-oriented programming language that allows a subclass or child class to provide a specific implementation of a method that is already provided by one of its super-classes or parent classes. 
When a method in a subclass has the same name,
same parameters or signature and same return type(or sub-type) as a method in its super-class, 
then the method in the subclass is said to override the method in the super-class.

'''

class Parent(): 
    # Parent's show method
    def display(self):
        print("Inside Parent")
# Inherited or Sub class (Note Parent in bracket) 
class Child(Parent): 
    # Child's show method
    def show(self):
        print("Inside Child")
# Inherited or Sub class (Note Child in bracket) 
class GrandChild(Child): 
    # Child's show method
    def show(self):
        print("Inside GrandChild")

# Driver code 
g = GrandChild()   
g.show()
g.display()


class A:
    def show(self):
        print("hi rama how are yu")
    def sum(self):
         print("yes fine")
class B(A):
    def show(self):
        super().show()
        #A.show(self)
        print("good mrng ")
    def sum(self):
        #A.sum(self)        #this way not correct but ok
        super().show()
        print("all my team")
object=B()
object.show()
object.sum()

