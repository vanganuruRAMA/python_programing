
def password_validator(password,name,emp_id):
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
   # print(val,password)
    print('emp_id: {3},emp_name: {0},emp_password: {1},password_value: {2}, '.format(name,val,password,emp_id))
#file=open("emp_records.csv","r+")
#data=file.readlines()

with open("emp_records.csv","r+") as data:
    a=data.readlines()
    #print(a)
    for each_word in a:
        names=each_word.split(',')[2]
        emp_ids=each_word.split(',')[0]
        password=each_word.split(',')[-1]
    
        password_validator(password,names,emp_ids)
        
            
       
    #if 'Tammy'==names.strip():
        #print('yes')
   #else:
        #print('NO')
		
   
   
   
   
   
   
   
  
  # print(each_data.split(',')[0:9])
   # names=each_data.split(',')[-1]
	
   # print(names)
   # password_validator(names)
    #if 'Tammy'==names.strip():
       # print('yes')
   #else:
        #print('NO')
		
   