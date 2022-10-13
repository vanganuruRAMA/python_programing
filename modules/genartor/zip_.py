numbers=[1,2,3,4,5,6,"nice"]
squers=(1,4,9,16,25,36,49)
names=["siva","pavan","mahesh","nari"]
#output (1,1)(2,4)
print(tuple(zip(numbers,squers,names))[2][2])
print(list(zip(numbers,squers,names))[2][2])