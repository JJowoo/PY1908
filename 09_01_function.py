# 함수의 호출순서, 리턴순서

def funcA():
    print("funcA() 호출")
    funcB()
    print("funcA() 리턴")

def funcB():
    print("funcB() 호출")
    funcC()
    print("funcB() 리턴")

def funcC():
    print("funcC() 호출")
    print("funcC() 리턴")

funcA()  # 함수 호출

print("-" * 30)

def aaa():
    print("aaa() 호출")
    return "aaa"

def bbb():
    print("bbb() 호출")
    return "bbb"

def ccc():
    print("ccc() 호출")
    return "ccc"

print(aaa(), bbb(), ccc())

print("-" * 30)

def ddd():
    print("ddd() 호출")
    return (aaa(), bbb(), ccc()) # tuple 리턴

print(ddd())


















