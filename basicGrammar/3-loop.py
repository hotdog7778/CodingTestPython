### 반복문 
# while , for
# 보통 for 문이 더 짧다.

# while문
# 조건문이 참일때 반복적으로 코드가 수행
i = 1
result = 0

while i <= 9:
    if i % 2 == 1:
        result += i
    
    i += 1
    
print(result)

# for문
# in : 첫 번째 인덱스 부터 차례로 방문. 리스트/튜플/문자열 등이 사용될 수 있음.
# range() : range(시작 값, 끝 값 +1)
# range() : 값을 하나만 넣으면 자동으로 시작값은 0 이다.
result = 0
for i in range(1, 10):
    result += i
print(result) # 1~9 합

scores = [90,85,77,65,97]
for i in range(5):
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.")
        
# continue : 반복문의 처음으로 돌아간다. 그리고 다음 반복을 수행한다.
black_list = {2,4}

for i in range(5):
    if i + 1 in black_list:
        continue
    if scores[i] >= 80:
        print(i + 1, "번 학생은 합격입니다.zz")


# 중첩 반복문
# &플로이드 워셜 알고리즘, 다이나믹 프로그래밍 등에서 자주 사용
for i in range(2,10):
    print(i,"단")
    
    for j in range(1,10):
        print(i,"*",j,"=",i*j)
    
    print()    
    