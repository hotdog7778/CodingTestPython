### 조건문
# if ~ elif ~ else 문
score = 90

if  score >= 90:
    print("A")
    print("우수한 성적입니다.")
elif score >= 80:
    print("B")
elif score >=70:
    print("C")
else:
    print("F")
    print("분발하세요")
    
# 들여쓰기는 스페이스바 4번

# 비교 연산자
X = "X"
Y = "Y"
X == Y # 서로 같을때 참이다.
X !=Y # 서로 다를때 참이다.

# 논리 연산자
X and Y
X or Y
not X # X가 false 일때 true 이다.

# 파이썬의 기타 연산자
# in 연산자
# not in 연산자
LIST = [1,2,3]
STRING = "string"
X in LIST # 리스트안에 X가 들어가 있을 때 참이다.
X not in STRING # 문자열 안에 X가 없을 때 참이다.

# 조건문 본문 pass
if score >= 80:
    pass
else:
    print("80점 미만")

# 한줄로 변경
if score >= 80: result = "Success"
else: result = "Fail"

# 조건부 표현식 ( if ~ else 문을 한줄에 작성)
score = 85
result = "Success" if score >= 80 else "Fail"
print(result)

# (리스트에 있는 원소의 값을 변경해서 다른 리스트를 만들려 할 때 사용하기 좋음)
a = [1,2,3,4,5,5,5]
remove_set = {3,5}

result = []
for i in a:
    if i not in remove_set:
        result.append(i)
print(result) # [1, 2, 4]
# result[i for i in a if i not in remove_set] 

