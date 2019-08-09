# print()  함수
#  파이썬의 기본 출력 함수
#   print(출력내용, 출력내용, 출력내용...)
#   print() <--  출력후 줄바꿈 기본
print(10, 20, 30, 40)
print('aaa', 'bbb', 3.14)
print("my wolrd " + "your world")
print("I'm", 30, "year's old")

a = 10
b = 5

# 10 + 5 = 15
# 10 - 5 = 5
# 10 * 5 = 50
# 10 / 5 = 2

print(a, "+", b, "=", a + b)
print(a, "-", b, "=", a - b)
print(a, "*", b, "=", a * b)
print(a, "/", b, "=", int(a / b))
print()   # 한줄 줄바꿈만 함.
print(a ** 3)
print('-' * 30)
# end 인자, print 출력후 마무리 문자
print(10, end="")
print('hello', end="")
print(3.14, end="")
print('world')
print('=' * 50)

year = 2019
month = 8
day = 9
print(year, end="-")
print(month, end="-")
print(day, end=" ")
hour, minute, second = 21, 30, 45
print(hour, end=':')
print(minute, end=':')
print(second)

#--------------------------------------------------
# 이스케이프 문자(escape character)
#  문자열(str) 안에서 특수한 문자 출력할때 사용
#  \  와 조합한 형태

#   \n : 줄바꿈 (new line)
#   \t  : 탭(tab)
#   \\  : 역슬래시
#   \'  : 홀따옴표
#   \"  : 쌍따옴표

#---------------------------------------
# 파이썬은 프로그램 작성시
# 들여쓰기 (indent) 에 매우 민.감.
print('#' * 60)
print(10)
print(20)
print(30)

#---------------------------------------
# 문자열 포맷팅 (formatting)

# 방법1 : % 연산자 사용
#   형식]  '서식포함문자열' % (데이터 들..)
str1 = "Hello %s" % ("파이썬")
print(str1)

str2 = "my name is %s, I'm %d yrs old" % ('john', 10)
print(str2)


# 방법2 : format() 함수 사용












