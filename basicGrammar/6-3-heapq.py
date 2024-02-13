## 3. heapq: Heap 기능을 제공. 우선순위 큐 기능 구현에 사용
# 보통 PriorityQueue 보다 빠르게 동작
# 단순히 원소를 힙에 넣었다 빼는것 만으로 오름차순 정렬됨 O(NlogN)
# 파이썬의 힙은 최소 힙으로 구성되어 있음. 최대 힙을 제공하지 않는다.
# 자료구조 최상단 원소는 '가장 작은' 원소
# heapq.heappush() : 원소 삽입
# heapq.heappop() : 원소 꺼내기

# 힙 정렬 구현
import heapq
def heapsort(iterable):
    h = []
    result = []
    # 차례로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 원소를 차례대로 꺼내 담기
    
    print("확인", h) # 확인 [0, 1, 2, 6, 3, 5, 4, 7, 8, 9]
    
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result
result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
# 최대 힙 대신 사용하는 방법
# 원소의 부호를 임시로 변경하는 방식
# 1. 삽입 전 부호 반대로 변경
# 2. 원소 꺼내어 다시 원소의 부호 바꿈
def heapsortDESC(iterable):
    h = []
    result = []
    # 힙에 원소 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    print(h) # [-9, -8, -4, -7, -5, -2, -3, -1, -6, 0]
    
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))    
    
    return result

result = heapsortDESC([1,3,5,7,9,2,4,6,8,0])
print(result) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

