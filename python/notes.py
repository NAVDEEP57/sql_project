#basiic rule to write coad in python 
'''
statemaent: basi unit of programm 
  x=10
  x=10+20
 ( x=10+23+
   20+23  this is worng )
'''
#for multiliner statement 
'''

'''
#arithmatic oprater:(-,+,*,/,**(for power ),%(for reminder), //(for whole after division ))
'''
x=15//2
print(x)

# remainder(%)
num = int(input("Enter a number:"))
print(num%2)
print(num%2==0) 
if(num%2==0):
    print(num,"is an even number") 
else:
    print(num,"is an odd number")
'''
#realtional oprater:(==,!=(not equal),<,>,<=,>=)

#logical oprater : ( or ,and , not)
'''
 or = if one statemaent is ture it show true 
 end = if one statemaent is false it sshows fales 
 not = it gives oppsite value means if statemaent true it shows false 
 '''
#assigment oprater :(+=,-=,*=,/=,//=,**=,%=)
'''
x=10
x+=10
print(x)
'''
#standerd data type :
'''
 we use type function to see type of data 
 1 int 
  x=10
 2 float
  x=13.54
 3 string
   x="hello"
'''
'''
x=13
print(type(x))
''' 
#funtion of string 
'''
#how to write string
x="hello NISHANT"
x="""hello nishant
      ....................... """      (string for pragraph)
'''
# print(data[starting element:next element from last: step gap])
'''
data="heLlo Nishant"
print(data[3])
print(data[:7])
print(data[2:])
print(data[2:7:2])
print(data[ : :-1])
print(data[-1: :-1])
print(data+" how are you")   #to add string
print(data*4)                #to wirte multiple time 
#print(data+200)             # it is worng becouse diffrent data type it shows type error
print(data.capitalize())
print(data.center(2))
print(data.endswith("t"))
print(data.find(h))
print(data.index(2))
print(data.format(4))
print(data.expandtabs(5))
print(data.casefold(2))
'''
#list: it is collaction of element of same and diffrent data type .list is mutabel(means we can edit or change it ) element 
'''
# listname[] it is function for list 
data=[2,4,6,8,0,2,3,4,[3,4,2,6,3],"""hello"""]
#function of list 
print(data[:])
print(data[4])
print(data[8][4])
print(data+[2,3])
data[2]=678  #to change the value
print(data[:])
del data[2]
print(data[:])
data.append(23)
print(data[:])
data.append([3,45,6,7])
print(data[:])
data.extend([23,56,45,23,12])
print(data[:])

'''

# any type of input by user 
'''
num = eval(input("Enter a string:"))
print(num)
print(type(num))
'''
# control statement 
'''
--> control statement is used to execute block of code on the basis of condition. If condition will return True then interpreter will allow to execute its block 
''' 
# Types of control statement 
'''
1> if else statement 
2> if elif else statement 
3> nested if elif else statement 
''' 
# if elif else statement 
'''
if(condition-1):
    block of if 
elif(condition-2):
    block of elif-1 
elif(condition-3):
    block of elif-2 
-------------------
-------------------
-------------------
elif(condition-n):
    block of elif-(n-1)
else:
    block of else 
''' 
# nested if elif else statement 
'''
if(condition):
    if(condition):
        block of nested if 
    elif(conditin):
        block of elif 
    ----------------    
    ----------------    
    ----------------
    elif(condition):
        block of elif 
    else:
        block of else 
elif(condition):
    if(condition):
        block of nested if 
    elif(conditin):
        block of elif 
    ----------------    
    ----------------    
    ----------------
    elif(condition):
        block of elif 
    else:
        block of else 
---------------------
---------------------
---------------------   
else:
    if(condition):
        block of nested if 
    elif(conditin):
        block of elif 
    ----------------    
    ----------------    
    ----------------
    elif(condition):
        block of elif 
    else:
        block of else 
'''
#while loop
'''
 while(condition):
    statement1
    statement1
    statement1
    statement1
    statement1
    x=x+step
'''
#for loop
'''
for i in range()
   statement1
   statement2
   statement3
'''
#functions- function are use to defien any specific task .
'''
function are of tow type
(1)- bulit iin functions= already defind in psf(python softwere fundation) when ever we need we can call tham   
(2)-user define = it can defind by the user
    syntex-
          def function_name(perameter list):
          #type of perameter passing inside a funtion
           1. Required perameter passing:
              def fun(x,y):
                 print(x,y)
              fun(3,4)     here 3=x ,4=y, are the req. perameter 
           2. Defalut peramerter:
               def fun(x=3,y=4):
                 print(x,y)
                fun()                 #it print 3 and 4
                fun(20)               #it means x=20 and y=4 
                fun(10,20)            # it means x=10 and y=20
           3. keyward perameter pasing:
               def fun(name,age)
                 print(f"name is{name} and age is {age}")
                 fun(nishant,23)                          #it print name is nishant and age is 23
                 fun(age=23,name="nishant")               #it print name is nishant and age is 23
                 fun(23,nishant)                          #it is worng
           4. variable length peramerter passing:
              def fun(*x):
                 print(x)
            fun(2,4,5,6,6,5,4,3,2)

            or

            def fun(**x):
                 print(x)
            fun(p=12,q=23,r=34)
            
'''
#return statement= it can return te value of funtion by deflalt it is "None" and it can also defind by user .
 
