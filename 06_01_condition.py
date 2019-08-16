# and , or, not 연산자

# 아무것도 안하는 블럭을 만들때
#  pass  명시!!
pocket = ['paper', 'money', 'phone']

if 'money' in pocket:
    pass   # 아무것도 안하는 블럭
else:
    print("카드를 꺼내세요")

# 숫자 하나를 입력 받아서,
# 3의 배수인지 아닌지 출력하고
# 3의 배수이면 짝수 인지 아닌지 여부도 출력

#num = int(input('숫자 하나 입력'))
num = 27
if num % 3 == 0:
    print("3의 배수입니다")
    if num % 2 == 0:
        print("2의 배수이기도합니다")
    else:
        print("3의 배수이지만 2의 배수는 아닙니다")
else:
    print("3의 배수가 아닙니다")

# if ~ elif

a = -10
if a > 0:
    print("양수입니다")
elif a == 0:
    print("0 입니다")
else:
    print("음수입니다")
    
#--------------------------
    
# 점수가 100점 이면 "BEST"
# 70점 이상이면 "GOOD"
# 60점 이상이면 "Danger"
# 그 이하면 "Fail"

point = 55

if point == 100:
    print("BEST")
elif point >= 70:
    print("GOOD")
elif point >= 60:
    print("Danger")
else:
    print("Fail")









