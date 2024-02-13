## 4. bisect: 이진 탐색 기능
# 정렬된 배열 에서 특정한 원소를 찾아야 할 때 효과적
# 주요 함수 bisect_left() , bisect_right() 시간복잡도는 O(logN)

# bisect_left(a, x) : 정렬 순서를 유지하며 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는다.
# bisect_right(a, x) : 정렬 순서를 유지하며 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를  찾는다.

from bisect import bisect_left, bisect_right

a = [1,2,4,4,8]
x = 4
print(bisect_left(a, x)) # 2
print(bisect_right(a, x)) # 4

# 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구하는데 활용
# bisect_right(a,y) - bisect_left(a,x) 는 그 범위의 원소 개수와 같다.
def count_by_range(list, left_value, right_value):
    leftIndex = bisect_left(list,left_value)
    rightIndex = bisect_right(list,right_value)
    result = rightIndex - leftIndex
    return result

result = count_by_range(a, 1, 8)
print(result) # 5

b = [1,2,3,3,3,3,3,4,4,8,9]
resultB = count_by_range(b, -1, 7)
print(resultB) # 9