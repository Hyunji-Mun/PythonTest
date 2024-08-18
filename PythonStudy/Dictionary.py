"""딕셔너리의 생성 및 사용 실습하기"""

"""1. 기본적인 딕셔너리 생성"""
dic1 = {1:'a', 2:'b', 3:'c'}
print(dic1)

# 키와 값을 반대로 생성
dic2 = {'a':1,'b':2,'c':3} # 키와 값은 사용자가 지정하는 것이지 규정은 없음
print(dic2)                # 주의할 점: 딕셔너리에는 순서가 없어서 생성한 순서대로 딕셔너리가 구성되어있다는 보장이 없음

"""2. 여러 정보의 딕셔너리 표현"""
student1 = {'학번':1000, '이름':'홍길동','학과':'컴퓨터학과'}
print(student1)

"""3. 딕셔너리 추가"""
# student1에 연락처 추가
student1['연락처']='010-1111-2222'
print(student1)

"""4. 딕셔너리 수정 및 삭제"""
# 학과 수정
student1['학과']='체육학과'
print(student1)

# student1의 학과 삭제
del(student1['학과'])
print(student1)

# 딕셔너리명.get(키) 함수를 사용해 키로 값에 접근
student1.get('이름')

"""튜플을 딕셔너리로 바꾸는 실습하기"""
# 1. 튜플 타입의 개념
# - 변경할 수 없는 열거 데이터의 집합
# - 리스트 타입과 달리, 한 번 값이 정해지면 항목의 값을 변경할 수 없음
# - 리스트는 대괄호 []로 생성, 튜플은 소괄호 ()로 생성
tt1 = (10,20,30);
print(tt1)
tt2 = 10, 20, 30;
print(tt2)

# 2. 튜플 타입 선언 및 사용
# - 튜플은 소괄호 ()를 생략 가능
# - 항목이 하나인 튜플은 뒤에 쉼표(,)를 붙임
card='red',4,'다이아몬드',True # 튜플 생성
print(card) # 튜플 값 확인
#card[-1]=False  # 튜플 마지막 값 변경 시도
print(card[2]) # 세 번째 항목 값 확인
print(card[:2]) # 첫 번째~두 번째 항목 자르기
print(card[2:]) # 세 번째~마지막 항목 자르기
print(card[:]) # 전체 튜플 복사하기

# 3. 튜플을 딕셔너리로 변환하기
programmer_list = [('Python',7),('Java',2)] # 리스트 생성
print(programmer_list) # 리스트 값 확인

programmer_dict = dict(programmer_list) # 딕셔너리로 변환
print(type(programmer_dict)) # 데이터 타입 확인
print(programmer_dict) # 딕셔너리 값 확인
print(programmer_dict['Python'])
print(programmer_dict['Java'])