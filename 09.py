Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
==================== RESTART: D:/Py1908/09_01_function.py ====================
>>> 
==================== RESTART: D:/Py1908/09_01_function.py ====================
funcA() 호출
funcB() 호출
funcC() 호출
>>> 
==================== RESTART: D:/Py1908/09_01_function.py ====================
funcA() 호출
funcB() 호출
funcC() 호출
funcC() 리턴
funcB() 리턴
funcA() 리턴
>>> 
==================== RESTART: D:/Py1908/09_01_function.py ====================
funcA() 호출
funcB() 호출
funcC() 호출
funcC() 리턴
funcB() 리턴
funcA() 리턴
------------------------------
aaa() 호출
bbb() 호출
ccc() 호출
aaa bbb ccc
>>> 
==================== RESTART: D:/Py1908/09_01_function.py ====================
funcA() 호출
funcB() 호출
funcC() 호출
funcC() 리턴
funcB() 리턴
funcA() 리턴
------------------------------
aaa() 호출
bbb() 호출
ccc() 호출
aaa bbb ccc
------------------------------
ddd() 호출
aaa() 호출
bbb() 호출
ccc() 호출
('aaa', 'bbb', 'ccc')
>>> 
===================== RESTART: D:/Py1908/09_02_return.py =====================
>>> result
(12, 8, 20, 5.0)
>>> result[0]
12
>>> result[1]
8
>>> 
===================== RESTART: D:/Py1908/09_02_return.py =====================
>>> aa
23
>>> bb
17
>>> cc
60
>>> dd
6.666666666666667
>>> type(oper(10, 2))
<class 'tuple'>
>>> 
===================== RESTART: D:/Py1908/09_02_return.py =====================
>>> 
===================== RESTART: D:/Py1908/09_02_return.py =====================
>>> myFunc2(50)
'100 이하입니다'
>>> 
===================== RESTART: D:/Py1908/09_02_return.py =====================
>>> myFunc2(200)
'100 보다 큽니다'
>>> 
==================== RESTART: D:/Py1908/09_03_practice.py ====================
>>> filter_str("토끼는 바보다")
'**금지어입니다**'
>>> filter_str("토끼는 귀엽다")
'토끼는 귀엽다'
>>> 
==================== RESTART: D:/Py1908/09_03_practice.py ====================
**금지어입니다**
토끼는 빠르다
**금지어입니다**
**금지어입니다**
산토끼 토끼야..
>>> 
==================== RESTART: D:/Py1908/09_04_argument.py ====================
150
>>> 
==================== RESTART: D:/Py1908/09_04_argument.py ====================
50
-50
>>> 
==================== RESTART: D:/Py1908/09_04_argument.py ====================
50
-50
Traceback (most recent call last):
  File "D:/Py1908/09_04_argument.py", line 10, in <module>
    print(func(10)) #?
TypeError: func() missing 1 required positional argument: 'b'
>>> 
==================== RESTART: D:/Py1908/09_04_argument.py ====================
50
-50
Traceback (most recent call last):
  File "D:/Py1908/09_04_argument.py", line 11, in <module>
    print(func(10, 20, 30))  #?
TypeError: func() takes 2 positional arguments but 3 were given
>>> 
==================== RESTART: D:/Py1908/09_04_argument.py ====================
50
-50
학생등록: hong 34 3
>>> 
==================== RESTART: D:/Py1908/09_04_argument.py ====================
50
-50
학생등록: hong 34 3
학생등록: kim 19 1
>>> print("hello", end = "--")
hello--
>>> 
==================== RESTART: D:/Py1908/09_04_argument.py ====================
50
-50
학생등록: hong 34 3
학생등록: kim 19 1
>>> myFunc1(1, 2, 3, 4, 5, 6)
21
>>> myFunc1(1, 2, 3, 4, 5)
15
>>> myFunc1(1, 2, 3, 4)
10
>>> myFunc1(1, 2, 3)
6
>>> myFunc1(1, 2)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    myFunc1(1, 2)
TypeError: myFunc1() missing 1 required positional argument: 'c'
>>> print(10)
10
>>> print(10, 20)
10 20
>>> print(10, 20, 30)
10 20 30
>>> 
==================== RESTART: D:/Py1908/09_04_argument.py ====================
50
-50
학생등록: hong 34 3
학생등록: kim 19 1
>>> add_many(1, 2)
3
>>> add_many(10, 20, 30, 40)
100
>>> add_many(3.14, 12, 100.123)
115.263
>>> add_many()
0
>>> add_many(1)
1
>>> 
==================== RESTART: D:/Py1908/09_04_argument.py ====================
50
-50
학생등록: hong 34 3
학생등록: kim 19 1
>>> print_kwargs(a = 1)
{'a': 1}
>>> print_kwargs(name='Groot', age=150, height=200)
{'name': 'Groot', 'age': 150, 'height': 200}
>>> 
===================== RESTART: D:/Py1908/09_05_global.py =====================
>>> vartest()
1
>>> a = 100
>>> vartest()
100
>>> 
===================== RESTART: D:/Py1908/09_05_global.py =====================
>>> vartest2(500)
500
>>> a
1
>>> 
===================== RESTART: D:/Py1908/09_05_global.py =====================
>>> vartest2(30)
60
>>> a
1
>>> #  https://docs.python.org/3/library/functions.html
# 파이썬의 내장 함수 (Build-in Functions)
# 별도의 import 없이 바로 사용 가능한 함수들.
>>> abs(3)  # 절대값
3
>>> abs(-3)
3
>>> abs(-1.234)
1.234
>>> all([10, 20, 30])  # 모두 '참'이면 True 리턴
True
>>> all([10, 0, 20])
False
>>> 7 // 3
2
>>> 7 % 3
1
>>> divmod(7, 3)
(2, 1)
>>> round(4.6)  # 반 올림
5
>>> round(-4.6)
-5
>>> round(5.678, 2)  # 소숫점 2자리까지 반올림
5.68
>>> sorted([3, 1, 2])  # 정렬값 리턴
[1, 2, 3]
>>> 
