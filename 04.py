Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> animals = ["dog", "cat", "bird"]
>>> animals
['dog', 'cat', 'bird']
>>> type(animals)
<class 'list'>
>>> print(list)
<class 'list'>
>>> print(animals)
['dog', 'cat', 'bird']
>>> animals = [
	"dog",
	"cat",
	"bird",
	"dog"
	]
>>> # 인덱싱(indexing)
#  list 의 데이터 원소는 0 부터 시작!
>>> animals[0]
'dog'
>>> animals[1]
'cat'
>>> animals[2]
'bird'
>>> animals[3]
'dog'
>>> animals[4]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    animals[4]
IndexError: list index out of range
>>> animals
['dog', 'cat', 'bird', 'dog']
>>> animals[-2]
'bird'
>>> # 리스트 원소의 개수는 len() 함수 사용
>>> len(animals)
4
>>> # 리스트에 원소 추가 : append() 함수 사용
>>> animals.append("tiger")
>>> animals
['dog', 'cat', 'bird', 'dog', 'tiger']
>>> # 리스트의 원소 삭제 : del() 함수 사용
>>> del(animals[3])
>>> animals
['dog', 'cat', 'bird', 'tiger']
>>> type(animals[0])
<class 'str'>
>>> score = [10, 20, 30]
>>> type(score[2])
<class 'int'>
>>> score = [35.3, 35.7, 100.33435, 324.234]
>>> person = ['토니', 48, 182.3]
>>> person
['토니', 48, 182.3]
>>> animals
['dog', 'cat', 'bird', 'tiger']
>>> print(animals[0])
dog
>>> animals[0] = 'puppy'   # 리스트 원소 변경 가능
>>> animals
['puppy', 'cat', 'bird', 'tiger']
>>> # 데이터를 변경할수 있는 특성을 -> mutable 이라 함.
>>> a = [1, 2, 3, ['a', 'b', 'c']]
>>> len(a)
4
>>> a[1]
2
>>> a[3]
['a', 'b', 'c']
>>> a[3][2]
'c'
>>> b = [
	[100, 200, 300],[1.1, 2.2, 3.3],[]]
>>> b = [
	[100, 200, 300],
        [1.1, 2.2, 3.3],
        ['a', [777,888,['bbb','ddd','zzz']], 'c']
        
    ]
>>> b
[[100, 200, 300], [1.1, 2.2, 3.3], ['a', [777, 888, ['bbb', 'ddd', 'zzz']], 'c']]
>>> len(b)
3
>>> b[0]
[100, 200, 300]
>>> b[1]
[1.1, 2.2, 3.3]
>>> b[2]
['a', [777, 888, ['bbb', 'ddd', 'zzz']], 'c']
>>> b[2][0]
'a'
>>> b[2][1]
[777, 888, ['bbb', 'ddd', 'zzz']]
>>> b[2][1][1]
888
>>> b[2][1][2][0]
'bbb'
>>> animals
['puppy', 'cat', 'bird', 'tiger']
>>> colors = ["white", "blue", "red"]
>>> colors
['white', 'blue', 'red']
>>> # list 의 +, *  연산
>>> animals + colors
['puppy', 'cat', 'bird', 'tiger', 'white', 'blue', 'red']
>>> animals * 3
['puppy', 'cat', 'bird', 'tiger', 'puppy', 'cat', 'bird', 'tiger', 'puppy', 'cat', 'bird', 'tiger']
>>> # 빈 empty 리스트
>>> e = []
>>> type(e)
<class 'list'>
>>> len(e)
0
>>> e.append(input())
100
>>> e
['100']
>>> e.append(input())
200
>>> e.append(input())
300
>>> e
['100', '200', '300']
>>> # 리스트 원소 전체 삭제
>>> e.clear()
>>> e
[]
>>> # list 의 슬라이싱(slicing )
>>> animals
['puppy', 'cat', 'bird', 'tiger']
>>> animals[0:3]   # 0부터 3 전까지
['puppy', 'cat', 'bird']
>>> animals = animals + ['fish', 'turtle']
>>> animals
['puppy', 'cat', 'bird', 'tiger', 'fish', 'turtle']
>>> animals[1:4]  # 1부터 4 전까지
['cat', 'bird', 'tiger']
>>> animals[:2]   # 처음부 2 전까지
['puppy', 'cat']
>>> animals[3:]    #  3부터 끝까지
['tiger', 'fish', 'turtle']
>>> animals[:]
['puppy', 'cat', 'bird', 'tiger', 'fish', 'turtle']
>>> # list.index(값) : 값으로 인덱스 찾기
>>> animals.index('tiger')
3
>>>  animals.index('gold')
 
