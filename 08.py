Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 문자열 함수 몇가지...
>>> "hello".count("l")  # 문자열안에 등장하는 sub문자열 개수
2
>>> "ababababbaaaabababaaaaabbabababa".coun("ab")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    "ababababbaaaabababaaaaabbabababa".coun("ab")
AttributeError: 'str' object has no attribute 'coun'
>>> "ababababbaaaabababaaaaabbabababa".count("ab")
11
>>> "Gorilla".lower()   #소문자 변환
'gorilla'
>>> "Gorilla".upper()   #대문자 변환
'GORILLA'
>>> ord("a")   # 문자 코드값
97
>>> ord("b")
98
>>> ord("A")
65
>>> #  able < bible
>>> # AaAa < aaAA
>>> chr(97)   # 코드값 --> 문자
'a'
>>> chr(103)
'g'
>>> # 리스트 만들기..
>>> # [ 'a', 'b', 'c', ... 'z']
>>> 
