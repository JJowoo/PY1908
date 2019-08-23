# 클래스 정의
class Cookie:
    pass        # 아무것도 없는 클래스

# 사각형 에 대한 클래스 정의
# 사각형의 '속성' :  가로, 세로 -> 객체변수로 선언
# 사각형의 '동작' :  넓이 계산하기, 둘레 계산하기

class Rectangle:
    def __init__(self):
        print("Rectangle() 생성자 호출")
        self.width = 0    # 객체변수 선언및 초기화
        self.height = 0
    # 넓이를 구하는 메소드 (동작)
    def getArea(self):
        return self.width * self.height
    # 둘레를 구하는 메소드 (동작)
    def getPerimeter(self):
        return (self.width + self.height) * 2



        
