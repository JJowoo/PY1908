# continue
#  순환문 안에서 continue 를 만나면
#  다시 순환문의 조건식으로 돌아 감
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0:
        continue
    print(a)

print("-" * 90)

dan = 8
i = 1
while i <= 9:
    print(dan, "x", i, "=", dan * i)
    if i == dan: break
    i = i + 1








