print("******************Hey you******************")
name=str(input("enter your name- "))
import re
for i in range(30):
    mail=str(input("enter your mail"))
    a=re.match("[a-z0-9A-Z]+@+[gmail|yahoo|outlook]+\.+[com|in|org|net]",mail)
    if(a):
       mail=a.group()
       break
    else:
        print("enter corect mail")

for i in range(15):
    try:
        ph=int(input("enter your phone number"))
    except:
        print("enter number in numeric ")
   
    else:
        if(len(str(ph))==10):
        
            break
        else:
            print("enter correct phone number")
print("please select the course")
print("course               fees")
print("python        -      20000")
print("java          -      23000")
print("django        -      21000")

x=str(input("enter the course-"))
if x=="python":
    print("fees - 20000")
    y=(20000/100)*12
    t=20000+y
    print(f"GST - {y}")
    print(f"total fees -{t}")
elif x=="java":
    print("fees - 23000")
    y=(23000/100)*12
    t=23000+y
    print(f"GST - {y}")
    print(f"total fees -{t}")
elif x=="django":
    print("fees - 21000")
    y=(21000/100)*12
    t=21000+y
    print(f"GST - {y}")
    print(f"total fees -{t}")
else:
    print("please enter a valid course")
        
print(f"Name - {name}")
print(f"Email - {mail}")
print(f"Phone number - {ph}")

d=open("data.txt","a")
d.write(f"\nName of student is {name}")
d.write(f"\nEmail - {mail}")
d.write(f"\nPhone number {ph}")
d.write(f"\nSlected course - {x}")
d.write(f"\nTotal fees - {t}")
d.write("\n-------------------------------------")
d.close()


import pymysql

mydb=pymysql.connector.connect(user='nkm',password="nkm@12345",host="localhost",database="python")
mycursor = db.cursor()
mycursor.execute("SHOW DATABASES")








