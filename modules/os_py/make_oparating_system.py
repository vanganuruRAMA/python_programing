import os

#print(dir(os))
current_path=os.getcwd()
print(current_path)

#directory= "sivakrishna"
#os.mkdir(directory)
list_dir= os.listdir(current_path)
print(list_dir)
#os.rmdir("sivakrishna")

list_dir= os.listdir(current_path)
print(list_dir)

os.rename("text.py","siva.py")

