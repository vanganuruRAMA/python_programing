# Loops

"""
for
while
nested loop   
"""



# for

#for i in range(10):       #0,1,2,3,4,5,6,7,8,9
#    print(i)
    
#data=[1,2,3,4,5,6,7,8,9]    #1,2,3,4,5,6,7,8,9
#for j in data:
#    print(j)
    
#for count, k in enumerate(range(1,100)):       #1,2,3,4,5    99
#    print(count,k)                     #postion 0,1,2,3,     98
"""
  ("aparna","bharath","yasodha","jaya")     # enumerate is the position of value
      0        1        2         3


data2=("aparna","bharath","yasodha","jaya")    
for index,name in enumerate(data2):
    print(index,name)
    
data3="hi welcome to python"
for index,letter in enumerate(data3):
    print(index,letter)


# while loop

count=0
while count<10:
    count=count+1
    print("hello")
    """
b=[1,2,3,4,5,6,7,8,10]
while b:
    print(b.pop())
    print(b)
    
# nested loop   #loop of loop
"""
cars=["maruthi","mg","tata","indigo"]
colours=["blue","white","black","red","gray"] 
speed_range=["200","400","700","800"]

for car in cars:    
    for colour in colours:
        for speed in speed_range:
            print(car,colour,speed)
    
      """
    

    
for i in range(1,100):
   for j in range (1,i):
      if (i%j) == 0:
         pass
      else:
         print(str(i)+" is a prime number")

