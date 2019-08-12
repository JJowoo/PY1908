# format specifier (서식 지정자)
#    %d  :   십진수 정수
#    %f   :   실수
#    %s   :   문자열 
#    %%  :   % 문자 자체


# 방법2 : format() 함수 사용
str = "My name is {}, I'm {} years old"
print(str)

print(str.format("박수진", 10))

str = "My name is {name}, I'm {age} years old"
print(str.format(age = 20, name = '티라노'))


print()
print("A{:<30}".format("Left"))
print("A{:>30}".format("Right"))
print("A{:^30}".format("Center"))

















