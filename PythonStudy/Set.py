"""집합의 기초 실습하기"""

"""1. 집합의 생성, 추가, 삭제"""
# 집합의 생성
s= set()
s= {1,2,5}
print(s)
# 집합에 원소를 추가하려면 add()를 사용
s.add(10)
s.add(3)
print(s)
# 집합의 항목을 삭제하려면 discard(), remove(), clear() 함수를 사용
s.discard(5)
print(s)
s.remove(2)
print(s)
#s.remove(7)
#print(s)

"""2. 집합과 리스트"""
lst = [1, 7, 7, 3, 5, 8, 2, 7, 1]
set(lst) # 리스트 lst를 집합으로 변환
print(lst)
lst = list(set(lst)) # 집합을 리스트로 변환
print(lst)

"""3. 집합에 적용되는 메소드"""
shape = {'삼각형', '사각형', '사다리꼴'}
shape.add('타원') # 집합 shape에 원소 한 개를 추가
print(shape)
shape.remove('사각형') # 집합 shape에 포함된 원소 한 개를 삭제
print(shape)
shape.discard('오각형') # 집합 shape에 없는 원소 한 개를 삭제하려는 discard. 에러 메시지가 안 나타남
print(shape)
#shape.remove('오각형') # 집합 shape에 없는 원소 한 개를 삭제하려는 remove. 에러 메시지가 나타남
#print(shape)

"""리스트 연산과 집합 연산 비교 실습하기"""

# 교집합에 해당하는 연산
list1 = [2,3,5]
list2 = [1,3,6]
result1 = []
for i in list2:
    if i in list1:
        result1.append(i)
print(result1)

# 합집합에 해당하는 연산
list1 = [2,3,5]
list2 = [1,3,6]
result1 = []
for i in list2:
    if i in list1:
        result1.append(i)
result2 = list1 + list2
for i in result1:
    result2.remove(i)
print(result2)

# 차집합에 해당하는 연산
list1 = [2,3,5]
list2 = [1,3,6]
result1 = []
for i in list2:
    if i in list1:
        list1.remove(i)
print(list1)