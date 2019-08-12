Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> pi = 3.141592
>>> "원주율은 %f 입니다"
'원주율은 %f 입니다'
>>> "원주율은 %f 입니다" % (pi)
'원주율은 3.141592 입니다'
>>> "나이는 %d 살이고 이름은 %s  입니다"
'나이는 %d 살이고 이름은 %s  입니다'
>>> "나이는 %d 살이고 이름은 %s  입니다" % (34, '김덕수')
'나이는 34 살이고 이름은 김덕수  입니다'
>>> "원주율은 %.2f 입니다" % (pi)  # %.2f 소숫점 2자리까지 출력
'원주율은 3.14 입니다'
>>> a, b, c, d = 10, 100, 1000, 10000
>>> print("%d:%d:%d:%d" % (a, b, c, d))
10:100:1000:10000
>>> print("%5d:%5d:%5d:%5d" % (a, b, c, d))
   10:  100: 1000:10000
>>> # ↑ 기본적으로 우측 정렬
>>> print("%-5d:%-5d:%-5d:%-5d" % (a, b, c, d))  # 음수지정하면 좌측정렬
10   :100  :1000 :10000
>>> 
>>> # 방법2 : format() 함수 사용
>>> 
>>> 
===================== RESTART: D:/Py1908/03_01_format.py =====================
My name is {}, I'm {} years old
>>> 
===================== RESTART: D:/Py1908/03_01_format.py =====================
My name is {}, I'm {} years old
My name is 박수진, I'm 10 years old
>>> 
===================== RESTART: D:/Py1908/03_01_format.py =====================
My name is {}, I'm {} years old
My name is 박수진, I'm 10 years old
My name is 티라노, I'm 20 years old
>>> 
===================== RESTART: D:/Py1908/03_01_format.py =====================
My name is {}, I'm {} years old
My name is 박수진, I'm 10 years old
My name is 티라노, I'm 20 years old

ALeft                          
A                         Right
A            Center            
>>> # 파이썬의 기본 입력함수  input()

# input() 함수는 키보드로부터 입력 받아
# 문자열(str)로 리턴한다.
>>> 
>>> 
>>> a = input()
10
>>> a
'10'
>>> type(a)
<class 'str'>
>>> a + 8
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a + 8
TypeError: can only concatenate str (not "int") to str
>>> # 주의 : input() 으로 입력받은 결과는 str 이기 때문에 산술 연산 불가.!
>>> a = int(input())
345
>>> a
345
>>> type(a)
<class 'int'>
>>> a * 3
1035
>>> print("당신의 키를 입력하세요 : ", end=" ")
당신의 키를 입력하세요 :  
>>> 
===================== RESTART: D:/Py1908/03_02_Input.py =====================
당신의 키를 입력하세요 :  174.7
>>> height
174.7
>>> # prompt 를 사용한 input 입력
>>> 
>>> 
>>> 
>>> height = float(input("키를 입력하세요 cm :"))
키를 입력하세요 cm :155.9
>>> height
155.9
>>> print(10, 20, 30)
10 20 30
>>> a, b, c = input("3개이력 하세요")
3개이력 하세요10 20 30
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    a, b, c = input("3개이력 하세요")
ValueError: too many values to unpack (expected 3)
>>> 
>>> # 한줄 에 여러개 입력 받기
# 방법1:  input().split()
#        공백으로 구부하여 여러개 입력 가능.

>>> a, b, c = input("3개 입력:").split()
3개 입력:10 30         50
>>> a
'10'
>>> b
'30'
>>> c
'50'
>>> # 5:35:21  --> 시, 분, 초 구분
>>> hour, minute, second = input("시:분:초 입력").split(":")
시:분:초 입력5:35:21
>>> hour
'5'
>>> minute
'35'
>>> second
'21'
>>> # 위의 내용을 숫자로 변환하려면???
>>> hour = int(hour)
>>> minute = int(minute)
>>> second = int(second)
>>> hour
5
>>> minute
35
>>> second
21
>>> 
>>> 
>>> a, b, c = map(int, input('3개의 정수 입력:').split())
3개의 정수 입력:10 20 30
>>> a, b, c
(10, 20, 30)
>>> print("합계", a + b + c)
합계 60
>>> 
=================== RESTART: D:/Py1908/03_03_practice1.py ===================
yard 입력: 23.45465445
inch 입력: 41.2745346
23.45 yard 는 2144.69 cm
41.27 inch 는 104.84 cm
>>> 
=================== RESTART: D:/Py1908/03_04_practice2.py ===================
3개의 정수입력10 20 44
합=74
평균=24
>>> 
=================== RESTART: D:/Py1908/03_05_practice3.py ===================
키(cm)와몸무게(kg) 입력183 93
BMI 는 27.8 입니다
>>> 
