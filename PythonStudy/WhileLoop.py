"""while 문을 사용하여 반복문 실습하기"""

""" 1. 문장을 3회 반복하도록 하는 while 문"""
i = 0 # for 문에서 사용한 변수와 시작값을 i = 0으로 while 문 위에 작성
while i < 3: # for 문의 끝값, while 문의 조건식인 i < 3으로 지정
    print("%d: 안녕하세요? while 문을 공부 중입니다. ^^"%i)
    i = i + 1 # for 문의 증가값, while문의 마지막에 i = i + 1로 작성

""" 2. 1과 10까지의 합 계산하기(1)"""
i, hap = 0,0

i = 1 # i의 시작값을 1로 지정
while i < 11: # i가 11보다 작으면 참, i가 10일 때 까지 5~6행 반복
    hap = hap + i # hap에 i값(처음에는 1)을 누적
    i = i + 1 # i를 1 증가

print("1에서 10까지의 합계: %d"%hap)

""" 2. 1과 10까지의 합 계산하기(2)"""
#제어 변수 선언
i = 1
sum = 0

# i 값이 10보다 작으면 반복
while i <= 10:
    sum = sum + i
    i = i + 1

print("합계는",sum)

"""무한 반복 while 문 실습하기"""

"""무한 루프 예(1)
i = 1
while i != 1.3:
    print(i)
    i = i + 0.1"""

"""무한 루프 예(2)
# 변수 선언
i = 0

# 변수i를 증가시키는 부분이 없어서 무한 루프가 됨
while i < 10:
    print("Hello!")"""

"""break, continue 실습하기"""

"""break 사용의 예"""
while True:
    light = input('신호등 색상을 입력하시오: ')
    if light == 'blue':
        break
print('전진!!')

"""continue 사용의 예(1)"""
hap, i = 0,0

for i in range(1,101):
    if i % 3 == 0:
        continue

    hap += i
print("1~100의 합계(3의 배수 제외): %d" %hap)

"""countinue 사용의 예(2)"""
for n in range(10):
    if n % 2 == 0:
        continue
    print(n)