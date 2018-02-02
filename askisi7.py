from datetime import datetime

now = datetime.now()
year = now.year
month = now.month
day = now.day
weekday = now.weekday()
count = 0
for i in range(1,11):
    for j in range(1,13):
        if weekday == datetime(year+i,j,day).weekday():
         count += 1

if weekday == 0:
    weekday = "Deyteres"
elif weekday ==1:
    weekday = "Trites"
elif weekday ==2:
    weekday = "Tetartes"
elif weekday ==3:
    weekday = "Pemptes"
elif weekday ==4:
    weekday = "Paraskeyes"
elif weekday ==5:
    weekday = "Savvata"
elif weekday ==6:
    weekday = "Kiriakes"
print "Sta epomena 10 xronia 8a exoume alles "+str(count)+" "+weekday+" pou 8a einai h "+str(day)+"i tou mina"



