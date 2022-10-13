'''

#file=open("data.txt","w+")
file=open("emp_records.csv","w+")
data=file.readlines()
#for each_data in data:
     print(type(each_data))
a=(each_data.split(','))
print(len(a))
file.write('\n this is read + method ')
file.close()

file=open("data.txt","w+")
file.write("hello goodmorning everyone")
file.close()


'''

file=open("emp_records.csv","r+")
data=(file.readlines())
for ram_data in data:
    print(type(ram_data))
    a=ram_data.split(',')[-1]
    print(ram_data.split(',')[1:9])
    print(len(a))
    print(a)
    #if "Tammy"==a.split():
    if "Roy"==a.split():
        print("yes")
    else:
        print("no")

file.close()