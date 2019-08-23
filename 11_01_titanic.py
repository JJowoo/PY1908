# 타이타닉 데이터 파일을 분석하여
# 객실 등급별 '탑승인원' 과
# '생존자'  그리고
# 객실등급별 생존률을 산출하세요
r = """
3등급] 총 491 명, 생존 119 명, 생존률 24.2%
1등급] 총 216 명, 생존 136 명, 생존률 63.0%
2등급] 총 184 명, 생존 87 명, 생존률 47.3%
"""
with open("data/titanic.csv", "r", encoding="utf8") as f:
    f.readline()  # 첫 줄 타이틀은 패스 ..
    line = f.readline()
    psgr = line.split(",")  # 승객
    survived = psgr[1]  #생존 여부
    pclass = psgr[2]  #객실등급
    print(survived, pclass)

print("*" * 30)

result = {}  
with open("data/titanic.csv", "r", encoding="utf8") as f:
    f.readline()  # 첫줄 건너뛰기
    for line in f:  # 승객 데이터 읽기
        psgr = line.split(",")  # 승객 한명의 데이터
        survived = psgr[1]  #생존여부
        pclass = psgr[2]  # 객실등급
        if result.get(pclass):
            result[pclass].append(survived)  # 기존에 해당 등급 객실 리스트 있었으면 추가
        else:
            result[pclass] = [survived]     # 기존에 해당등급 객실 리스트 없었으면 새로 생성 

# 결과 계산해서 출력하기
for key in result:
    total = len(result[key])  # result[key] 는 '리스트'
    survived = result[key].count("1")  # CSV 파일 읽어 들인건 일단 전부 str 로 읽어 들임
    print("%d등급] 총 %d명, 생존 %d 명, 생존률 %.1f%%" % (int(key), total, survived, (survived / total) * 100 ) )
    
2

         

    
    














