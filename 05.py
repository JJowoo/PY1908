Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> student = {}
>>> student
{}
>>> type(student)
<class 'dict'>
>>> student = {"name":"john", "email":"jj@mail.com"}
>>> student
{'name': 'john', 'email': 'jj@mail.com'}
>>> print(student)
{'name': 'john', 'email': 'jj@mail.com'}
>>> len(student)
2
>>> # len(dict) --> dict 의 key:value 쌍의 개수
>>> student = {
	"name" : "susan",
	"age" : 21,
	"address" : "USA"
	}
>>> student["name"]
'susan'
>>> student["age"]
21
>>> student["address"]
'USA'
>>> student.get("name")
'susan'
>>> student.get("age")
21
>>> student.get("address")
'USA'
>>> animals = ['dog', 'cat', 'bird']
>>> animals[0]
'dog'
>>> animals[10]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    animals[10]
IndexError: list index out of range
>>> student['hobby']
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    student['hobby']
KeyError: 'hobby'
>>> studen.get('hobby')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    studen.get('hobby')
NameError: name 'studen' is not defined
>>> student.get('hobby')
>>> uuu
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    uuu
NameError: name 'uuu' is not defined
>>> uuu = 100
>>> uuu
100
>>> del(uuu)
>>> uuu
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    uuu
NameError: name 'uuu' is not defined
>>> uuu = None
>>> uuu
>>> student
{'name': 'susan', 'age': 21, 'address': 'USA'}
>>> student.get('grade')
>>> student.get('grade', 1)  # grade 란 키가 없으면 기본값 1 사용
1
>>> student['phone'] = '010-1111-2222'  # key-value 추가
>>> student
{'name': 'susan', 'age': 21, 'address': 'USA', 'phone': '010-1111-2222'}
>>> del(student['address'])
>>> student
{'name': 'susan', 'age': 21, 'phone': '010-1111-2222'}
>>> student['name'] = "Michael"
>>> student
{'name': 'Michael', 'age': 21, 'phone': '010-1111-2222'}
>>> # dict 의 value 는 어떠한 타입도 가능!
>>> 
====================== RESTART: D:/Py1908/05_01_dict.py ======================
>>> dict1
{1: 'haha', 2: 'gaga', 3: 'nana'}
>>> 
====================== RESTART: D:/Py1908/05_01_dict.py ======================
>>> dict2
{'one': (1, 2, 30), 'two': [10, 20, 3.14], 'three': {0: 'abc', 1: 'def', 3: 'ghi'}}
>>> dict2["one"]
(1, 2, 30)
>>> dict2["one"][2]
30
>>> dict2["three"]
{0: 'abc', 1: 'def', 3: 'ghi'}
>>> dict2["three"][1]
'def'
>>> 
====================== RESTART: D:/Py1908/05_01_dict.py ======================
>>> dict2["three"][False][1]
'b'
>>> 
====================== RESTART: D:/Py1908/05_01_dict.py ======================
Traceback (most recent call last):
  File "D:/Py1908/05_01_dict.py", line 53, in <module>
    [10, 20, 30] : "gkgk"
TypeError: unhashable type: 'list'
>>> # dict.keys(), dict.value() 함수
>>> student
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    student
NameError: name 'student' is not defined
>>> dict1
{1: 'haha', 2: 'gaga', 3: 'nana'}
>>> dict1.keys()
dict_keys([1, 2, 3])
>>> dict1.values()
dict_values(['haha', 'gaga', 'nana'])
>>> 10 in (10, 20, 30)
True
>>> 100 in [10, 20, 30]
False
>>> dict1
{1: 'haha', 2: 'gaga', 3: 'nana'}
>>> 1 in dict1
True
>>> 4 in dict1
False
>>> dict1.keys()
dict_keys([1, 2, 3])
>>> 1 in dict1.keys()
True
>>> 4 in dict1.keys()
False
>>> 'haha' in dict1.values()
True
>>> 'nana' in dict1.values()
True
>>> 'hoho' in dict1.values()
False
>>> #----------------------------
>>> # sum() 함수
>>> score = [78, 89, 43, 12]
>>> sum(score)
222
>>> 
