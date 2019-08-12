# 파이썬의 기본 입력함수  input()

# input() 함수는 키보드로부터 입력 받아
# 문자열(str)로 리턴한다.

print("당신의 키를 입력하세요 : ", end=" ")
height = float(input())

# prompt 를 사용한 input 입력

# input 으로 여러개 입력?  --> 불가

# 한줄 에 여러개 입력 받기
# 방법1:  input().split()
#        '공백'으로 구분하여 여러개 입력 가능.

#   input().split(구분할문자)

# 한줄 입력후 일괄로 한번에 변환하기
#  map() 함수 ..
#  변수1, 변수2.. = map(int, input().split())



















