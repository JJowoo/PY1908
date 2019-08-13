# 여러개의 데이터를 담는 데이터 타입(들)

# 1. list  : 순서가 있다. 중복 허용, mutable
# 2. tuple : 순서가 있다. 중복 허용, immutable
# 3. set   : 순서 없다. 중복허용 안함
# 4. dict  :  key-value 쌍으로 저장

#------------------------------
# list
#     [     ]   으로 만든다.
#  데이터(원소)들은 콤마로 구분한다.
#  각 데이터 (원소)들은 어떠한 타입도 가능!

# 인덱싱(indexing)
#  list 의 데이터 원소는 0 부터 시작!

# 파이썬은 음수 인덱싱 가능!

# 리스트 원소의 개수는 len() 함수 사용

# 리스트에 원소 추가 : append() 함수 사용

# 리스트의 원소 삭제 : del() 함수 사용

b = [
	[100, 200, 300],
        [1.1, 2.2, 3.3],
        ['a', [777,888,['bbb','ddd','zzz']], 'c']
        
    ]

# list 의 +, *  연산
#  +  :   리스트 원소들을 연결한 리스트

# list 의 슬라이싱(slicing )

# list.index(값) : 값으로 인덱스 찾기

# 특정 원소가 list 에 있는지 여부 -> in 연산자 사용
#   bool 타입 결과 ( True / False)

# list 와 str
#   str.join() 함수 : list --> str 묶어줌.
#   str.split() 함수 : str --> list 로 쪼개줌.
#   list(str) 함수 : str -> list 형변환 함수









