# List Comprehension (리스트 내포?)
# 리스트 안에 포함된 for 문

# [표현식 for 항목 in 반복가능객체 (if조건)]

# ex)
# 주어진 기존의 리스트 데이터들을
# x 3 하여 새로운 리스트 작성하기

a = [1, 2, 3, 4] # -> [3, 6, 9, 12]

result = []
for num in a:
    result.append(num * 3)
print(result)

print()
result = [num * 3 for num in a ]
print(result)

# 짝수에만 3을 곱하여 담고 싶다면??
result = [num * 3 for num in a if num % 2 == 0]
print(result)

#---- 0 으로 초기화된 리스트
result = [ 0 for n in range(26)]
print(result)

# for문 2개 이상 사용 가능...
# [표현식 for 항목1 in 반복객체1
#         for 항목2 in 반복객체2
#         for 항목3 in 반복객체3
#         ...
#  ]

result = [  str(n) + "-" + ch
            for n in range(1, 4)
            for ch in "ABC"  ]

print(result)

#------------------------------
dataset = [1, -2, 3, -4, 5]

print([ x ** 2 for x in dataset ])

result = [ y
    for y in [ x ** 2 for x in dataset ]
    if y > 10 ]

print(result)












