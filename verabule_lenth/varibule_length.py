# variable length arguments:
#*args (Non-Keyword Arguments)
#**kwargs (Keyword Arguments)

#*args (Non-Keyword Arguments)
def august_batch(*names):
    print(names)
    print(type(names))
august_batch("subbareddy","suresh","barath","rajasekhar")


def get_details(name,*copany):
    print(name,copany)
    print(type(name))
get_details("rama","sree","tata","pooja")	

def march_batch(name,*copany):
    print(name,copany)
    print(type(name))
march_batch("tata","sree","rama","pooja")	

def may_batch(copany,*names):
    print(copany,names)
    print(type(names))
may_batch("tata","sree","rama","pooja")	
may_batch("tata","sree","rama","pooja")	

#**kwargs (Keyword Arguments)
def group(**names):
    print(names)
    print(type(names))
group(firstname="vanganuru",lastname="rama",id=4152,emailid="rama@")
group(firstname="vanganuru",lastname="rama",id=4152,emailid="rama@")
group(firstname="vanganuru",lastname="rama",id=4152,emailid="rama@")