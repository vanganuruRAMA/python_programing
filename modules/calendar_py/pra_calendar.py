import calendar

print(calendar.month(2002,10))
print(calendar.calendar(2005,1,2,10)) 


if calendar.isleap(2004):
    print("this is aleap year")
else:
    print("not aleap year")



#create  plain atext calendar  but must should capital the "T" and "C" 

c=calendar.TextCalendar(calendar.SUNDAY)
str=c.formatmonth(2025,1)
print(str)

c=calendar.TextCalendar(calendar.THURSDAY)
#str=c.formatmonth(2025,1)
#print(str)
for i in c.itermonthdays(2025,4):
    print(i)




#for name in calendar.month_name:
for name in calendar.day_name:
    print(name)
    #print(name)

