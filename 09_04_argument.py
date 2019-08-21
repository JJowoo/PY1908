# 매개변수 (parameter), 인자(argument)
def func(a, b):
    return a - b

print(func(100, 50))

# 함수 호출시 매개변수 지정 가능!
print(func(b = 100, a = 50))

# 정의한 매개변수의 개수와 호출한 개수는
# (기본적으로) 일치해야 한다

# print(func(10)) #?  에러!
# print(func(10, 20, 30))  #? 에러!

# 함수 정의시 매개변수의 초깃값을 설정 가능
# default argument
def reg_student(name, age, grade = 1):
    print("학생등록:", name, age, grade)

reg_student('hong', 34, 3)
reg_student('kim', 19)


# 바람직 : 초깃값 이 있는 매개변수들은
# 함수 정의시 우측으로 몰아서 정의
# (a, b, c, d = xxx, e = xxx, f = xxx ..)

# ↓ 에러
# (a, b = xxx, c, d, e = xxx, f ..)

def myFunc1(a, b, c, d = 0, e = 0, f = 0):
    return a + b + c + d + e + f

# 에러
# def myFunc2(a, b = 0, c, d = 0, e, f = 0):
#     return a + b + c + d + e + f

# 매개변수가 임의 의 개수인 함수 정의
# 호출할때 여러개의 매개변수가 아래args
# 에 tuple 로 건네진다.
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

# 키워드 매개변수 kwargs
# 함수 호출시 name=value 쌍으로 매개변수
# 넘겨주면 dict 형태로 받는다.
def print_kwargs(**kwargs):
    print(kwargs)

# *   args, kwargs 대신 다른 이름 사용해도 OK
#  그러나, 관례적으로 위 이름 사용. 



