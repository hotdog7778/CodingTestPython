### 함수

def add(a, b):
    return a + b
    # print(a+b)
print(add(3,7)) # 10
print(add(b = 6, a = 5)) # 11

# global 키워드로 변수를 지정하면 함수 바깥에 선언된 변수를 바로 참조하게 된다.
a = 0
def func():
    global a
    a += 1
    
for i in range(15):
    func()
    
print(a) # 15

# 람다 표현식
# 정렬 라이브러리를 사용할때, 정렬 기준을 설정할 때에도 자주 사용된다.
print((lambda a, b: a + b)(30,70)) # 100
