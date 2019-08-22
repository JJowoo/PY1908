# 파일 구분자 (separator)를
# Windows 환경에서도
# / 나 \ 가 둘다 작동하게 처리되긴 함.

#f = open("out/새파일2.txt", "w")
#f = open("out\\새파일3.txt", "w")

f = open("out/새파일4.txt", "w")
for i in range(1, 11):
    data = "%d번째 줄입니다\n" % i
    f.write(data)
f.close()

# TODO
# out/새파일4.txt 내용을 읽어서
# 화면에 출력 하기

with open("out/새파일4.txt", "r") as f:
    data = f.read()
    print(data)

print("*" * 40)

with open("out/파일utf-8.txt", "r", encoding="utf8") as f:
    data = f.read()
    print(data)

# 파일 저장시 encoding 과
# 파일 읽을때 encoding 이 일치해야 한다.

with open("out/한글파일1.txt", "w", encoding="utf8") as f:
    for i in range(1, 6):
        f.write("201" + str(i) + "년 입니다\n");

with open("out/한글파일1.txt", "r", encoding="utf8") as f:
    data = f.read()
    print(data)



