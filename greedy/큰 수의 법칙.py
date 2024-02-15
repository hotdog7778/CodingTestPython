# 큰 수의 법칙
# 92page

# 문제
# 다양한 수로 이루어진 배열이 있다.
# 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 단, 특정 인덱스에 해당하는 수가 연속해서 K번 초과하여 더해질 수 없다.

# N : 배열의 크기
# M : 숫자가 더해지는 횟수
# K : 같은 인덱스 사용 제한 수
import time
# 입력 받기
n, m ,k = map(int, input().split())
numbers = list(map(int, input().split()))

# START_TIME = time.time()

### 생각 및 풀어보기
# 일단, 가장 큰거를 K번 더한다. 인덱스가 다른 원소중 가장 큰거를 K번 더해
# 단, M번만 더해
# 1번쨰로 큰수, 2번째로 큰 수만 알면됨
# numbers.sort(reverse=True) # 큰수 알기위해 sort씀
# first = numbers[0]
# second = numbers[1]

# maxNum = 0;
# count = k;

# for _ in range(m):
#     count -= 1
    
#     if(count < 0):
#         maxNum += second
#         count = k
#     elif(count >= 0):
#         maxNum += first

# END_TIME = time.time()

# print(maxNum, "시간 : ", END_TIME-START_TIME)

####

### 위 풀이는
# M:숫자가 더해지는 횟수. 가 100억 이상 커진다면 시간초과 판정을 받을 것이다.
START_TIME = time.time()

numbers.sort(reverse=True) # 큰수 알기위해 sort씀
first = numbers[0]
second = numbers[1]

# 큰수가 반복되는 횟수
count = (m // (k + 1)) * k
count = count + (m % (k + 1))

firstSum = count * first
secondSum = (m - count) * second
result = firstSum + secondSum

END_TIME = time.time()
print(result, "시간 : ", END_TIME-START_TIME)

