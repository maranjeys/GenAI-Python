Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #python Tokens :
... # It means python LANGUAGE COMPONENTS
... 
... #Types:
... # identifiers
... # literals
... # operators
... # keywords
... # comments
... # quotations
... 
... # IDENTIFIERS:
... 
... # Identifier means VARIABLES / VALUE CONTAINERS
... # Identifier in python are like functions / class / modules...
... 
... # Rules:
... 
... # Identifiers cannot be a keyword, built in function
... # Identifiers cannot start with numbers
... # Identifiers can start with alphabets, _
... 
>>> name = 'ai'
>>> city = 'Chennai'
>>> age  = 27
... 
#literals :

# checking the exact datatype of a value stored in an identifier

type(name)
<class 'str'>
type(city)
<class 'str'>
type(age)
<class 'int'>
type(29.30)
<class 'float'>

#Identifiers types:
    # private identifiers - Starts with _ ( Single underscore)
    # strong private identifiers - Starts with __ ( Single underscore)
    # magical method identifiers(starts and ends with __)

_name = 'Maran'  #Private

__name = 'Jeys' #Strong

a = 20

b = 80
a.__add__(b)
SyntaxError: multiple statements found while compiling a single statement
a = 20
b = 80
a.__add__(b)
100
a.__add__(b) #magical method identifiers
100


# Operators:
# arithmetic operators (+ - * / % //)
# logical operators(and or not)
# relational operator(> >= < <= == !=)
# assignment operator(= += -= *= /= %= //=)
# membership operator(in not in)
# identity operators(is is not)

# Identity operators(is, is not)
a = 100
b = 200
a is b
False
a is not b
True

# membership operator(in not in)
'm' in 'Maran'
False
'm' in 'maran'
True
'r'not in 'maran'
False

#Arithemtic operators(+ - * / % //)
a
100
=
a+b
300
a-b
-100
a*b
20000
b/a
2.0
b//a #floor or integer division - return only Quotient
2
b%2 # modulo division - returns only remainder
0

#To return both quotient & remainder - user " divmod"
divmod(36,6)
(6, 0)
divmod(35,4)
(8, 3)

# logical operators(and or not)
a = 40
b = 60
a==40 or b==30
True
a==20 and b==30
False
a==40 and b==60
True
a is 40
True
b is not 60
False
b is 60 and a is 30
False
b is not 30 and a is 40
True
a is 40 or b is not 50
True
a != 50
True


# Relational operators

mj = 30
Maran = 50
mj>maran
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    mj>maran
NameError: name 'maran' is not defined. Did you mean: 'Maran'?
mj>Maran
False
20==20
True
30<30
False


a = 30 # Means "Symbolic Notation"
a is 30 # Means " Logical Representation"
True


# Assignment operators (= += -= *= /= %= //=)

# --> unlike other operators, assignment operators keep on UPDATING the original value all time

a = 10
a
10
a+=30 # a = a+30
a
40
a-=20 # a = a-20

a
20
a*=5 #a = a*4
a
100
a/=10 # a = a/10
a
10.0
a = int(a)
a
10
a//=3 #a = a//3
a
3
a%=2 a = a%2
SyntaxError: invalid syntax
a%=2 #a = a%2
a
1

#keywords:
# keyword means reserved words with a specific meaning
# keywords are represented in orange color

help('keywords')

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

# looping statements ---> for / while
# decision making stmts ---> if / else / elif
# flow control statements ---> break / continue / pass
# user defined functios ----> def / return / yield
# oops                  ----> class / del /
# exception handling    ----> try / except / finally
# boolean logic values  ----> True / False
# modules programming   ----> import / from / as
# logical operator      ----> and / or / not
# file handling         ----> with

# comments and quotations:
# 1.Single line comments -  anything in the #hash is single line comment
# 2.Multi line comments - anything withing ''' (Triple quotation) --- '''

print('M')
M
'''
print(M)
Print(A)
'''
'\nprint(M)\nPrint(A)\n'
print ('Maran') #outside of multi line comments
Maran
