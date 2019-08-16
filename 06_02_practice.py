# 국어, 영어, 수학 점수를 입력받고
# 평균이 90 이상 -> A
#  80이상 -> B
#  70이상 -> C
#  60이상 -> D
#  60미만 -> F
# 출력은 '평균' 과 '등급' 출력
# 평균은 소숫점 1자리까지  출력

kor = int(input("국어점수입력:"))
eng = int(input("영어점수입력:"))
math = int(input("수학점수입력:"))

avg = (kor+ eng + math) / 3
grade = None
if avg > 90:
    grade = 'A'
elif avg >=80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'
else:
    grade = 'F'

print("평균 {:.1f}, 등급{}".format(avg, grade))





