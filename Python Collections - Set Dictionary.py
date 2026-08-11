Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> # PYTHON COLLECTIONS - Set/ Dictionary
>>> 
>>> #SET:
>>> # set is an unordered collection of data items
... # set values are unindexed
... # set never supports duplicates
... # popping allowed from beginning to end
>>> # set accepts heterogeneous value
>>> # set is enclosed with {values} with braces
>>> 
>>> bike = {'ronin', 'himalayan','duke','r15v3', 'classic350'}
>>> type(bike)
<class 'set'>
>>> num = {10,20,30,40,50}
>>> num # Set values will be unordered
{50, 20, 40, 10, 30}
>>> 
>>> num
{50, 20, 40, 10, 30}
>>> # Once it takes an order, then the same order will be followed by set
>>> 
>>> bike
{'duke', 'classic350', 'himalayan', 'r15v3', 'ronin'}
>>> bike
{'duke', 'classic350', 'himalayan', 'r15v3', 'ronin'}

a = {1,2,3,4,5}
b = {4,5,6,7,8}
a
{1, 2, 3, 4, 5}
b
{4, 5, 6, 7, 8}
c = {9,10,11,12,13}
c
{9, 10, 11, 12, 13}
# Only numbers are in ordered as same as provided input

a.add(5) # Set never accespts duplicate values
a
{1, 2, 3, 4, 5}
b.add(6)
b
{4, 5, 6, 7, 8}
a.intersection(b)
{4, 5}

a.difference(b)
{1, 2, 3}
b.difference(a) # b-a
{8, 6, 7}
a.difference_update(b) # The difference value will be updated in a
a
{1, 2, 3}

a.pop() # Removes value from 1st to last
1
a
{2, 3}
a.add(4)
a.add(5)
a
{2, 3, 4, 5}
a.union(b) # Provide common in a with all values in b
{2, 3, 4, 5, 6, 7, 8}
# a.union(b) => It combines all the unique elements from both sets

d = c.union(b)
d
{4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

a.isdisjoint(b) # Don't have common element?
False
a.issubset(b)
False
d.issuperset(b)
True
d.issuperset(c)
True
d.issuperset(a)
False

a.discard(4) # Removes a specific element from a set
a
{2, 3, 5}
a.remove(5)
a
{2, 3}
a.discard(6)
a
{2, 3}
a.remove(6)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a.remove(6)
KeyError: 6

# a.discard(6) => It does nothing
# a.remove(6)  => Gives KeyError ( 6 doesn't exist in the set)

#---------------------------------------------------------------------------------------------------

# DICTIONARY:

# dictionary is not indexed
# dictionary ordered collection of data items
# instead of indexing, dict follows {key:value} as a paired items
# duplicate values are not followed
# popping allowed as usual

car = {'brand':'TOYOTA', 'model':'Taisor', 'cartype':'suv', 'price':1000000}
type(car)
<class 'dict'>
car1 = {'brand':'TOYOTA', 'model':'TOYOTA'}

car[0] #dictionary is not indexed
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    car[0] #dictionary is not indexed
KeyError: 0
car['brand']
'TOYOTA'
car['model']
'Taisor'
car['price']
1000000
car2 = {'brand':'TOYOTA', 'brand':'TOYOTA'}
car2
{'brand': 'TOYOTA'}
car1
{'brand': 'TOYOTA', 'model': 'TOYOTA'}
car['model']= 'Hyrider'
car
{'brand': 'TOYOTA', 'model': 'Hyrider', 'cartype': 'suv', 'price': 1000000}

# List
a
{2, 3}
b
{4, 5, 6, 7, 8}
a.add(4)
a.add(5)
a
{2, 3, 5, 4}
b
{4, 5, 6, 7, 8}
a.intersection(b) # Common elements GO
{4, 5}
a.symmetric_difference(b)   # Common elements GO
{2, 3, 6, 7, 8}
\
a.union(b) ## Common elements STAY
{2, 3, 4, 5, 6, 7, 8}
#

car.keys()
dict_keys(['brand', 'model', 'cartype', 'price'])
car.values()
dict_values(['TOYOTA', 'Hyrider', 'suv', 1000000])
car.items()
dict_items([('brand', 'TOYOTA'), ('model', 'Hyrider'), ('cartype', 'suv'), ('price', 1000000)])
car.pop('price')
1000000
car
{'brand': 'TOYOTA', 'model': 'Hyrider', 'cartype': 'suv'}
car.get('model')
'Hyrider'
car['brand']
'TOYOTA'
car.get('brand')
'TOYOTA'
car.popitem() #Removes last value
('cartype', 'suv')
car
{'brand': 'TOYOTA', 'model': 'Hyrider'}

#How to make a set as frozen?
a
{2, 3, 5, 4}
a = frozenset(a)
# Now if we put a. then "add, remove, discard options will not be available
