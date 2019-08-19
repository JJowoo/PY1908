# break, continue
# --> for 순환문에서도 사용 가능

for x in range(10):
    if x % 2 == 0: continue
    print(x)
print()
for x in range(10):
    print(x)
    if x == 5 : break

print("-" * 80)

# 중첩 순환문
#  nested loop
#  순환문 안의 순환문

num = 5

for y in range(num):
    for x in range(num):
        print("*", end="")
    print()


print()

for y in range(num):
    for x in range(y + 1):
        print("*", end="")
    print()

# TODO
# *****
# ****
# ***
# **
# *

print()

for y in range(num):
    for x in range(num - y):
        print("*", end="")
    print()

print("\n구구단 출력")

dan = 2

for dan in range(2, 10):    
    for i in range(1, 10):
        print(dan, "x", i, "=", dan * i)
    print()








