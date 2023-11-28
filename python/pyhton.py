# sum of two number 
'''
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
sum1 = num1 + num2 
print("Sum of two number is",sum1)
'''
# detect a number is odd or even
'''
x=int(input("enter the number ="))
if x%2==0:
      print(x," is even")
else:
    print(x," is odd")
'''
# area of triangle 
'''
a = float(input("Enter length of first side of triangle:"))
b = float(input("Enter length of second side of triangle:"))
c = float(input("Enter length of third side of triangle:"))
if((a+b)>c and (b+c)>a and (a+c)>b):
    s = (a+b+c)/2 
    area = (s*(s-a)*(s-b)*(s-c))**0.5
    print("Area of triangle is",area,"square-cm")
else:
    print("Triangle can not be formed with these dimensions")
'''
# greatest between two number 
'''
num1 = int(input("Enter first number:"))    
num2 = int(input("Enter second number:"))    
if(num1>=num2):
    print(num1,"is gretest") 
else:
    print(num2,"is greatest") 
'''

# greatest between two number 
'''
num1 = int(input("Enter first number:"))    
num2 = int(input("Enter second number:"))    
if(num1==num2):
    print("Both are equal")
elif(num1>num2):
    print(num1,"is gretest") 
else:
    print(num2,"is greatest") 
'''
# gretest among three number 
'''
num1 = int(input("Enter first number:"))    
num2 = int(input("Enter second number:"))    
num3 = int(input("Enter third number:"))  
if(num1==num2 and num2==num3):
    print("All are equal") 
elif(num1>=num2 and num1>=num3):
    print(num1,"is greatest") 
elif(num2>=num3):
    print(num2,"is greatest") 
else:
    print(num3,"is greatest")
''' 
# categorize age into old , young , teen , chidhood age 
'''
age = float(input("Enter your age:")) 
if(age<=0 or age>125):
    print("Invalid age input") 
elif(age>=60):
    print("old age") 
elif(age>=20):
    print("Young age") 
elif(age>12):
    print("Teen age") 
else:
    print("Childhood age")
'''

# detect a leap year 
'''
y = int(input("Enter a leap year:")) 
if(y%4==0):
    if(y%100==0):
        if(y%400==0):
            print(y,"is a leap year") 
        else:
            print(y,"is not a leap year") 
    else:
        print(y,"is a leap year") 
else:
    print(y,"is not a leap year")
    
'''

#swipe to number
'''
x=0
num1=int(input("enter the number"))
num2=int(input("enter the number"))
print("value of a =",num1)
print("value of b =",num2)
x=num1
num1=num2
num2=x
print("value of a=",num1)
print("value of b=",num2)
'''
#grater number
''' 
num1=int(input("enter the number"))
num2=int(input("enter the number"))
print("value of a =",num1)
print("value of b =",num2)
if(num2<num1):
    print(num1,"is grater")
else:   
    print(num2,"is grater")
'''
#SI
'''
p=int(input("enter the principle vlue="))
t=int(input("enter the time period="))
r=int(input("enter the rate of intrest per annual="))
i=(p*t*r)/100
sum=p+i
print("simple intrest for",t,"year=",i)
print ("total sum =",sum)
'''
#ci
'''
p=int(input("enter the principle vlue="))
t=int(input("enter the time period="))
r=int(input("enter the rate of intrest per annual="))
a=(p*(1+(r/100))**t)
ci=a-p
print("compound intrest for",t,"year=",ci)
print ("total amount =",a)
'''

#to find bmi and chack underweight or over weight
'''
h=float(input("enter the Height in meter="))
w=float(input("enter the weight in kg="))
b=w/(h*h)
if(b<=18):
    print("underweight")
elif(b>18 and b<=25):
    print("normal weight")
elif(b>25 and b<30):
    print("over weight")
else:
    print("obbese")
'''
# To count number of elphabet in string
'''
x="hello how are you"
y=0
z=0
t=0
c=" "
while(y<len(x)):
 if(x[y] not in c):
     z=x.count(x[y])
     print(x[y],"=",z)
     t=t+z 
     c=c+x[y]
 y=y+1
print("total number of elphabet=",t)  

'''
# factorial of a given number
'''
x=int(input("enter the number ="))
y=1
c=1
while(y<=x):
    c=c*y
    y=y+1
print(c)     
'''

