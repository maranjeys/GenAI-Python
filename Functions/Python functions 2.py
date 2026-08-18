Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # USER DEFINED FUNCTIONS:
>>> #User defined fuction:
... #---------------------
... #A function where the paramaters and arguments are defined by the user is called as user defined function(UDF)
... 
... # use "def" keyword at the beginning followed by a meaningful functions enclosed with ()
... 
... # invoke line indentation using :
... 
... # create logic for the function and return the output
... 
... # call the function to get the output
... 
>>> # TYPES OF ARGUMENTS IN UDF:
>>> #---------------------------
>>> # 1. default args
>>> # 2. positional args
>>> # 3. Keyword args
>>> # 4. arbitrary args
>>> 
>>> # 1. default args -> function to be created with parameters & default args
>>> 
>>> def bike(brand,model,price):
...     print(f'bike brand is {brand} model is {model} price is {price}')
... 

bike('bajaj','platina',89000)
bike brand is bajaj model is platina price is 89000

# here,
# brand, model, price ---> parameters
# bajaj, platina, 89000 ---> arguments


# default args

def car(brand='ford', model='endeavour', price=2800000):
    print(f'car brand is {brand} car model is {model} car price is {price}')

car()
car brand is ford car model is endeavour car price is 2800000

# By using default args,
                   # 1. We can call the func with parameters that have pre-assigned default values
                   
                   # 2. We can pass the new arguments too
                   
car('Toyota','Hyrider','1500000') # Just passing the new arguments
car brand is Toyota car model is Hyrider car price is 1500000

# Real time application of default args: -> ATM fast cash withdrawal -> Suggestion of amount based on previous transaction or 100,500, 2000 default amount to withdraw

# Positional Args:

# => User / Developer has to remember the order of parameters so that he can send arguments

car()
car brand is ford car model is endeavour car price is 2800000
car('skoda','Kylaq')
car brand is skoda car model is Kylaq car price is 2800000
car('','Kylaq','15lks')
car brand is  car model is Kylaq car price is 15lks

# Using positional args -> we can change the arguments, but cannot change the position of the args.So that key word args takes place

# 3. Keyword args:
#           => No need to follow the order of parameter
#           => we can change any parameter value regardless of order
car()
car brand is ford car model is endeavour car price is 2800000
car(price='20lks')
car brand is ford car model is endeavour car price is 20lks
car(model='Punch',brand='TATA')
car brand is TATA car model is Punch car price is 2800000
# Any specific paramenter values can be passed regardless of order
# But, output will be ordered

# 4. arbitrary args: [ Company side - broadcast msg]

def greet(*students):
    for i in students:
        print(f' Hi {i}, today is holiday due to heavy rainfall')

            
greet('Maran','Shru','Ishu','jey','priya','Jeys')
 Hi Maran, today is holiday due to heavy rainfall
 Hi Shru, today is holiday due to heavy rainfall
 Hi Ishu, today is holiday due to heavy rainfall
 Hi jey, today is holiday due to heavy rainfall
 Hi priya, today is holiday due to heavy rainfall
 Hi Jeys, today is holiday due to heavy rainfall

#------------------------------------------------------------------
 
# Built-in Functions:
#--------------------
# => Represented in PURPLE color
# => Also called READYMADE FN / STEADY STATE FN / SHIPPED FN

help('builtins')

import builtins
dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'PythonFinalizationError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_IncompleteInputError', '__build_class__', '__builtins__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

# Important builtin functions :---
       #abs - absolute, Bin - binary, Bool - True or false, chr, dir - director, divmod,
# enumerate, eval - evaluate, exit, id, input, len, min, max, range, reversed, round, sorted, sum, type

abs(-5) # Absolute value
5
bin(10)
'0b1010'
bin(15)
'0b1111'
bool(1)
True
bool(-3) # Execept 0 is True
True
char(65)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    char(65)
NameError: name 'char' is not defined. Did you mean: 'car'?
chr(65)
'A'
ord(a)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    ord(a)
NameError: name 'a' is not defined
ord(65)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    ord(65)
TypeError: ord() expected string of length 1, but int found
Ord('A')
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    Ord('A')
NameError: name 'Ord' is not defined. Did you mean: 'ord'?
ord('A')
65
ord('a')
97
chr(97)
'a'
divmod(30,7)
(4, 2)
for i in 'maran':
    print(i)

    
