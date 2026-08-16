Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
 # Pattern Program using FOR LOOP
 
for i in range(5):
    print(i,end=' ')

    
0 1 2 3 4 

for i in range(5,0,-1):
    print(i)

    
5
4
3
2
1

for i in range(5,-1,-1):
    print(i)

    
5
4
3
2
1
0

for i in range(1,6):
    for j in range(0,i):
        print(i,end=' ')
    print()

    
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
# Right Angle Triangle

# i --> outer loop --> row printing --> it tells which number to print
# j --> inner loop --> col printing --> it tells how many times to print

for i in range(1,6):
    for j in range(0,i):
        print(j,end=' ') # col printing
    print()

    
0 
0 1 
0 1 2 
0 1 2 3 
0 1 2 3 4 

for i in range(1,6):
    for j in range(0,i):
        print('*',end=' ')
    print()

    
* 
* * 
* * * 
* * * * 
* * * * * 

chr(65)
'A'
chr(97)
'a'
ord(A)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    ord(A)
NameError: name 'A' is not defined
ord('A')
65
ord('a')
97

for i in range(1,6):
    for j in range(0,i):
        print(i+64,end=' ')
    print()

    
65 
66 66 
67 67 67 
68 68 68 68 
69 69 69 69 69 

for i in range(1,6):
    for j in range(0,i):
        print(i+96,end=' ')
    print()

    
97 
98 98 
99 99 99 
100 100 100 100 
101 101 101 101 101 

for i in range(1,6):
    for j in range(0,i):
        print(chr(i+64),end=' ')
    print()

    
A 
B B 
C C C 
D D D D 
E E E E E 

for i in range(1,6):
    for j in range(0,i):
        print(chr(i+96),end=' ')
    print()

    
a 
b b 
c c c 
d d d d 
e e e e e 

for i in range(1,6):
    for j in range(0,i):
        print(chr(j+64),end=' ')
    print()

    
@ 
@ A 
@ A B 
@ A B C 
@ A B C D 

for i in range(1,6):
    for j in range(0,i):
        print(chr(j+65),end=' ')
    print()

    
A 
A B 
A B C 
A B C D 
A B C D E 

for i in range(1,6):
    for j in range(0,i):
        print(chr(j+97),end=' ')
    print()

    
a 
a b 
a b c 
a b c d 
a b c d e 

# rat - number row
# rat - number col
# rat - star
# rat - upper row
# rat - upper col
# rat - lower row
# rat - lower col

# INVERSE RAT:

for i in range(5,0,-1):
    for j in range(0,i):
        print(i,end=' ')
    print()

    
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
for i in range(5,0,-1):
    for j in range(0,i):
        print(j,end=' ') # col printing
    print()

    
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1 
0 

for i in range(5,0,-1):
    for j in range(0,i):
        print('*',end=' ')
    print()

    
* * * * * 
* * * * 
* * * 
* * 
* 

for i in range(5,0,-1):
    for j in range(0,i):
        print(chr(i+64),end=' ')
    print()

    
E E E E E 
D D D D 
C C C 
B B 
A 

for i in range(5,0,-1):
    for j in range(0,i):
        print(chr(j+65),end=' ')
    print()

    
A B C D E 
A B C D 
A B C 
A B 
A 
>>> 
>>> for i in range(5,0,-1):
...     for j in range(0,i):
...         print(chr(i+96),end=' ')
...     print()
... 
...     
e e e e e 
d d d d 
c c c 
b b 
a 
>>> 
>>> for i in range(5,0,-1):
...     for j in range(0,i):
...         print(chr(j+97),end=' ')
...     print()
... 
...     
a b c d e 
a b c d 
a b c 
a b 
a 
