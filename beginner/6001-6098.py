# print('print("Hello\\nWorld")')

## split-sep 사용
# a, b = input().split(':')
# print(a,b, sep=':')

## 16진수, 8진수 출력
# a = input()
# n = int(a)            #입력된 a를 10진수 값으로 변환해 변수 n에 저장
# print('%x'% n)  #n에 저장되어있는 값을 16진수(hexadecimal) 소문자 형태 문자열로 출력
# print('%X' % n)  #n에 저장되어있는 값을 16진수 대문자 형태 문자열로 출력

# 참고
# 10진수 형태로 입력받고
# %x로 출력하면 16진수(hexadecimal) 소문자로 출력된다.
# (%o로 출력하면 8진수(octal) 문자열로 출력된다.)

## 영문자 1개를 입력받아 10진수 유니코드(Unicode) 값으로 출력해보자.
# n = ord(input()) #입력받은 문자를 10진수 유니코드 값으로 변환한 후, n에 저장한다.
# print(n)

## 10진 정수 1개를 입력받아 유니코드 문자로 출력
# c = int(input()) # 10진 정수 1개(32 ~ 126 범위)가 입력된다.
# print(chr(c))  #c에 저장되어 있는 정수 값을 유니코드 문자(chracter)로 바꿔 출력한다. 


## 문자 1개를 입력받아 그 다음 문자를 출력
# n = ord(input()) 
# print(chr(n+1))

## 단어와 반복 횟수를 입력받아 여러 번 출력해보자.
# 문자열 * 정수 또는 정수 * 문자열은 그 문자열을 여러 번 반복한 문자열을 만들어 준다.
# s, n = input().split()
# print(int(n) * s)

## 반올림
# a = input()
# a = float(a)
# print(format(a, ".2f"))

## 입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력
# ~(bitwise not), 
# &(bitwise and), 
# |(bitwise or), 
# ^(bitwise xor),
# <<(bitwise left shift), 
# >>(bitwise right shift)

# a = 1
# print(~a) # -2


## 3항 연산
# 3개의 요소로 이루어지는 3항 연산은
# "x if C else y" 의 형태로 작성이 된다.
# - C : True 또는 False 를 평가할 조건식(conditional expression) 또는 값
# - x : C의 평가 결과가 True 일 때 사용할 값
# - y : C의 평가 결과가 True 가 아닐 때 사용할 값
# a,b=input().split()
# a=int(a)
# b=int(b)
# print(a if (a >= b) else b)

# 입력된 세 정수 a, b, c 중 가장 작은 값을 출력
# a,b,c=input().split()
# a=int(a)
# b=int(b)
# c=int(c)

# 더 작은 값
# a if (a <= b) else b
# print((a if (a <= b) else b) if ((a if (a <= b) else b) <= c) else c)