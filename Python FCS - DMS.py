Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> '''
... PYTHON FLOW CONTROL STATEMENTS(FCS) :
... ==============================
... 
... 1. Decision-Making Statements (DMS)
...    - if
...    - if-else
...    - if-elif-else
...    - Nested if
... 
... 2. Looping Statements
...    - for
...    - while
... 
... 3. Jump / Transfer Statements
...    - break
...    - continue
...    - pass
... '''
'\nPYTHON FLOW CONTROL STATEMENTS(FCS) :\n==============================\n\n1. Decision-Making Statements (DMS)\n   - if\n   - if-else\n   - if-elif-else\n   - Nested if\n\n2. Looping Statements\n   - for\n   - while\n\n3. Jump / Transfer Statements\n   - break\n   - continue\n   - pass\n'
>>> 
>>> # DECISION MAKING STATEMENTS:
>>> # if:
# if the given test condition is satisfied then it prints something
# if not satisfied it prints nothing

name = 'Maran Jeys'
if name == 'Maran Jeys':
    print('Your name is',name)

    
Your name is Maran Jeys

# if...else :

# if the given test condition is satisfied then it returns IF block statements
# if not then ELSE block statements

age = 40
if age >= 60:
    print(' SENIOR CITIZEN')
else:
    print('NOT A SENIOR CITIZEN')

    
NOT A SENIOR CITIZEN

# if...elif...else :

# if a single value to be checked with multiple test conditions

# Grade of marks
# 91 - 100 S
# 81 - 90  A
# 71 - 80  B
# 61 - 70  C
# 51 - 60  D
# 50       E
# <50      U

mark = 75
if mark >=91 and mark <=100:
    print('S grade - ',mark)
elif mark>=81 and mark <=90:
    print('A grade - ',mark)
elif mark >=71 and mark <=80:
    print('B grade - ',mark)
elif mark >=61 and mark <=70:
    print('C grade - ',mark)
elif mark >=51 and mark <=60:
    print('D grade - ',mark)
elif mark ==50:
    print('E grade - ',mark)
elif mark <50:
    print('U : Fail - ',mark)
else:
    print('Provide Valid Mark')

    
B grade -  75

# nested if :

# If one test condition is given inside another test condition

age = 22
weight = 50
if age>= 18:
    print('Eligible Age')
    if weight >=50:
        print('Eligible to donate blood')
    else:
        print('Eligibility not met for weight)
              
SyntaxError: unterminated string literal (detected at line 6)
age = 22
              
weight = 40
              
if age>= 18:
    print('Eligible Age')
    if weight >=50:
        print('Eligible to donate blood')
    else:
        print('Eligibility not met for weight')
else:
    print('Age creteria not met')

    
Eligible Age
Eligibility not met for weight

age = 18
weight = 50
if age>= 18:
    print('Eligible Age')
    if weight >=50:
        print('Eligible to donate blood')
    else:
        print('Eligibility not met for weight')
else:
    print('Age creteria not met')

    
Eligible Age
Eligible to donate blood

age = 16
weight = 45
if age>= 18 and weight>=50:
    print('Eligible to donate blood')
    if weight >=50:
        print('Weight cretia met')
    else:
        print('Weight cretia not met')
else:
    print('Age and weight creteria not met')

    
Age and weight creteria not met

age = 16
weight = 45
if age>= 18 or weight>=50:
    print('Eligible to donate blood')
    if weight >=50:
        print('Weight cretia met')
    else:
        print('Weight cretia not met')
else:
    print('Age and weight creteria not met')

    
Age and weight creteria not met

age = 20
weight = 65
if age>= 18 or weight>=50:
    print('Eligible to donate blood')
    if weight >=50:
        print('Weight cretia met')
    else:
        print('Weight cretia not met')
else:
    print('Age and weight creteria not met')

    
Eligible to donate blood
Weight cretia met
age = 20
weight = 45
if age>= 18 or weight>=50:
    print('Eligible to donate blood')
    if weight >=50:
        print('Weight cretia met')
    else:
        print('Weight cretia not met')
else:
    print('Age and weight creteria not met')

    
Eligible to donate blood
Weight cretia not met
