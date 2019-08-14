# dict 딕셔너리
# dict 타입은 key-value 쌍으로
# 저장되는 데이터 타입
# { key1:value1, key2:value2, .. }
# 이름:홍길동, 나이:34...
# 순서 저장 안됨.

# len(dict) --> dict 의 key:value 쌍의 개수

# 특정 key 의 value 꺼내기
#   1. dict변수[ key ]
#   2. dict변수.get(key) 사용
#       --> key 가 없는 경우 None 리턴

# None <-- 데이터 타입
#     아무 타입도 정해지지 않은 타입

# get() 을 사용하면 예외적인 상황에서
# 동작 가능하게 커리 가능

# dict 데이터 추가
# dict 데이터 삭제
# dict 데이터 수정

# dict 은 언제 유용?
#  폼 형태의 테이블 데이터들
#  엑셀, database 등의 데이타들 다룰때.


# dict 의 value 는 어떠한 타입도 가능!
# dict 의 key는 .. hash 가능한 타입만 가능.

dict1 = {
    1 :  "haha",
    2 : "gaga",
    3 : "nana"
    }

dict2 = {
    "one" : (1, 2, 30),
    "two" : [10, 20, 3.14],
    "three" : {
            0 : 'abc',
            1 : 'def',
            3 : 'ghi',
            False : ["a", "b", "c"]
        }
    
    }

# key 에 불가한 타입
# dict3 = {
#    [10, 20, 30] : "gkgk"
#    }


# dict.keys(), dict.value() 함수

# in  연산자 와 dict
#   dict 의 key 존재 여부 확인










