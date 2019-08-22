# append 모드

f = open("새파일.txt", "a") # append 모드
for i in range(3):
    data = "%d Line appended\n" % (i + 1)
    f.write(data)
f.close()
