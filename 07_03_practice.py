# 예제 연습
# 학생들의 점수가 아래와 같이 주어졌다고 하자
# 총점과 평균을 출력해보세요
# 단! for 사용

total = 0
avg = 0.0
scores = [88, 34, 98, 74, 33, 88, 22, 100]

for s in scores:
    total += s   # total = total + s

print("학생수:", len(scores), "명")
print("총점:", total, "점")
print("평균:", total / len(scores), "점")

# [결과]
# 학생수: 5 명
# 총점: 327 점
# 평균: 65.4 점




