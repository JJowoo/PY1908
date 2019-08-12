# 키(cm) 와 몸무게(kg) 를 입력받아 bmi 를 계산하여 출력
# bmi = 몸무게(kg) /  (키(m) x 키(m))
# bmi는 소숫점 한자리까지 출력

height, weight = map(float, input("키(cm)와몸무게(kg) 입력").split())
height /= 100;
bmi = weight / (height ** 2)
print("BMI 는 {:.1f} 입니다".format(bmi))