# file heandling- By this we can do read or write werite opratoin in other file like .txt, binary files.
'''
name=str(input("enter the name ="))
print(f"{name}")
file=open("hello.txt","a")      #to opan a file and it neccesry to opne of close a file {"w"- to overwrite file or if file not exist it create new file.
file.write(f"\n{name}")                         #{"a"- to append data or overload tha data,or if file not exist it create new file.}
file.close()                                     #{"r"-to read the data, if file not exist it throw the error file not found}
print("data write done")
'''
'''
n=open("hello.txt","r")
c=n.readline(2)
d=n.readlines()    #to write all line in a list
x=n.seek(0,0)      #to change the position of courser (0,0) for begining
print(c)
print(d)
print(x)
n.close
print(ord("a"))    #to find binary value of keybord key
print(len(d))
'''
#import oprating system:
'''
import os
os.mkdir("new")
y=os.getcwd()
print(y)

'''

#Exception handlinng:
'''
Exception are unique object that python uses to control error that occur when a program is runing .
'''
'''
a=int(input("enter number ="))
try:
   print(20/a)
except:
    print("zero division error ")
'''

#else with exception:
'''
a=int(input("enter number ="))
try:
   print(20/a)
except:
    print("zero division error ")
else:
    print("program have no error")
'''
# assertion:it is run if statement is false.the code assert keyword is used when debugging code.
'''
x=12
assert x>30,("this is an assertion error")
'''

# Regular expression: regular expression are use to deal with text data or in process of data
#                     mining(finding useful information from row data) or manupulation and transformation of text data.

'''
syntex import re:
\d- for digit
\D- for a not digit match
\s- for space match
\S- for a non space match
\w- for word match alpha numeric
\W- for non word match
 *- for zero or more match
 +- for one or more match
 .- for anything except new line
[abc]- for any of them a,b,c
[a-z]- for any between a to z
[A-Z]- for any between A to Z
[a-z0-9-a-z]- for any between a to z or 0-9 0r A-Z
{n}- excat n time
{m,n}- at list m time of at most n time match

'''

import re
data="regular expre678ssion are use  to deal with te8xt data or989 in process mining or06 manupul778ation and transformation of text data"
m=re.search("are",data)                       # it search data from staring 
if(m):
    print("data find=",m.group())
else:
    print("data not found")
m=re.match("re",data)
if(m):
    print("data find=",m.group())
else:
    print("data not found")
m=re.findall("re",data)                       #to find text and bound in a list 
if(m):
    print("data found=",m)
else:
    print("data not found")
x=re.match("[a-z].*",data)
if(x):
    print("found=",x.group())
else:
    print("not found")


# graphical use : call by tkinter
'''
import tkinter                    
win=t.Tk()                                              # to create window
win.configure(bg="skyblue")
l1=t.Label(win,text="Enter Data",bg="gray")             # to create a lable
l1.grid(row=0,column=4)                                 # position of lable
l2=t.Label(win,text="Enter your name",bg="lightblue")
l2.grid(row=1,column=3)
l3=t.Label(win,text="enter your email ",bg="lightblue")           
l3.grid(row=2,column=3)
l4=t.Label(win,text="enter the phone number",bg="lightblue")
l4.grid(row=3,column=3)
l5=t.Label(win,text="select the course-",bg="lightblue")
l5.grid(row=4,column=3)
e1=t.Entry(win)                                            # to create entry block
e1.grid(row=1,column=5)
e2=t.Entry(win)
e2.grid(row=2,column=5)
e3=t.Entry(win)
e3.grid(row=3,column=5)
drop= t.OptionMenu(win,"C++","Python","Java")              # to create drop down list
drop.grid(row=4,column=5)
button = t.Button(win,text="Submit Data",command=save,width="10",height="2")    # to create a button 
button.grid(row=6,column=4)
'''

# Multithreeding: it is use to run the multi task at same time. In which we create multi threed to prform task
''' syntex:
    t1=threeding.threed(target=task1)
    t2=threeding.threed(target=task2)
    ................................
    ................................'''
'''
import threading                                                # import the thread module  
from datetime import datetime                                                  # import time module  
import time
  
def sqre(num):                                               # define the sqre function  
    print(" Calculate the square root of the given number")  
    for n in num:   
        time.sleep(1)                                      # at each iteration it waits for 0.3 time  
        print(' Square is : ', n * n)  
        print(datetime.now().time())
def cube(num):                                               # define the cube() function  
    print(" Calculate the cube of  the given number")  
    for n in num:   
        time.sleep(1)                                      # at each iteration it waits for 0.3 time  
        print(" Cube is : ", n * n *n)  
        print(datetime.now().time())



arr = [4, 5, 6, 7, 2]                                        # given array  
t1 = threading.Thread( target=cube(arr))
t2 = threading.Thread( target=sqre(arr))
t1.start()
t2.start()

'''
# class and object:
#class:- class is collaction of object or it is prototype that drfine and state of object anythig that define insidea
        #class can only br acssic by its object and all thing define inside a class is called member of class.

#object:-cbject are the real world entities9 having state(variable can hold) and behaviour(function can hold) 
#syntex:-
'''
       class class_name:
             def__init__(self):                #it is initiate function
                  
             function2:
                  ............
             function3:
                  ............
       o2=class_name()                        #object creation
       o1=class_name() ... 

       print(o1.funtion1)                   #function call
       o1.fintion2()













'''


















































