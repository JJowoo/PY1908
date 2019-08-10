Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 8/9 일 강의 내용이 저장이 안되어 재작성후 업로드 합니다.
>>> """
    변수 이름 사용 가능
        알파벳, 숫자, _ , 
    불가능
        숫자로 시작하면 안됨.
        띄어쓰기 안됨.

    변수명은 대소문자 구분한다!!!
    예약어 사용 불가  ex) return
"""

'\n    변수 이름 사용 가능\n        알파벳, 숫자, _ , \n    불가능\n        숫자로 시작하면 안됨.\n        띄어쓰기 안됨.\n\n    변수명은 대소문자 구분한다!!!\n    예약어 사용 불가  ex) return\n'
>>> # 사용 가능 변수
>>> a = 10;
>>> abc1999 = 100;
>>> hello_world = 200;   # 밑줄 (_) 사용 가능
>>> # 사용 불가 변수
>>> 2000bbb = 100;   # 숫자로 시작할수 없다!
SyntaxError: invalid syntax
>>> my name = 'john';   # 변수명에 공백 넣을수 없다
SyntaxError: invalid syntax
>>> return = 1000;
SyntaxError: invalid syntax
>>> # ↑ 키워드 사용 불가
>>> __this_year__  = 2019    # 밑줄로 시작하는 변수는 가능
>>> 
>>> # 변수는 대소문자 구분한다!
>>> myname = 'john'
>>> MyName = 'susan'
>>> print(myname, MyName)
john susan
>>> print(Myname)   # 없는 변수다!
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(Myname)   # 없는 변수다!
NameError: name 'Myname' is not defined
>>> # 변수 없애기 :  del() 사용
>>> del(myname)    # 변수 myname 제거
>>> print(myname)   # 더이상 없는 변수 myname
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print(myname)   # 더이상 없는 변수 myname
NameError: name 'myname' is not defined
>>> 
>>> # 여러 변수를 한줄에 선언하기 가능
#  기본적으로 파이썬 한 줄에 한 문장만 작성원칙..
#   ;  을 사용하면 여러문장을 한줄에 표현 가능.
>>> a = 10; b = 20; c = 30   # 가능
>>> # 그러나 파이썬 다운 표현은 아래와 같다.
>>> a, b, c = 10, 20, 30
>>> print(a, b, c)
10 20 30
>>> 
>>> # 변수의 값을 증가 시키기
>>> a
10
>>> a = a + 1    # a 의 값을 1 증가
>>> a
11
>>> a = a * 2    # a 의 값을 2 증가
>>> a
22
>>> # ↑ 정정 : a 값 2배 ^^
>>> # 복합 대입 연산자
#  a += 1  <--->   a = a + 1

>>> a += 1
>>> a
23
>>> a *= 3
>>> a
69
>>> a /= 3
>>> a
23.0
>>> # 명심 !  파이썬에서 / 연산의 결과는 무.조.건 실수 (float)
>>> 
>>> # 파이썬에서 변수값 바꾸기 (swap)
>>> #  우선 전통적인 방법은..
>>> a, b = 10, 200;
>>> a, b
(10, 200)
>>> temp = a
>>> a = b
>>> b = temp
>>> a, b      # 별도의 변수 temp 사용하여 a, b 값을 바꿈.
(200, 10)
>>> 
>>> # 그러나 파이썬에서는 변수값 바꿀때 아래와 같이 하면 된다.
>>> c, d = 'hello', '2019'
>>> c, d
('hello', '2019')
>>> c, d = d, c    # 변수값 바꾸기!
>>> c, d
('2019', 'hello')
>>> #-----------------------------------------------------------------
>>> # 형변환 함수들
>>> 
>>> "I'm " + 19 + "yrs old"    # 불가
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    "I'm " + 19 + "yrs old"    # 불가
TypeError: can only concatenate str (not "int") to str
>>> str(19)     #  int 19 를 str '19' 로 형변환
'19'
>>> age = 19
>>> age
19
>>> str(age)
'19'
>>> age      # 형변환 함수를 사용했다고 원래 변수가 바뀌는건 아니다.  단지 함수의 결과값이 형변환 된 결과 일 뿐이다.
19
>>> "I'm " + str(age) + " yrs old" # 가능!
"I'm 19 yrs old"
>>> 
>>> # str -> int, float
>>> n = "10"  # 문자열 "10"
>>> n + 20    # 불가
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    n + 20    # 불가
TypeError: can only concatenate str (not "int") to str
>>> int(n) + 20    # 가능!
30
>>> int('hello')   # 숫자타입으로 형변환 불가!
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    int('hello')   # 숫자타입으로 형변환 불가!
ValueError: invalid literal for int() with base 10: 'hello'
>>> n
'10'
>>> float(n)
10.0
>>> pi = 3.141592
>>> pi
3.141592
>>> int(pi)
3
>>> # ↑ 실수 타입을 정수타입으로 형변환 할때는 소숫점이하 절삭됨 (데이터 손실 발생주의!)
>>> #---------------------------------------------------------
>>> 
>>> # print()  함수
#  파이썬의 기본 출력 함수
#   print(출력내용, 출력내용, 출력내용...)
#   print() <--  출력후 줄바꿈 기본
>>> 
==================== RESTART: E:\Py1908\02_03_print함수.py ====================
10 20 30 40
aaa bbb 3.14
my wolrd your world
I'm 30 year's old
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2

1000
------------------------------
10hello3.14world
==================================================
2019-8-9 21:30:45
############################################################
10
20
30
Hello 파이썬
my name is john, I'm 10 yrs old
>>> #--------------------------------------------------
# 이스케이프 문자(escape character)
#  문자열(str) 안에서 특수한 문자 출력할때 사용
#  \  와 조합한 형태

#   \n : 줄바꿈 (new line)
#   \t  : 탭(tab)
#   \\  : 역슬래시
#   \'  : 홀따옴표
#   \"  : 쌍따옴표
>>> print("hello\nworld")
hello
world
>>> print("10\t20\t30")
10	20	30
>>> print("100\t200\t300")
100	200	300
>>> print("1000\t2000\t3000")
1000	2000	3000
>>> print("He says \"I\'m fine\"")    # "~" 안에서 " 출력 가능!
He says "I'm fine"
>>> #---------------------------------------
# 문자열 포맷팅 (formatting)

# 방법1 : % 연산자 사용
#   형식]  '서식포함문자열' % (데이터 들..)
>>> str1 = "Hello %s" % ("파이썬")
>>> str1
'Hello 파이썬'
>>> str2 = "my name is %s, I'm %d yrs old" % ('john', 10)
>>> str2
"my name is john, I'm 10 yrs old"
>>> 
