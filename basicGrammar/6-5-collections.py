## 5. collections: deque, Counter 등 자료구조를 포함
# 자료구조를 제공하는 표준 라이브러리

## deque
# 보통 deque를 사용해서 큐를 구현한다.

# 먼저, 리스트자료형의 append(),pop() 은 데이터 추가,삭제시 '가장 뒤 원소' 기준이다.
# 리스트로 앞쪽 원소부터 처리하고 싶을 때 시간복잡도는 O(N) 이다.
# 즉, 앞쪽 원소처리에 관련해서는 deque 사용을 고려할 필요 있음.

# 뒤쪽 원소 처리 : 
#  추가 : 
#  - 리스트 : O(1)
#  - deque : O(1)
#  삭제 : 
#  - 리스트 : O(1)
#  - deque : O(1)

# 앞쪽 원소 처리 : 
#  추가 : 
#  - 리스트 : O(N)
#  - deque : O(1)
#  삭제 : 
#  - 리스트 : O(N)
#  - deque : O(1)

# deque 는 인덱싱, 슬라이싱 기능 사용 X
# 스택이나 큐의 기능을 모두 포함한다. 스택 또는 큐 자료구조 대용으로 사용
# popleft() : 첫 원소 제거
# pop() : 마지막 원소 제거
# appendleft() : 첫 인덱스에 원소 추가
# append() : 마지막 인덱스에 원소 추가
from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))


## Counter 
# 등장 횟수를 세는 기능을 제공한다.
# ex) 리스트에서 내부의 원소가 몇번 등장 했는지
from collections import Counter

list = ['red','blue','red','red','green','green',]
counter = Counter(list)

print(counter['red']) # 3
print(counter['blue']) # 1 
print(counter['green']) # 2
print(counter['fake']) # 0