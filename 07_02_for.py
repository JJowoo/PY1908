# for ~ in 순환문

# list 사용
test_list = ["aaa", "bbb", "ccc"]
for item in test_list:
    print(item)

print()  # tuple 사용
for item in (111, 2000, 3.14):
    print(item)

print()  # str 사용
for ch in "Python":
    print(ch)

# dict 사용
test_dict = {
        "name" : "hong",
        "age" : 13,
        "grade" : 5
    }

for k in test_dict:
    print(k, test_dict[k])

print()
# range() 사용
# 숫자로 순환 하는 경우
for i in range(3):  # range(3) => 0, 1, 2
    print(i)

print()
for i in range(5, 8):  # 5, 6, 7
    print(i)

print()
for i in range(4, 15, 3):  # 4, 7, 10, 13
    print(i)

print()
for i in range(10, 0, -2):# 10, 8, 6, 4, 2
    print(i)

print()
# list + for 다른 예
animals = ["dog", "cat", "bird", "fish"]
print(len(animals))

for n in animals:
    print(n)

print()
for i in range(len(animals)):
    print(animals[i])

# 리스트의 데이터가 tuple 인 경우?
print("*" * 60)

a = [(1, 2), (3, 4), (5, 6)]
# len(a) <-- ???

for x in a:
    print(x[0], x[1])

print()

for (x, y) in a:
    print(x, y)




    

 



