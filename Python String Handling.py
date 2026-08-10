Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # STRING HANDLING MANAGEMENT
... 
... # categories - 3 types:
... # 1.string operations (indexing / slicing / ranging)
... # 2.string methods (concatenation / repetition / formatting)
... # 3.string supporting functions(string dotted functions)
...  
... # STRING OPERATIONS:
... # string = sequence of characters
... # string are enclosed with quotations
... 
... #Maranjeys
... #012345678 - index position
>>> 
>>> name = 'Maranjeys'
>>> name
'Maranjeys'
>>> # indexing = getting a particular character from a string using its INDEX value
... 
>>> name[0]
'M'
>>> name[1]
'a'
>>> name[2]
'r'
>>> name[3]
'a'
name[4]
'n'
# This process is called STRING TRAVERSING / POSITIVE INDEXING

name = 'maranjs'
name
'maranjs'
# Maranjs
# M a r a n j s
#-7-6-5-4-3-2-1
name[-1]
's'
name[-2]
'j'
# NOTE: space is meaningful in python as it takes a index value
#These process is called NEGATIVE INDEXING OR REVERSE INDEXING

#SLICING:
#slicing => getting a particular portion from a string using (starting : stopping)
name = 'generative ai'
name
'generative ai'
name[0:3]
'gen'
name[0:9}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
name[0:9]
'generativ'
name[0:13]
'generative ai'

#String Reveres:
name[::-1]
'ia evitareneg'

name = 'maran'
name [0:3]
'mar'
name[-6:-2]
'mar'
name = 'Maranjeys'
name[::2] #prints evert 2nd char from the beginning
'Mrnes'
name[::3]
'Mae'

# RANGING => almost similar to slicing
#slicing process called as "Fetching" -> String fetching

#RANGING:
name
'Maranjeys'
name[:5]
'Maran'
name[5:] #from 5th char till the end
'jeys'
name[2:7]
'ranje'

name = 'RANGING METHODS'
name[-7:-14]
''
name[-14:-7]
'ANGING '
name[13:9]
''
name[13:9] #should be [Min:max]
''
name[13:9:-1]
'DOHT'

# String methods(concatenation / repetition / formatting)
#Concatenation:

name = 'maran'
age = 27
city = kodaikanal
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    city = kodaikanal
NameError: name 'kodaikanal' is not defined
name = 'maran'
age = 27
city = 'kodaikanal'
name+city
'marankodaikanal'
name +str(age)
'maran27'
'20' + '20'
'2020'
'2020'
'2020'

# Repetition:
name*5
'maranmaranmaranmaranmaran'

#Formatting
name = 'maran'age = 27city = 'kodaikanal'
SyntaxError: invalid decimal literal
name = 'maran'
age = 27
city = 'kodaikanal'
print('my name is {0} from {1} aged {2}')
my name is {0} from {1} aged {2}
print('my name is {0} from {1} aged {2}'.format(name,city,age))
my name is maran from kodaikanal aged 27

# ------The above is Manual formatting ------

# Automated formatting:
print('my name is %s from %s aged %d' % (name,city,age))
my name is maran from kodaikanal aged 27
print('my name is %s from %s aged %s' % (name,city,age))
my name is maran from kodaikanal aged 27

# General formatting:
print('name is',name)
name is maran
print('name is',name,'hometown is',city)
name is maran hometown is kodaikanal

#formatted string (fstring)
print(f'my name is {name} and the age is {age}')
my name is maran and the age is 27

#3.STRING SUPPORTING FUCTIONS (dedicated string methods) -->String Dotted Function

'maran'.capitalize()
'Maran'
'maran'.count()
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    'maran'.count()
TypeError: count expected at least 1 argument, got 0
'maran'.upper()
'MARAN'
'maRAn'.casefold()
'maran'
name = 'maranjs'
name.capitalize()
'Maranjs'
name.find('r')
2
'Gen Ai'.center(40)
'                 Gen Ai                 '
'Python'.ljust(30)
'Python                        '
'Python'.rjust(30)
'                        Python'
'python for gen ai'.title()
'Python For Gen Ai'
'130'.zfill(10)
'0000000130'
'130'.center(20)
'        130         '
'150'.ljust(10,'*')
'150*******'
'150'.rjust(10,'*')
'*******150'
'  maran js  '.strip() #Removes White Space
'maran js'

'maranjs'.find('e') #out of string char
-1
'maranjs'.index('e') # Also out of stringchar but o\p differs
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    'maranjs'.index('e') # Also out of stringchar but o\p differs
ValueError: substring not found

#Maran -> string
#Mar -> Sub staring
#M -> character string

'maranjs'.count('a')
2
'maranjs'.endswith('s')
True
'maranjs'.startswith('a')
False

'-'.join(['J','Maran','Jeys'])
'J-Maran-Jeys'
'J-Maran-Jeys'.partition('-')
('J', '-', 'Maran-Jeys')
'Maran Jeys'.partition(' ')
('Maran', ' ', 'Jeys')
'Maran Jeys'.removesuffix('s')
'Maran Jey'
'Maran Jeys'.removeprefix('Ma')
'ran Jeys'
'Maran Jeys'.strip('n')
'Maran Jeys'
'Maran Jeys'.strip('M')
'aran Jeys'
'Maran Jeys'.strip('s')
'Maran Jey'
'Maran Jeys'.partition('an')
('Mar', 'an', ' Jeys')
'MaraM'.strip('M')
'ara'
#Strip  - not only removes white space but also removes character in a string that starts and ends with the same character

'Maran Jeys'.replace('Jeys','Js')
'Maran Js'
'Maran'.index('a')
1
'Jmaran'.index('a')
2
'Jmaran'.rindex('a')
4
'Maran Jeys'.isalnum() #Alnum -> Anything within ' ' but except space
False
'MaranJeys'.isalnum()
True
'Maran Jeys'.isdecimal()
False
'Maran Jeys'.isidentifier()
False
'maran'.islower()
True
'Maran Jeys'.isspace() #There not only space
False
'Maran Jeys'.isprintable()
True
'Maran Jeys'.isascii()
True
