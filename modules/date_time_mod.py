import datetime
res=datetime.datetime.utcnow()
print(res.year)
print(res.strftime("%p"))
print(res.strftime("%A"))
print(res.strftime("%d"))
print(res.strftime("%B"))
print(res.strftime("%f"))
print(res.strftime("%Z"))