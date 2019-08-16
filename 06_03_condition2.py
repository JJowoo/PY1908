# 조건부 표현식

# 절대값
n = 70
print(n if n >= 0 else -n)

# 차이값
# 10, 40 의 차이는 30?
# 40, 10 의 차이는 30?
a = -100
b = -1000
diff = a - b if a > b else b - a
print("diff", diff)
