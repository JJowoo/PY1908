# 리스트 만들기..
# ['a', 'b', 'c', ... 'z']

result = []
for ch_code in range(ord('a'), ord('z') + 1):
    result.append(chr(ch_code))

print(result)

result2 = [
        chr(ch_code)
        for ch_code
        in range(ord('a'), ord('z') + 1)
    ]

print(result2)