# find total no of even odd and string data present in given list
'''
data=[3,24,56,776,44,334,55,43,23,5,'a',6,"fddfsdf","""sd"""]
x=0
odd=0
string=0
even=0
while(x<len(data)):
     if(type(data[x])==str):
          string=string+1
     elif(data[x]%2==0):
          even=even+1
     else:
          odd=odd+1
     x=x+1     
print("numbers of even",even)
print("numbers of odd",odd)
print("numbers of string",string)
'''
# to find prime number and co-prime number
'''
x=int(input("enter the number "))

for i in range(2,x-1):
   if(x%i==0):
       print(x,"is a co-prime number")
       break
   print(x,"prime number")
   break''
'''
# To find largest number in a list.
'''
data=[3,5,2,5,43,565,4949,55,56,44,9998,999]
maximum=0

for i in data:
    for x in range(i+1,len(data)):
        if data[i]>=data[x]:
            if maximum<=data[i]:
                maximum=data[1]
        else:
            if maximum<=data[x]:
                maximum=data[x]
            
print("max",maximum)
'''
# To reverse the list element order .
'''
data=[23,43,12,54]
re=[]
for i in range(len(data)-1,-1,-1):
    re.append(data[i])
print("data=",data)    
print("re=",re)

'''

# To find prime & coprime number
'''
data=[8,5,3,4,6]
coprime=0
prime=0
for i in range(0,len(data)):
    for x in range(2,data[i]):
        if (data[i]%x==0):
            coprime=coprime+1
            break  
    else:
        prime=prime+1
   
print("numbers of prime element",prime)
print("numbers of coprime element",coprime)
'''
# TO form ***** digram 
#         *****
#         *****
#         *****
#         *****
'''
for i in range(5):
    for x in range(5):
        print("*",end="")

    print()

'''
# To form triangel shap by *
'''
for i in range(10):
    for x in range(10-i):
        print(" ",end="")
    for x in range(i):
        print("*",end="")
    for x in range(i+1):
        print("*",end="")
   
    print()
        
'''
# to form a daimond shap by *
'''
r=int(input("enter no of row"))
for i in range(r):
    for x in range(r-i):
        print(" ",end="")
    for x in range(i):
        print("*",end="")
    for x in range(i+1):
        print("*",end="")
    print()
for i in range(r,-1,-1):
    for x in range(r-i):
        print(" ",end="")
    for x in range(i):
        print("*",end="")
    for x in range(i+1):
        print("*",end="")
    
   
    print()
'''
# To form 
'''
   *ooo*ooo*
   o*oo*oo*o
   oo*o*o*oo
   ooo***ooo
'''
'''
r=int(input("enter no of row"))
for i in range(r):
    for y in range(i):
        print("o",end="")
    for x in range(1):
        print("*",end="")
    for x in range(r-1-i):
        print("o",end="")
    for y in range(1):
        print("*",end="")
    for y in range(r-1-i):
        print("o",end="")
    for x in range(1):
        print("*",end="")
    for x in range(i):
        print("o",end="")
    print()
'''

# To use the user define funtion 
'''

def rec(r):                            # TO form rectangel shap
    for i in range(r):
        for x in range(r):
            print("*",end="")
        print()


def tri(r):                            # To form triangel shap
 star=1
 spc=r-1
 for i in range(r):
    print(" "*spc,"*"*star,sep="")
    star=star+2
    spc=spc-1
 print()
def dia(r):                             # to form a daimond shap 
 star=1
 spc=r-1
 for i in range(r):
    print(" "*spc,"*"*star,sep="")
    star=star+2
    spc=spc-1
 star=star-4
 spc=1
 for i in range(r):
    print(" "*spc,"*"*star,sep="")
    star=star-2
    spc=spc+1
 print()
r=int(input("number of row in rec")) 
rec(r)
r=int(input("number of row in triangle"))
tri(r)
r=int(input("number of row in diamond"))
dia(r)

'''
# To form the swastika
'''
r=int(input("enter no. "))
 
for i in range(1):  
    print("* ","  "*(r-3)," *"*r,sep="",end="")
    print()
for i in range(r-1):
    print("*","  "*(r-2),"*",sep="",end="")
    print()
for i in range(1):  
    print("* "*(r-1)*2,end="")
    print()
for i in range(r-1):
    print(" ","  "*(r-2),"*","  "*(r-2),"*",sep="",end="")
    print()  
for i in range(1):  
    print(" ","* "*(r-1),"  "*(r-3)," *",sep="",end="")
'''
# wap useing of lambda funtion:
'''
r=[]
arr=[2,3,4,5]
fun=[lambda x:x*2,lambda x:x+5,lambda x:x**2,lambda x:x+5]
def camp():
     for i in range(len(arr)):
          x=arr[i]
          for j in range(len(fun)):
               x=fun[j](x) 
               r.append(x)
     return print(r)
camp()
'''              



