SyntaxError: unexpected indent
>>> animals.index('tiger')
3
>>> animals.index('gold')
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    animals.index('gold')
ValueError: 'gold' is not in list
>>> # 특정 원소가 list 에 있는지 여부 -> in 연산자 사용
>>> 'dog' in animals  # 'dog' 가 animals 리스트에 있나요?
False
>>> 'puppy' in animals
True
>>> # list 와 str
#   str.join() 함수 : list --> str 묶어줌.
>>> 
>>> 
>>> animals
['puppy', 'cat', 'bird', 'tiger', 'fish', 'turtle']
>>> ",".join(animals)
'puppy,cat,bird,tiger,fish,turtle'
>>> dd = ['2019', '08', '13']
>>> dd
['2019', '08', '13']
>>> "-".join(dd)
'2019-08-13'
>>> hh = "2019-08-13"
>>> hh
'2019-08-13'
>>> hh.split('-')
['2019', '08', '13']
>>> "100 200 300".split()
['100', '200', '300']
>>> #   list(str) 함수 : str -> list 형변환 함수
>>> str = "animals"
>>> list(str)
['a', 'n', 'i', 'm', 'a', 'l', 's']
>>> #--------------------------------
>>> # tuple
>>> a = 10
>>> b = 20
>>> c = 30
>>> a, b, c
(10, 20, 30)
>>> animals = ("dog", 'cat', 'fish')  # ( ~ )
>>> animals
('dog', 'cat', 'fish')
>>> type(animals)
<class 'tuple'>
>>> people = ('Tom')
>>> people
'Tom'
>>> type(people)
<class 'str'>
>>> # 원소 하나짜리 tuple 만드려면...
>>> people = ('Tom', )
>>> people
('Tom',)
>>> type(people)
<class 'tuple'>
>>> len(animals)   # 튜플 원소의 개수
3
>>> # 인덱싱 동일
>>> animals[0]
'dog'
>>> animals[1]
'cat'
>>> animals[1:]
('cat', 'fish')
>>> country = 'korea', 'japan', 'usa', 'russia'
>>> country
('korea', 'japan', 'usa', 'russia')
>>> type(country)
<class 'tuple'>
>>> # tuple 은 immutable 하다 (데이터 변경 불가)
>>> country[1]
'japan'
>>> country[1] = 'china'
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    country[1] = 'china'
TypeError: 'tuple' object does not support item assignment
>>> country.append('china')
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    country.append('china')
AttributeError: 'tuple' object has no attribute 'append'
>>> del(country[1])
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    del(country[1])
TypeError: 'tuple' object doesn't support item deletion
>>> country = country + ("china", )
>>> country
('korea', 'japan', 'usa', 'russia', 'china')
>>> country = country[:1] + country[2:]
>>> country
('korea', 'usa', 'russia', 'china')
>>> 
>>> #ex)사각형 표현 가로(width) ,  세로 (height)
>>> # 리스트로 하는 경우
>>> rec = [100, 200]
>>> width = rec[0]
>>> height = rec[1]
>>> widh
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    widh
NameError: name 'widh' is not defined
>>> width
100
>>> height
200
>>> #  tuple 의 경우
>>> rec = (333, 500)
>>> width, height = rec
>>> width
333
>>> height
500
>>> width, height = (400, 600)
>>> width, height = height, width
>>> width, height
(600, 400)
>>> #----------------------------
>>> # bool 타입
>>> t1 = True
>>> t1
True
>>> type(t1)
<class 'bool'>
>>> t2 = true
Traceback (most recent call last):
  File "<pyshell#160>", line 1, in <module>
    t2 = true
NameError: name 'true' is not defined
>>> 10 > 5
True
>>> 10 < 5
False
>>> 20 > 20
False
>>> 20 >= 20
True
>>> 20 == 20
True
>>> 20 != 20
False
>>> 20 === '20'
SyntaxError: invalid syntax
>>> t2 = 400 > 200 * 1.5
>>> t2
True
>>> 