m
a
r
a
n
for i in enumerate('Maran Jeys Jeyamurugan') # It gives the index of the string
SyntaxError: expected ':'

for i in enumerate('Maran Jeys Jeyamurugan'): # It gives the index of the string
    print(i)

    
(0, 'M')
(1, 'a')
(2, 'r')
(3, 'a')
(4, 'n')
(5, ' ')
(6, 'J')
(7, 'e')
(8, 'y')
(9, 's')
(10, ' ')
(11, 'J')
(12, 'e')
(13, 'y')
(14, 'a')
(15, 'm')
(16, 'u')
(17, 'r')
(18, 'u')
(19, 'g')
(20, 'a')
(21, 'n')
# this concept comes in pandas ( Intrinsic indexing & Extrinsic indexing )

# enumerate --> Means "Passing through"
'20'+'30'
'2030'
'20+30'
'20+30'
eval('20+30')
50
eval('20*30')
600
eval('1.5* 4.7')
7.050000000000001
#It evaluates the value eventhough it is string
eval('1*mj')
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    eval('1*mj')
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'mj' is not defined
eval('mj+js')
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    eval('mj+js')
  File "<string>", line 1, in <module>
    __import__('idlelib.run').run.main(True)
NameError: name 'mj' is not defined
'mj'*5
'mjmjmjmjmj'
exit()
len('Maran')
5
min(12,20,24,10)
10
max(12,20,24,10)
24
sum(12,20,24,10) # Allows only 2 args. Instead give as list
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    sum(12,20,24,10) # Allows only 2 args. Instead give as list
TypeError: sum() takes at most 2 arguments (4 given)
sum([12,20,24,10]) # Instead give as list
66
sum([12,20,24,10],[100])
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    sum([12,20,24,10],[100])
TypeError: can only concatenate list (not "int") to list
pow(12,2)
144
12**2
144

def sqr(num):
    return num**2:
        
SyntaxError: invalid syntax
def sqr(num):
    return num**2
sqr(13)
SyntaxError: invalid syntax
sqr(13)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    sqr(13)
NameError: name 'sqr' is not defined. Did you mean: 'str'?
def sqr(num):
    return num**2

sqr(13)
169
sqr(15)
225
def sqrt(num):
    return num**0.5

sqrt(5)
2.23606797749979
sqrt(10)
3.1622776601683795

for i in reversed ('Maranjs'):
    print(i,end = ' ')

    
s j n a r a M 
sorted('Maranjs')
['M', 'a', 'a', 'j', 'n', 'r', 's']
sorted('MARANJS')
['A', 'A', 'J', 'M', 'N', 'R', 'S']
sorted('Maranjs')[::-1]
['s', 'r', 'n', 'j', 'a', 'a', 'M']
round(15.5)
16
round(15.4)
15
round(1.5)
2
round(6.5)
6
round(5.6)
6
round(6.9)
7

# maran ---> hexadecimal value ---> binary
for i in 'maran':
    print(i,'--->',ord(i),bin(ord(i))) # here used ord(i) since string is in small

    
m ---> 109 0b1101101
a ---> 97 0b1100001
r ---> 114 0b1110010
a ---> 97 0b1100001
n ---> 110 0b1101110
for i in 'MARAN':
    print(i,'--->',ord(i),bin(ord(i)))

    
M ---> 77 0b1001101
A ---> 65 0b1000001
R ---> 82 0b1010010
A ---> 65 0b1000001
N ---> 78 0b1001110
for i in 'MARAN':
    print(i,'--->',ord(i),bin(i))

    
Traceback (most recent call last):
  File "<pyshell#146>", line 2, in <module>
    print(i,'--->',ord(i),bin(i))
TypeError: 'str' object cannot be interpreted as an integer
