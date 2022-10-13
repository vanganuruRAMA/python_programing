'''
File Handling:
1. Open method
2. With open method

read
write
append
'''
#open method
'''
file=open("data.txt","w")
file.write("hello goodmorning everyone")
file.close()
'''

#with open method
'''
with open("data2.txt","w")as file_obj:
    file_obj.write("welcome to python")
'''

#read mode
'''
file=open("data2.txt","r")
print(file.readlines())
file.close()

with open("data2.txt","r")as file_obj:
    print(file_obj.readline())
'''

#append
file=open("data.txt","a")
file.write("\nhow are you\n this is append method")
file.close()

'''
Behavior  Modes
Read      r, r+, w+, a+
Write     r+, w, w+, a, a+
'''

#f = open("<file name>", "r+")  # Textual read and write