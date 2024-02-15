## 숫자 카드 게임
# 96page
# 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장 뽑기.
# 카드는 N X M 형태로 놓임. N은 행, M은 열 이다.

# N M
N, M = map(int, input().split())
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))

array = [row1, row2, row3]

for i in range(len(array)):
    minArray = [0] * len(array)
    
    for num in array[i]:
        if minArray[i] == 0: 
            minArray[i] = num
        elif minArray[i] < num:
            minArray[i] = num
    
    if (i == len(array)-1):
        minArray.sort(reverse=True)
        print(minArray[0])


### min(), max() 사용한 풀이
# N M
N, M = map(int, input().split())
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
row3 = list(map(int, input().split()))
        
cards = [
    list(map(int, input().split())) for _ in range(N)
]

# 각 행에서 가작 작은수
mins = [min(row) for row in cards]
# ex) [1, 1, 1]

# mins 리스트에서 가장 큰 수
print(max(mins))