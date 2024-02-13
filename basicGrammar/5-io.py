### 입출력
# input() : 한 줄의 문자열을 입력 받로고 해준다.
# int() : 입력받은 데이터를 정수형 데이터로 처리하기 위해서 문자열 -> 정수로 바꾸는 int()
# 문자열을 띄어쓰기로 구분하는 경우가 많다. --> list(map(int, input().split()))

# 입력을 위한 전형적인 코드
n = int(input())
data = list(map(int, input().split()))
data.sort(reverse = True)
print(data)

# n, m, k를 공백으로 구분하여 입력
n, m, k = map(int, input().split())
print(n, m, k)

# 입력을 받는 시간도 줄여야 한다. 그래서 입력을 더빠르게 받는 방법을 알고 있어야 한다.
# 입력 개수가 많은 경우 -> sys 라이브러리의 sys.stdin.readline() 함수를 이용.
import sys
data = sys.stdin.readline().rstrip()
# readline() 으로 입력 받으면 엔터가 줄바꿈
# rstrip() 은 이 엔터 공백 문자를 제거한다.
print(data)

# 출력
print() # 각 변수를 , 로 구분하면 띄어쓰기로 구분되어 출력된다. 그리고 기본적으로 출력 이후에 줄 바꿈을 수행한다.
answer = 7
# print("정답은 " + answer + " 입니다.") << 에러 
print("정답은 " + str(answer) + " 입니다.")
print("정답은", answer, "입니다.")

# f-string (3.6 버전부터)
print(f"정답은 {answer} 입니다.")


