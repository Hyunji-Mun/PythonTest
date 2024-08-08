"""기본 if문 실습하기"""

"""1. 문자열의 비교 실습"""
print('cat'<'dog') #True # 알파벳 순서
print('Dog'<'dog') #True # 대문자는 소문자보다 앞에 위치
print('Dog'<'cat') #True # 모든 대문자는 소문자보다 앞에 위치
print('알고리즘'>'파이썬')  #False # 한글은 가나다 순서를 따름
print('알고리즘'>'algorithm') #True # 한글은 알파벳보다 뒤에 위치

"""ERROR 발생
print(123 > "CPU") #숫자와 문자열을 비교
 "Traceback (most recent call last):
    print(123 > "CPU") #숫자와 문자열을 비교
TypeError: '>' not supported between instances of 'int' and 'str'"""

"""2. 논리 연산자 실습"""
# 논리 연산자 and
print(3<4 and 7<8) #True
print(3<4 and 7>8) #False

# 논리 연산자 or
print(3<4 or 7<8) #True
print(3<4 or 7>8) #True

# 논리 연산자 not
print(not 7<8) #False
print(not 7>8) #True

"""3. 조건이 거짓이고 실행할 문장이 2개일 때"""
a=200
if a<100:
    print("100보다 작다.")
print("거짓이므로 이 문장은 안 보이겠죠?")
print("프로그램 끝")

"""4. 조건이 거짓이고 실행할 문장이 1개일 때"""
a=200
if a<100:
    print("100보다 작다.")
    print("거짓이므로 이 문장은 안 보이겠죠?")
print("프로그램 끝")

"""5. if문에서 두 문장 이상을 실행하고자 할 때"""
a=200
if a<100:
    print("100보다 작다.")
    print("참이면 이 문장도 보이겠죠?")
else:
    print("100보다 크다.")
    print("거짓이면 이 문장도 보이겠죠?")
print("프로그램 끝")

"""6. 입력 숫자가 짝수인지 홀수인지 계산"""
a=int(input("정수를 입력하세요:"))
if a % 2 == 0:
    print("짝수를 입력했군요.")
else:
    print("홀수를 입력했군요.")


"""if의 복합문 실습하기"""
#if의 중첩 실습
num = int(input("정수를 입력하시오."))
if num >= 0:
    if num == 0:
        print("0입니다.")
    else:
        print("양수입니다.")
else:
    print("음수입니다.")


#if-elif-else
num = int(input("정수를 입력하시오."))
if num > 0:
    print("양수입니다.")
elif num == 0:
    print("0입니다.")
else:
    print("음수입니다.")
