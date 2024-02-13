## 2. itertools : 반복 형태의 데이터 처리 기능 제공. 순열과 조합 라이브러리 제공
# permutations : 
#  - iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산
#  - 객체 초기화 이후 리스트 자료형으로 변환하여 사용
from itertools import permutations
data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result) # [('A', 'B', 'C'), ('A', 'C', 'B'), ('B', 'A', 'C'), ('B', 'C', 'A'), ('C', 'A', 'B'), ('C', 'B', 'A')]

# combinations : 
#  - iterable 객체에서 r개의 데이터를 뽑아 나열 (순서 고려하지 않음)
#  - 리스트 자료형으로 변환하여 사용
from itertools import combinations
data = ['A', 'B', 'C']
result = list(combinations(data, 2)) 
print(result) # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# product : 
#  - iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산 (중복 허용)
from itertools import product
data = ['A','B','C']
result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열(중복 허용)
print(result) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

# combinations_with_replacement
#  - r 개의 데이터를 뽑아 순서 고려 X 하고 모든 경우. 원소 중복 허용
#  - list로 변환하여 사용
from itertools import combinations_with_replacement
data = ['A','B','C']
result = list(combinations_with_replacement(data, 2))
print(result) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]


