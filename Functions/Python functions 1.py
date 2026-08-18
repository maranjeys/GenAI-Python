#Functions:
#---------
#function means organized collection of meaningful instructions to do a specific task whenever the function gets called
#Functions are reusable code instructions template
#Functions are named code containers
#Functions are sub routine
#Functions are code container modules

# Function Components:

# parameter ----> place holder --- (promoted variables)

# Arguments ----> actual value given by user at run time

# NOTE :  function usually returns the processed output value as an END RESULT


def add():  #Fucntion without parameter
...     a,b=20,30  # a & b are variable
...     return a+b
... 
>>> add()
50
>>> add()
50
>>> add()
50
>>> # Reusable code
>>> 
>>> def addition(a,b): # Fucntion with parameter -> a & b are parameter
...     return a+b
... 
>>> addition(400,500)
900
>>> addition(3,1)
4
>>> addition(345,567)
912

#Types of functions
#--------------------
#1) User defined function(customized function)
#2) Math function
#3) Builtin function
#4) Recursive function --> Function inside function
#5) Lambda function(anonymous function)

#User defined fuction:
#---------------------
#A function where the paramaters and arguments are defined by the user is called as user defined function(UDF)

# use "def" keyword at the beginning followed by a meaningful functions enclosed with ()

# invoke line indentation using :

# create logic for the function and return the output

# call the function to get the output

#-------------------------------------------------------------------
#calling function with print

def bio(name, age, city):

    return (name, age, city)
name = input('enter name:')
age = int(input('enter age:'))
city = input('enter city:')

print (bio(name, age, city))

#calling function without print

def bio(name, age, city):

    print (name, age, city)
name = input('enter name:')
age = int(input('enter age:'))
city = input('enter city:')

bio(name, age, city)

# Rat using function

name='maran'
def name_rat():
    for i in range(0,len(name)):
        for j in range(0,i+1):
            print(name[i],end=' ')
        print()
name_rat()

# Inverse Rat using function

name='maran'
def name_irat():
    for i in range(len(name),0,-1):
        for j in range(0,i):
            print(name[i-1],end=' ')
        print()
name_irat()

# Call function with chioce

print('Available choices:')
print('------------------')
print('1.name rat')
print('2.name irat')

choice = int(input('Enter the choice:'))
if choice==1:
    name_rat()
elif choice==2:
    name_irat()
else:
    print ('Enter valid choice')
