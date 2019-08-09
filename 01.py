Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(100)
100
>>> print(20 + 5)
25
>>> print()

>>> print("Hello Python")
Hello Python
>>> print("20 + 5")
20 + 5
>>> print(
	10 + 30
	)
40
>>> print(hello)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(hello)
NameError: name 'hello' is not defined
>>> 
================== RESTART: D:/Py1908/01_01_HelloPython.py ==================
안녕하세요 파이썬
제 이름은 성연철 입니다
2019
>>> 
================== RESTART: D:/Py1908/01_01_HelloPython.py ==================
안녕하세요 파이썬
제 이름은 성연철 입니다
2019
>>> type(100)
<class 'int'>
>>> type(3.14)
<class 'float'>
>>> type(100)
<class 'int'>
>>> type(100.0)
<class 'float'>
>>> type("Python")
<class 'str'>
>>> 
===================== RESTART: D:/Py1908/01_02_Basic1.py =====================
>>> 
===================== RESTART: D:/Py1908/01_02_Basic1.py =====================
<class 'int'>
>>> 
===================== RESTART: D:/Py1908/01_02_Basic1.py =====================
<class 'int'>
>>> 100 + 20
120
>>> 120 - 5 + 4
119
>>> 120 * 2
240
>>> 120 / 2
60.0
>>> type(120 * 2)
<class 'int'>
>>> type(120 / 2)
<class 'float'>
>>> 120 // 2
60
>>> type(120 // 2)
<class 'int'>
>>> 120 // 2.0
60.0
>>> 3.4 / 1.1
3.0909090909090904
>>> 3.4 // 1.1
3.0
>>> 4 + 5 * 2
14
>>> (4 + 5) * 2
18
>>> 5 / 0
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    5 / 0
ZeroDivisionError: division by zero
>>> 13 % 3
1
>>> 12.5 % 4.1
0.20000000000000107
>>> 2 ** 4
16
>>> 2 ** 8
256
>>> 2 ** 16
65536
>>> 2 ** -1
0.5
>>> 2 ** -2
0.25
>>> 2 ** 0.5
1.4142135623730951
>>> "Life is Too Short"
'Life is Too Short'
>>> ''' Life is Too Short '''
' Life is Too Short '
>>> print("He says "Hi!"")
SyntaxError: invalid syntax
>>> print('He says "Hi!"')
He says "Hi!"
>>> print("She's Gone")
She's Gone
>>> print("""He says "I'm so tired" """)
He says "I'm so tired" 
>>> print("""He says "I'm so tired" """)
He says "I'm so tired" 
>>> 
===================== RESTART: D:/Py1908/01_02_Basic1.py =====================
<class 'int'>
>>> "Hello" + "Python"
'HelloPython'
>>> "Hello" + " : " + "파이썬"
'Hello : 파이썬'
>>> 12 + "monkeys"
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    12 + "monkeys"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> "-" * 20
'--------------------'
>>> 
===================== RESTART: D:/Py1908/01_02_Basic1.py =====================
<class 'int'>
Traceback (most recent call last):
  File "D:/Py1908/01_02_Basic1.py", line 44, in <module>
    printf("-" * 40)
NameError: name 'printf' is not defined
>>> 
===================== RESTART: D:/Py1908/01_02_Basic1.py =====================
<class 'int'>
----------------------------------------
>>> len("안녕하세요")
5
>>> len("hello")
5
>>> a = 10
>>> a
10
>>> print(a)
10
>>> type(a)
<class 'int'>
>>> a * 100
1000
>>> 
