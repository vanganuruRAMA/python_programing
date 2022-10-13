#dictionary datatype

data={"name":"yasodha","college":"JNTUA","code":"python","Role_No":123,"fruites":['banana','apple','cherry']}
#print(type(data))
print(dir(data))
print(data.keys())
print(data.values())
print(data.items())
#data.pop("Role_No")    #only specific values deleted
#print(data)
#data.update({"name":"yasodha reddy"})
#print(data)
"""
data["name"]="apple"
print(data)
#print(data.get("college"))
print(data["college"])
out_put=data.popitem()
print(out_put)
print(data)
data.clear()
print(data)   #{}   total clear data
data2=data.copy()
print(data2)
ids=("id1","id2","id3")
out_put=data2.fromkeys(ids,0)
print(out_put)
"""
a=data.setdefault("college2",'SV')
print(a)
print(data)


