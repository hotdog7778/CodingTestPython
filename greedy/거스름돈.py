# 당신은 음식점 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원 동전이 무한히 존재한다고 가정한다.
# 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야 할 동전의 최소 개수를 구하라.
# 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.
import time

N = int(input())

START_TIME = time.time()

##### 풀이
changes = N;
count = 0;
units = [500, 100, 50, 10]

for unit in units:
    if(changes == 0): 
        break    
    unitCount = changes // unit    
    if(unitCount == 0): 
        continue    
    count += unitCount
    changes %= unit 
    #print(unit,"원 짜리 동전", unitCount, "개")
#####


##### 해설 풀이
# n = N
# count = 0

# # 큰 단위의 화폐부터 차례 확인
# coin_types = [500,100,50,10]

# for coin in coin_types:
#     count += n // coin
#     n %= coin

# print(count)

END_TIME = time.time()

print("시간:", END_TIME-START_TIME ,"동전수:", count)


### 동전 큰단위가 작은단위의 배수 형태이기 때문에 가능
### 500,400,50,10 으로 생각해보기  -->  다이나믹 프로그래밍으로 해결 할 수 있다.