# ,주어진 문자열을 알파벳별로 출현빈도 구하려면?
# 대소문자 구분없이 소문자로만
# 입력 : "Gorilla"
# ↓
# {
#     "g": 1,
#     "o": 1,
#     "i": 1,
#     "l": 2,
#     "a": 1,
#     "r": 1
# }

str_data = input("문자열을 입력해보세요:")
str_data = str_data.lower()  # 소문자 변환

#1
result = {}

for ch_code in range(ord('a'), ord('z') + 1):
    cnt = str_data.count(chr(ch_code))
    if cnt > 0:
        result[chr(ch_code)] = cnt

print(result)

#2
result2 = {
    chr(ch_code) : str_data.count(chr(ch_code))
    for ch_code in range(ord('a'), ord('z') + 1)
    if str_data.count(chr(ch_code)) > 0
    }

print(result2)

#3
result3 = {}
for ch in str_data:
    if ord('a') <= ord(ch) <= ord('z'):     # 'a' ~ 'z' 사이
        if result3.get(ch):
            result3[ch] += 1  # 기존값 +1
        else:
            result3[ch] = 1   # 첫등장

print(result3)







