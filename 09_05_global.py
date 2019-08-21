a = 1  # 함수 '밖'에서 선언된 변수
       #  전역 변수 (global variable)
def vartest():
    print(a)

# 매개변수, 혹은 함수 안에서 선언된 변수는
# 지역변수 (local variable) 이라 함
# 지역 변수는 해당 블럭이 끝나면 소멸됨.
def vartest2(a):
    a = a * 2
    print(a)

2    
    
