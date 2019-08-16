# 무한루프 연습
# 사용자로부터 계속 정수를 입력
# 받다가 0이 입력되면...
# 그때까지 입력 받았던 숫자들을
# 모~ 두 출력하고
# 합한 결과도 출력.

num_list = []
print("정수들을 입력하세요")
print("0을 입력 하면 종료합니다")
while True:
    num = int(input())
    if num == 0:
        break    # 순환문 종료
    num_list.append(num)

print(num_list)
print("합:", sum(num_list))




    
