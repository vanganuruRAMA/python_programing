#function
#required argument
#default argument
#keyword arguent


#required argument
def sum_of_two_numbers(num1,num2):
    print(num1+num2,num1-num2,num1*num2)
sum_of_two_numbers(10,20)
sum_of_two_numbers(120,140)
sum_of_two_numbers(15,10)
def odd_of_two_numbers(num3,num4):
    print(num3,num4)
odd_of_two_numbers(3,5)   
odd_of_two_numbers(3,9) 
odd_of_two_numbers(4,5) 
#default argument
def get_details(name="rama",company="techmahindra",id=456):
    print(name,company,id) 
get_details("surendra") 
  
def get_bank_details(name="sree",bank="icic",id=257,mailid="sree@"):
    print(name,bank,id,mailid)
get_bank_details("pooja")

#keyword arguent

def get_details(name,copany,project):
    print(name,"he is good working",copany,project)
get_details(name="ramudu",project="USA",copany="tata")