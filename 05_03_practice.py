# 1
# 홍길동씨의 주민등록번호는 881120-1068234이다.
# 홍길동씨의 주민등록번호를 연월일(YYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
jumin = '881120-1068234'
yymmdd = jumin[:6]
nums = jumin[7:]
print(yymmdd)
print(nums)


#2
# ['Life', 'is', 'too', 'short'] 라는 리스트를
# Life is too short라는 문자열로 만들어 출력해 보자.
s = ['Life', 'is', 'too', 'short']
print(" ".join(s))

#3
# (1,2,3)이라는 튜플에 4라는 값을 추가하여
# (1,2,3,4)처럼 만들어 출력해 보자.
a = (1, 2, 3)
# a.append(4)  ???????
a = a + (4, )
print(a)

#4
# [1, 3, 5, 4, 2]라는 리스트를 [5, 4, 3, 2, 1]로 만들어보자.
u = [1, 3, 5, 4, 2]
u.sort()
u.reverse()
print(u)





