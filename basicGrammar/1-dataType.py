### 자료형

## Number
# 정수와 실수 많이 사용. 정수를 기본으로 사용

## Integer
# 정수형

a = 1000
print(a)
a = -7
print(a)
a = 0
print(a)

## Real Number
# 실수형
a = 157.93
print(a)
a = -1837.2
print(a)
a = 5. # 5.0 .. 0 생략 
print(a)
a = -.7 # -0.7 .. 0 생략
print(a)

# 지수 표현방식
# &최단경로 문제에서 자주 사용
a = 1e9 # 9는 10의 9제곱을 의미
print(a) # 1000000000.0 .. 10억임
a = 5e9 # 9는 10의 9제곱을 의미
print(a) # 5000000000.0

# 실수처리 - 부동소수점
# &코딩테스트에서 흔히 소수 5번째 자리에서 반올림한 결과가 같으면 정답으로 인정
a = 0.3 + 0.6
print(a) # 0.8999999999999999

a = round(a, 1) # 소수 1 번째 자리에서 반올림
print(a) # 0.9


# 수 연산
# / 연산은 나눠진 결과를 기본적으로 실수형으로 처리한다.
# '//' 는 나눈 값에서 몫만 얻는 몫연산자
# '**' 는 거듭제곱 연산자
a = 5
b = 3
print(a ** b) # 5의 3거듭 제곱


## 리스트 자료형
# 내부적으로 배열
# 연결리스트는 append(), remove() 등 메서드 지원
# 리스트 대신 배열 혹은 테이블이라고 부르기도 한다.
a = [1,2,3,4,5,6,7,8,9]
print(a)
print(a[0])
newList1 = list()
newList2 = []
print(newList1, newList1)

# 크기가 N인 1차원 리스트 초기화. 모든 값은 0이다.
n = 10
a = [0] * n # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(a)

# Indexing
# 인덱스를 사용해서 특정 원소에 접근하는것
# -1 로 인덱싱하면 마지막 원소 출력

# Slicing
# 연속적인 위치의 원소들을 가져올때 사용
# 시작위치 : 끝위치
print(a[1:4]) # 1 ~ 3 을 자른다.

# 리스트 컴프리헨션
# 리스트 초기화 방법 중 하나.
# [] 안에 조건문과 반복문을 넣음.
array = [i for i in range(20) if i % 2 == 1]
print(array)
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)
print(array)

array = [ i * i for i in range(1,10)] # 1부터 9까지
print(array)

# 2차원 리스트 초기화에 사용하면 효과적이다. (반드시)
# N x M 크기의 2차원 리스트를 초기화 할때
n = 3
m = 4
array = [[0] * m for _ in range(n)] # 단순히 n번 수행하는게 중요할때 _ 사용
print(array) # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# 리스트 메서드
# append()에 비해 insert()는 동작이 느리다.
# insert() 함수를 남발하지 마라. remove() 도 마찬가지다.
a = [1,4,3]
# append() | 변수명.append() | 리스트에 원소 하나 삽입 | O(1)
a.append(2)
print(a) # [1, 4, 3, 2]

# sort() | 변수명.sort() | 기본 정렬기능. 오름차순 | O(NlogN)
a.sort()
print(a) # [1, 2, 3, 4]

# sort() | 변수명.sort(reverse = True) | 내림차순 정렬 | O(NlogN)
a.sort(reverse = True)
print(a) # [4, 3, 2, 1]

# reverse() | 변수명.reverse() | 원소 순서를 모두 뒤집기 | O(N)
a.reverse()
print(a) # [1, 2, 3, 4]

# insert() | 변수명.insert(삽입 위치 인덱스, 삽입 값) | 특정 인덱스 위치에 원소 삽입 | O(N)
a.insert(4, 104) # [1, 2, 3, 4, 104]
a.insert(7, 107) # [1, 2, 3, 4, 104, 107]
print(a)

# count() | 변수명.count(특정 값) | 리스트에서 특정 값을 가지는 데이터의 개수 | O(N)
a.insert(1, 1)
print(a.count(1)) # 2
print(a.count(2)) # 1

# remove() | 변수명.remove(특정 값) | 특정 값을 갖는 원소를 제거, 원소가 여러개면 하나만 제거 | O(N)
print(a) # [1, 1, 2, 3, 4, 104, 107]
a.remove(104)
print(a) # [1, 1, 2, 3, 4, 107]
a.insert(1,3)
print(a) # [1, 3, 1, 2, 3, 4, 107]
a.remove(3)
print(a) # [1, 1, 2, 3, 4, 107]

# 모두 remove 하기 (메서드로는 없음)
a = [1,2,3,4,5,5,5]
remove_set = {3, 5}
result = [ 
    i for i in a
        if i not in remove_set
    ]
print(result) # [1, 2, 4]


## 문자열 자료형
data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

# 문자열 연산
a = "Hello"
b = "World"
print(a + " " + b)

a = "String"
print(a*3) # StringStringString

# 문자열은 내부적으로 리스트처럼 처리된다. 여러 개의 문자가 합쳐진 리스트 라고 볼 수 있다.
# 따라서, 인덱싱과 슬라이싱을 이용할 수 있다.
a = "ABCDEF"
print(a[2:4]) # CD
a = "ABCDEF"
print(a[2]) # C

## 튜플 자료형 : 각원소의 성질이 서로 다를때 주로 사용
# &그래프 알고리즘 구현에 자주 사용
# 리스트와 거의 비슷한데 다음과 같은 차이가 있다.
# 튜플은 선언된 값을 변경할 수 없음.
# 리스트는 [] , 튜플은 ()
a = (1,2,3,4)
print(a) # (1, 2, 3, 4)
# a[2] = 7 # 오류 발생

## 사전 자료형
# 키와 밸류 쌍을 데이터로 가지는 자료형 이다.
# 내부적으로 해시 테이블을 이용한다.
# O(1) 의 시간 복잡도를 가진다.
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

# 관련 함수
# keys() : 키만 담은 리스트 반환
key_list = data.keys()
# values() : value만 담은 리스트 반환
value_list = data.values()
print(key_list)
print(value_list)
# 키에따른 값 출력
for key in key_list:
    print(data[key])

## 집합(Set) 자료형
# 리스트 혹은 문자열을 이용해서 만들 수 있다.
# 중복을 허용하지 않는다.
# 순서가 없다. >> 인덱싱 의미없음
# 특정원소 존재 여부 검사는 O(1)
# &특정한 데이터가 이미 등장한 적 있는지 여부를 체크할때 효과적

# 초기화 방법 : set(), { , , }
data = set([1,1,2,3,4,4,5])
print(data) # {1, 2, 3, 4, 5}
data = {3,3,4,4,5,5,6,6}
print(data) # {3, 4, 5, 6}

# 집합 자료형 연산
# 합집합 '|' / 교집합 '&' / 차집합 연산 '-' 
a = set([1,2,3,4,5])
b = set([3,4,5,6,7])
print(a | b)
print(a & b)
print(a - b)

# 집합자료형 관련 함수
data = set([1,2,3])
# add() : 집합 데이터에 값을 추가. O(1)
data.add(4)
print(data)
# update() : 여러 개의 값을 한꺼번에 추가
data.update([5,6])
print(data)
# remove() : 특정한 값을 제거. O(1)
data.remove(3)
print(data)





