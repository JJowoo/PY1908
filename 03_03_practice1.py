# 1야드(yd)는 91.44cm이고 1인치(in)는 2.54cm이다.
# 처음에는 야드를 입력받고 두번째는 인치를 입력받아 
#각각 cm로 변환하여 다음 형식에 맞추어 소수 첫째자리까지 출력하시오.

yard = float(input("yard 입력: "))
inch = float(input("inch 입력: "))
print("%.2f yard 는 %.2f cm" % (yard, yard * 91.44))
print("%.2f inch 는 %.2f cm" % (inch, inch * 2.54))
