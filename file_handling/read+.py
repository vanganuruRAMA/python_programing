
'''
#file=open('data.txt','r+')
file=open('emp_records.csv','r+')
data=file.readlines()
for each_data in data:
    print(type(each_data))
    a=(each_data.split(','))
    print(len(a))
#file.write('\n this is read + method ')
file.close()
'''
def password_validator(password):
    special_symbols=['@','$','#','%']
    
    val=True
    if len(password)<6:
        print("length should be 6")
        val=False

    if len(password)>20:
        print("password must not be > 20")
        val=False
    if not any(char.isdigit() for char in password):
       print("should have at least one number")
       val=False

    if not any(char.isupper() for char in password):
       print("should have at least one upper")
       val=False

    if not any(char.islower() for char in password):
       print("should have at least one lower")
       val=False
    if not any(char in special_symbols for char in password):
        val=False
        print("please enter at least one special symbol")
       
    if val:
        val=val
    print(val,password)

file=open("emp_records.csv","r+")
data=file.readlines()
for each_data in data:
   #print(each_data.split(',')[1:3])
   names= each_data.split(',')[-1]
   #print(names)
   password_validator(names)
   #if 'Tammy'==names.strip():
   #if 'Ruby'==names.strip():

       #print('yes')
   #else:
      # print('no')
       
   
        
    
    
file.close()