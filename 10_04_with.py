# with 구문
# 매번 close() 해주기 불편, 까먹기 쉽다.
# with 구문 사용하면 자동적으로 close해준다.
#  파이썬 2.5 부터 지원

with open("새파일.txt", "r") as f:
    data = f.read()
    print(data)
# 반드시 블럭 형태로 작성되어야 하며,
# 블럭이 끝나면 f 가 자동적으로 close() 된다.
