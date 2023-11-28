import re
regex=r"[a-z0-9A-Z]+@+[google|yahoo|outlook|]+\.+[com|in|org|net]"
def checkemail(email):
    if(re.search("[a-z0-9A-Z]+@+[gmail|yahoo|outlook|]+\.+[com|in|org|net]",email)):
        print("valid email")
        return True
    else:
        print("invalid email")
        email=input("again enter corect email")
        checkemail(email)
        return True
        
def checknumber(number):
    regex=r'^\+?\d{9,12}$'
    if(re.fullmatch(regex,number)):
        return True 
    else:
        number=str(input("again enter mobile number"))
        checknumber(number)
        return True

def checkname(name):
    for i in name:
        if i.isdigit():
            value=False
            break
        else:
            value=True
            return True
            
import datetime
def timesample():
    x = datetime.datetime.now()
    return x

def writefile(name,email,mobile,course,time):
    import os
    writepath='file.txt'
    mode='a' if os.path.exists(writepath) else 'w'
    with open(writepath,mode) as f:
        f.write(f'Name:{name}\n')
        f.write(f'email:{email}\n')
        f.write(f'Mobile:{mobile}\n')
        f.write(f'Course:{course}\n')
        f.write(f'Time:{time}\n')
        f.write(f'*********\n')

def courseSelection():
    print("Select a course:\n 1. Python\n 2. Artificial Intelligence 3. AWS")
    value=int(input())
    if value==1:
        return"Python"
    elif value==2:
        return"Artificial Intelligence"
    elif value==3:
        return"AWS"
    else:
        print("invalid selection")
        return 0

def userdetail():
    name=input("enter your name:")
    if checkname(name):
        email=input("enter email:")
        if checkemail(email):
            mobile=input("enter mobile number:")
            if checknumber(mobile):
                course=courseSelection()
                context={
                    "Name": name,
                    "Email":email,
                    "Number":mobile,
                    "Date":timesample(),
                    "Course":course,}
                
                writefile(name,email,mobile,course,timesample())
                print(f"welcome{name}\n your email address {email}\n your mobile number{mobile}\n your course{course}")
            else:
                print("Wrong Mobile number")
        else:
            print("wrong email address")
    else:
        print("user name")

userdetail()



