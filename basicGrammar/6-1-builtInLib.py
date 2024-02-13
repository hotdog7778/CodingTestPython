### 주요 라이브러리 문법 및 유의점
# 코딩테스트는 대부분 표준 라이브러리를 사용 하도록 허용한다.
# https://docs.python.org/ko/3/library/

## 반드시 알아야할 6가지 표준 라이브러리
# 1. 내장 함수
# 2. itertools : 반복 형태의 데이터 처리 기능 제공. 순열과 조합 라이브러리 제공
# 3. heapq: Heap 기능을 제공. 우선순위 큐 기능 구현에 사용
# 4. bisect: 이진 탐색 기능
# 5. collections: deque, Counter 등 자료구조를 포함
# 6. math: 수학적 기능 제공

## 1. 내장 함수
# import 명령 없이 사용

# input() , print()

# sum() : iterable 객체를 매개변수로 받았을떄, 모든 원소의 합을 반환한다.
sum([1,2,3,4,5]) # 15

# min() : 2개 이상 파라미터가 들어왔을 때 , 최소값 반환
min(7,3,5,2) # 2

# max() : 2개 이상 파라미터가 들어왔을 때 , 최대값 반환
max(7,3,5,2) # 7

# eval() : 문자열 형식의 수학 수식을 받아 계산한 결과를 반환한다.
result = eval("(3+5)*7")
print(result)

# sorted() : iterable 객체를 받아 정렬된 결과 반환.
sorted([9,1,8,5,4]) # 오름 차순
sorted([9,1,8,5,4], reverse = True) # 내림 차순

# 정렬 기준 명시 방법
result = sorted(
    [
        ('홍길동', 35),
        ('장만복', 37),
        ('고길동', 22),
        ('은가누', 15),
    ],
    key = lambda x: x[1],
    reverse = True
)
print(result)

# sort()
data = [9,1,4,5,6]
data.sort()
print(data)