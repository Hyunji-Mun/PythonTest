"""리스트의 활용 실습하기"""

"1. 리스트의 값을 변경"
# 두 번째 위치한 한 개의 값을 변경하는 방법
aa = [10, 20, 30]
aa[1] = 200
print(aa)

# 두 번째 값인 20을 200과 201 두 개의 값으로 변경
aa = [10, 20, 30]
aa[1:2] = [200, 21]
print(aa)

# aa[1:2] 대신 aa[1]을 사용하는 경우 -> 리스트 안에 또 다른 리스트로 추가됨
# 결과가 틀리지는 않지만 이렇게는 많이 사용하지 않음
aa = [10, 20, 30]
aa[1] = [200, 201]
print(aa)

# del()함수를 사용하여 aa[1] 항목을 삭제하는 방법
aa = [10, 20, 30]
del(aa[1])
print(aa)

# 여러 개의 항목을 삭제하려면 'aa[시작:끝+1]=[]' 문장으로 설정
aa = [10, 20, 30, 40, 50]
aa[1:4] = []
print(aa)

"2. 리스트에 for 문 활용"
# 100개의 리스트를 만들 경우 append()와 함께 for 문을 활용
aa = []
for i in range(0,100):
    aa.append(0)

print(len(aa))

# 콜론의 앞이나 뒤 숫자의 생략도 가능
aa = [10, 20, 30, 40]
print(aa[2:])
print(aa[:2])

"""리스트 연산자 실습하기"""
# + 연산자
primes = [2, 3, 5, 7, 11, 13, 17, 19]

newlist = primes + [23, 29, 31] # 집합 결과를 새 리스트에 배정
print(newlist)

primes = primes + [23, 29, 31] # 기존 리스트를 수정
print(primes)

# + 연산자로 값 합치기
list2 = [37, 23, 10, 33, 29, 40]
print(list2)

list2.append(16)
print(list2)

list3 = list2 + [16]
print(list3)

list4 = list2 + list3
print(list4)