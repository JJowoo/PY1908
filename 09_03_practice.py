filter_word = ['바보', '짱깨', '멍청이']

input_word = [
        "토끼는 바보다",
        "토끼는 빠르다",
        "이 토끼는 짱깨다",
        "저 토끼는 멍청이다",
        "산토끼 토끼야.."
]

def filter_str(s):
    for word in filter_word:
        if word in s:
            return "**금지어입니다**"

    return s

for s in input_word:
    print(filter_str(s))




