"""논리 타입 실습하기"""
# 1. 참(True)과 거짓(False)데이터 확인

print(100<200) #100이 200보다 작은가?
print(100>200) #100이 200보다 큰가?
print(100==200) #100이 200과 같은가?
print(100!=200) #100은 200과 같지 않은가?
print(10<300) #10이 300보다 작은가?
print(50>500) #50이 500보다 큰가?
print(100==2000) #100이 2000과 같은가?
print(1000!=250) #1000은 250과 같지 않은가?

"""비교 연산자, 논리 연산자 실습하기"""
# 1. 비교 연산자와 논리 연산자 실습
print(100>200 or 400>300) #거짓 혹은 참인 경우
print(100>200 and 400>300) #거짓 그리고 참인 경우
print(not 100>200) #거짓의 반대인 경우
print(not 10<100)

# 2. 논리 타입을 숫자로 바꾸기
print(int(True)) #참 데이터를 숫자로 바꾸기
print(int(False)) #거짓 데이터를 숫자로 바꾸기

"""조건 분기문의 활용 실습하기"""
# 1. if-else문 실습
## 값 입력 ##
flag = input('마음에 드는 옷을 찾았나요?(Y/N):')
## 조건 분기 ##
if flag == 'Y':
    print(':)축하합니다!!')
else:
    print(':(아쉽군요.')

# 2. if-elif-else 문 실습
## 값 입력 ##
flag = input('마음에 드는 옷을 찾았나요?(Y/N):')
## 조건 분기 ##
if flag == 'Y':
    print(':)축하합니다!!')
elif flag == 'N':
    print(':(아쉽군요.')
else:
    print("'Y'또는 'N'으로만 입력하세요.")

# 3. 다자 택일 선택 구조
score = int(input("성적을 입력하시오:"))
if score>=90:
    print('grade=A')
if (score>=80) and (score < 90):
    print('grade=B')
if (score>=70) and (score < 80):
    print('grade=C')
if (score>=60) and (score < 70):
    print('grade=D')
if score<60:
    print('grade=F')