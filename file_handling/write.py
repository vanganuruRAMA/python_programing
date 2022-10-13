#open method
#write
file=open("data.txt","w")
file.write("hello good marning")
file.close()
#with open


with open("data2.txt","w") as file_obj:
    file_obj.write("welcom python")
	
#read
file=open("data2.txt","r")
print(file.readlines())
file.close()

#with open
with open("data2.txt","r") as file_obj:
    print(file_obj.readlines())

#append
file=open("data.txt","a")
file.write("how are you  this is append method")


'''
Behavior  Modes
Read      r, r+, w+, a+
Write     r+, w, w+, a, a+
'''