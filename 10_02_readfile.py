# 파일 읽기

# 한줄 읽기 readline()

f = open("새파일.txt", "r")
line = f.readline()   # 한줄 읽어오기
print(line, end="")
line = f.readline()
print(line, end="")
f.close()

print("*" * 40)

# 파일 전체 읽어오기
# 방법1 :readline() 사용
f = open("새파일.txt", 'r')
while True:
    line = f.readline() # 더이상 읽을것이 없으면 None 리턴
    if not line: break
    print(line, end="")
f.close()

print("*" * 30)

# 방법2 : readlines() 사용
# 각각의 line 들을 담은 list 를 리턴
f = open("새파일.txt", "r")
lines = f.readlines()
for line in lines:
    print(line, end="")
f.close()

print("-" * 20)

# 방법3: 파일 객체 사용
f = open("새파일.txt", "r")
for line in f:  # 파일객체에서 '한라인' 씩 for 문으로 읽을수 있다.
    print(line, end="")
f.close()

print("-" * 20)

# 방법4 : read() 사용, 전체 읽기
f = open("새파일.txt", "r")
data = f.read()  # 파일 전체 읽기
print(data)
f.close()




