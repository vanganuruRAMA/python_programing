def password_validator(password):
    special_symbols=['@','$','#','%']
    
    val=True
    if len(password) <6:
        print("let should be atleast 6")
        val=False
        
    if len(password) >20:
        print("must not be >20")
        val=False
    if not any(char.isdigit() for char in password):
        print("Should have at least one number")
        val=False

    if not any(char.isupper() for char in password):
        print("Should have at least one uppercase")
        val=False    
        
    if not any(char.islower() for char in password):
        print("Should have at least one lowercase")
        val=False

    if not any(char in special_symbols for char in password):
        print("please enter atleast one special symbol")
        val=False    
        
    if val:
        val=val
    print(val)    
#password=input("please enter password:")    
#password_validator(password)    

# Required arugments:

def sum_of_two_numbers(num1,num2):
    print(num1+num2)
sum_of_two_numbers(10,20)
sum_of_two_numbers(120,140)
def odd_of_two_numbers(num3,num4):
    print(num3,num4)
odd_of_two_numbers(3,5)   
odd_of_two_numbers(3,9) 

# defalut arguments:

def get_details(name="subbareddy",company="techmahindra",id=456):
    print(name,company,id) 
get_details("surendra")   

# keyword arguments:

def team(name,project):
    print(name,"is working on an",project)
team(project="python automation",name="subbareddy")

# variable length arguments:
#*args (Non-Keyword Arguments)

def august_batch(*names):
    print(names)
    print(type(names))
august_batch("subbareddy","suresh","barath","rajasekhar")

def august_batch(company,*names):
    print(company,names)
	
    print(type(names))
august_batch("techmahindra","subbareddy","suresh","barath","rajasekhar")

#**kwargs (Keyword Arguments):
def get_info(**details):
    print(details)
get_info(first_name="subbareddy",last_name="vadlamuri",company="ibm",id=456)
