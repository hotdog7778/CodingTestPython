## 1이 될때 까지
# 99page

# N에서 1을 빼던가 K로 나눠서 값을 1로 만들어라
# N >= K
# n, k = map(int, input().split())

# count = 0

# while True:
#     if (n % k == 0):
#         n /= k
#         count +=1
#     else:
#         n -= 1
#         count += 1
    
#     if (n == 1): 
#         print(count)
#         break
    
n, k = map(int, input().split())
result = 0;

while True:
    print(f"반복문 시작 N:{n}, K:{k} 입니다.")
    target = (n // k) * k
    print(f"target:{target} 입니다.")
    result = result + (n - target) 
    print(f"result:{result} 입니다.")
    
    n = target 
    
    if n < k:
        print(f"반복문 종료 N:{n}, K:{k}, Result:{result} 입니다.")
        break
    
    n = n // k
    result = result + 1
    print(f"N:{n}, result:{result} 입니다.")
    
result = result - 1
print(f"결과 출력 N:{n}, K:{k} Result:{result} 입니다.")
    
    
    
    
    