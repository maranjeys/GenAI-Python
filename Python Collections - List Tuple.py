Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> # PYTHON COLLECTIONS - List / Tuple / Set/ Dictionary
>>> #-> Called as Python Native datatypes / python collections / python NON PRIMITVE DATATYPES
... # Primitive datatypes:- String/Float/Int/Complex/Boolean
... # Non primitive datatypes --> list / tuple / set / dict
>>> name='maran'
>>> type(name)
<class 'str'>
>>> name = 'maran','jeys'
>>> type(name)
<class 'tuple'>
>>> name = ['maran','jeys']
>>> type(name)
<class 'list'>
>>> name = {'maran','jeys'}
>>> type(name)
<class 'set'>
>>> name = {'first_name':'maran','last_name':'jeys']
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> name = {'first_name':'maran','last_name':'jeys'}
>>> type(name)
<class 'dict'>
>>> 
>>> # LIST:
... 
# enclosed with []
# list contains ordered collection of data items
# list values are indexed
# values are mutable and changeable
# list supports duplicate values
# list contains hetrogenous values

car = ['creta','civic','santro','wagonr','creta','beat']
type(car)
<class 'list'>
car[0]
'creta'
car[1]
'civic'
car[0]==car[4]
True
car[0] = 'polo' #vales are changing temporarily in Non-primitive vs Primitive data type
car
['polo', 'civic', 'santro', 'wagonr', 'creta', 'beat']
# car[0] = 'polo' => values are changing "permanently" in Non-primitive vs Primitive data type
#Non - Primitive data types are called "COLLECTIONS"

car[1:4]
['civic', 'santro', 'wagonr']
car[:3]
['polo', 'civic', 'santro']
car[3:]
['wagonr', 'creta', 'beat']
#------------------------------------------
# list methods / list supporting functions / list operations
car
['polo', 'civic', 'santro', 'wagonr', 'creta', 'beat']
car.append('swift')#Using append, we can add only one value in the list at the end
car
['polo', 'civic', 'santro', 'wagonr', 'creta', 'beat', 'swift']

car.clear() #clears the data from the list of car
car
[]
car.append('polo') #only one value
car,exten(['civic','santro','wagonr','creta']) ##Using extend, we can add multiple value in the list by using only one list
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    car,exten(['civic','santro','wagonr','creta']) ##Using extend, we can add multiple value in the list by using only one list
NameError: name 'exten' is not defined. Did you mean: 'exec'?
car,extend(['civic','santro','wagonr','creta']) ##Using extend, we can add multiple value in the list by using only one list
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    car,extend(['civic','santro','wagonr','creta']) ##Using extend, we can add multiple value in the list by using only one list
NameError: name 'extend' is not defined
car.extend(['civic','santro','wagonr','creta']) ##Using extend, we can add multiple value in the list by using only one list
car
['polo', 'civic', 'santro', 'wagonr', 'creta']
car.extend(['civic','santro'],['wagonr','creta']) #
KeyboardInterrupt
car.extend(['ciaz','civic','taigun'],['tiguan','rapid'])# cannot add 2 list values
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    car.extend(['ciaz','civic','taigun'],['tiguan','rapid'])# cannot add 2 list values
TypeError: list.extend() takes exactly one argument (2 given)
car
['polo', 'civic', 'santro', 'wagonr', 'creta']
car.count('swift')
0
car.count('polo')
1
car.index(3)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    car.index(3)
ValueError: 3 is not in list
car.index('creta')
4
car[3]
'wagonr'
car.insert(1,'alto') #It inserts the value at the given index(1)
car
['polo', 'alto', 'civic', 'santro', 'wagonr', 'creta']


car[0]= 'Omni' # To replace the value, but no .replace available
car
['Omni', 'alto', 'civic', 'santro', 'wagonr', 'creta']
car.remove('santro')
car # To remove the specific value
['Omni', 'alto', 'civic', 'wagonr', 'creta']
car.pop(3) #To remove the specific value
'wagonr'
car #wagonr has to be removed from car
['Omni', 'alto', 'civic', 'creta']
car.pop() # It removes the last value
'creta'
car
['Omni', 'alto', 'civic']
car.reverse() #Like string revers [::-1]
car
['civic', 'alto', 'Omni']
car.pop('civic')  # Not allows direct value to remove through pop
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    car.pop('civic')  # Not allows direct value to remove through pop
TypeError: 'str' object cannot be interpreted as an integer
car.sort() # To sort the car
car
['Omni', 'alto', 'civic']
car
['Omni', 'alto', 'civic']
car.sort()
car
['Omni', 'alto', 'civic']
car_dup = car
car_dup
['Omni', 'alto', 'civic']
# car_dup = car => Called as "Shallow Copy" - it affects the value if changes are made in duplicate car value
#dup = car.copy() => Called as "Deep Copy" - it doesn't affect the original value of car
car_dup.pop()
'civic'
car_dup
['Omni', 'alto']
car
['Omni', 'alto']
#changes are also affected in original value of car. Instead, we can use dup = car.copy()
dup = car.copy()
dup
['Omni', 'alto']
dup.insert(1,'Seiarra')
dup
['Omni', 'Seiarra', 'alto']
car
['Omni', 'alto']
# Now car values are not affected when using "Deep Copy" method
#----------------------------------------------------------------------------------------------------

# TUPLE:

# tuple is enclosed with ()
# tuple values are also ordered collection
# tuple values are indexed
# tuple values support duplicates
# tuple values are IMMUTABLE

name = ('maran','jeys','genaideveloper,''chenai')
type(name)
<class 'tuple'>
name.append('jeys')
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    name.append('jeys')
AttributeError: 'tuple' object has no attribute 'append'
# Note : Tupe is IMMUTABLE so cannot add or change the value. So it needs conversion to list
name = list(name)
type(name)
<class 'list'>
name.append('jeys')
name
['maran', 'jeys', 'genaideveloper,chenai', 'jeys']
name.count('jeys')
2
name = tuple(name)
type(name)
<class 'tuple'>
# These type changing process is called as "Type Casting"

name2 = (10,20,30)
type(name2)
<class 'tuple'>
name = name + name2
name
('maran', 'jeys', 'genaideveloper,chenai', 'jeys', 10, 20, 30)
