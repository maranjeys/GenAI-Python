Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> '''  LOOPING STATEMENTS                   
... ...                    - for
... ...                    - while '''
'  LOOPING STATEMENTS                   \n...                    - for\n...                    - while '
>>> 
... # looping statements :
... 
... # looping => same set of actions repeated many times till n-1 times based on given condition
... 
... # for loop
... # while loop
... 
... # what is iterative statements???
... 
... # Iterative => going through the elements of a given python collection(list/set/tuple/dict)using for loop / while loop
... 
>>> # FOR LOOP:
>>>   # CORM Process -> Check Once Runs Manytimes
...   
>>>   # For Loop checks the condition only once and run the loop many time (n-1)
...   
>>> for i in range(5):
...     print (i)

    
0
1
2
3
4
for i in range(1,10,1):
    print (i)

    
1
2
3
4
5
6
7
8
9
# i -> Item
#range(1,10,1), 1-> Starting Value, 10-> Stopping Value, 1-> Step increment value

for i in range(1,11,1):
    print (i,end = '')

    
12345678910
for i in range(1,11,1):
    print (i,end = '  ')

    
1  2  3  4  5  6  7  8  9  10  
for i in range(1,11,1):
    print (i,end = '_')

    
1_2_3_4_5_6_7_8_9_10_

for i in range(1,11,1):
    print (i)
    print ('_')

    
1
_
2
_
3
_
4
_
5
_
6
_
7
_
8
_
9
_
10
_

# print even numbers b/w 1 to 10
for i in range(2,11,2):
    print (i,end = ' ')

    
2 4 6 8 10 
# print even numbers b/w 1 to 10
# print even numbers b/w 1 to 10
for i in range(1,11,2):
    print (i,end = ' ')

    
1 3 5 7 9 


# 1 - odd
# 2 - even
# 3 - odd
# 4 - even
# 5 - odd

for i in range(1,11,1):
    if i%2==0:
        print( i,' - even')
        else:
            
SyntaxError: invalid syntax
for i in range(1,11,1):
    if i%2==0:
        print( i,' - even')
    else:
        print( i, '- odd')

        
1 - odd
2  - even
3 - odd
4  - even
5 - odd
6  - even
7 - odd
8  - even
9 - odd
10  - even


for i in range(1,11):
    if i%2==1:
        print( i,' - odd')
    else:
        print( i, ' - even')

        
1  - odd
2  - even
3  - odd
4  - even
5  - odd
6  - even
7  - odd
8  - even
9  - odd
10  - even

prog = ['C','Fortran','Pascal','Java','C++','Python','C#']

for i in prog:
    print(i)

    
C
Fortran
Pascal
Java
C++
Python
C#

name = ['creta', 'ciaz', 'cruze', 'santro', 'santafe']

for i in name:
    print(i.startswith('c'))

    
True
True
True
False
False

for i in name:
    if i.startswith('c'):
        print(i)

        
creta
ciaz
cruze

for i in name:
    if i.endswith('e'):
        print(i)

        
cruze
santafe

name
['creta', 'ciaz', 'cruze', 'santro', 'santafe']
for i in name:
    if len (i) == 5:
        print(i, end=' ')

        
creta cruze 
#print the name which has 6 character

for i in name:
    if len (i) == 6:
        print(i, end=' ')

        
santro 

#Print the name ends with vowels

for i in name:
    if i.endswith('a'):
        print(i)
    elif i.endswith('e'):
        print(i)
    elif i.endswith('o'):
        print(i)
    elif i.endswith('i'):
        print(i)
    elif i.endswith('u'):
        print(i)

        
creta
cruze
santro
santafe

# there is another best ways to do the same

vowels =['a','e','i','o','u']
for i in name:
    for j in vowels:
        if i.endswith(j):
            print(i)

            
creta
cruze
santro
santafe

# In some other way
for i in name:
    if i.endswith('a'or'e'or'i'or'o'or'u'): # will resturn only one value if satisfied
        print(i)

        
creta


# WHILE LOOP:

# checks the every single time and runs the loop till the condition is TRUE
# It is mandate to give the incremental / decremental value in while loop

a = 6
while a > 0:
    print(a)
    a-=1

    
6
5
4
3
2
1

'''# FLOW CONTROL STATEMENTS
Jump / Transfer Statements :
...    - break       #STOP
...    - continue    #SKIP
...    - pass        #DO NOTHING

break ------> it terminates the execution of a loop when certain condition is met
continue ---> Skips the current iteration and moves to the next iteration
pass -------> Does nothing
'''
'# FLOW CONTROL STATEMENTS\nJump / Transfer Statements :\n...    - break       #STOP\n...    - continue    #SKIP\n...    - pass        #DO NOTHING\n\nbreak ------> it terminates the execution of a loop when certain condition is met\ncontinue ---> Skips the current iteration and moves to the next iteration\npass -------> Does nothing\n'

#Break :

for i in range(10)
SyntaxError: expected ':'

for i in range(10):
    print(i,end =' ')   # Print first
    i == 5:
        
SyntaxError: invalid syntax
for i in range(10):
    print(i,end =' ')   # Print first
    if i == 5:
        break

    
0 1 2 3 4 5 
for i in range(8):
    print(i,end =' ')   # Print first
    if i == 5:          # Compare next
        break

    
0 1 2 3 4 5 

for i in range(8):
    if i == 5:              # Compare first
        print(i,end =' ')   # Print next
        break

5 

for i in range(8):
    if i == 5:          # Compare first
        break
    print(i,end =' ')   # Print next

    
0 1 2 3 4 

#CONTINUE:

#Display number from 1 to 10 and skip number 5 and 7
for i in range(1,11,1):
    if i==5 or i==7:
        continue
    print(i)

    
1
2
3
4
6
8
9
10

name
['creta', 'ciaz', 'cruze', 'santro', 'santafe']

#Display name whose count is not exactly 5 using FCS
for i in name:
    if len(i)==5:
        continue
    print(i)
    
ciaz
santro
santafe


#Display name whose count is not exactly 5 using without FCS

for i in name:
    if len(i)!=5:
        print(i)

        
ciaz
santro
santafe

#------------------------------------------------------
for i in range (100):
    if i==60:
        break
    print(f'age is {i} work hard')

    
age is 0 work hard
age is 1 work hard
age is 2 work hard
age is 3 work hard
age is 4 work hard
age is 5 work hard
age is 6 work hard
age is 7 work hard
age is 8 work hard
age is 9 work hard
age is 10 work hard
age is 11 work hard
age is 12 work hard
age is 13 work hard
age is 14 work hard
age is 15 work hard
age is 16 work hard
age is 17 work hard
age is 18 work hard
age is 19 work hard
age is 20 work hard
age is 21 work hard
age is 22 work hard
age is 23 work hard
age is 24 work hard
age is 25 work hard
age is 26 work hard
age is 27 work hard
age is 28 work hard
age is 29 work hard
age is 30 work hard
age is 31 work hard
age is 32 work hard
age is 33 work hard
age is 34 work hard
age is 35 work hard
age is 36 work hard
age is 37 work hard
age is 38 work hard
age is 39 work hard
age is 40 work hard
age is 41 work hard
age is 42 work hard
age is 43 work hard
age is 44 work hard
age is 45 work hard
age is 46 work hard
age is 47 work hard
age is 48 work hard
age is 49 work hard
age is 50 work hard
age is 51 work hard
age is 52 work hard
age is 53 work hard
age is 54 work hard
age is 55 work hard
age is 56 work hard
age is 57 work hard
age is 58 work hard
age is 59 work hard
