# 프로그램의 제어문 (control)
# 조건에 따라 순차적으로 진행하는
# 프로그램 실행순서를 변경하여 진행

# 제어문의 종류
#   1 조건문 : if
#   2 순환문  : for, while

# if 조건문
#
#  if 조건식:
#     수행할 문장1
#     수행할 문장2
#      ...

print('시작합니다')
num = 30
if num > 20:
    num += 20
    print(num)

print('종료합니다')

print("*" * 60)

num2 = 40
if num2 % 2 == 0:
    print("짝수")
    print("입니다")
    print("곧집에 갑니")
else:         # 위 if 조건식이 False 일때 수행
    print("홀수")

# 주어진 숫자가 3의 배수이면?
if num2 % 3 == 0:
    print("3의 배수입니다")
else:
    print('3의 배수 아닙니다')
    
        









