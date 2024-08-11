"""기본 for 문 실습하기"""

# 1. 같은 작업 나열 vs 반복 구조
# 같은 작업을 여러번 나열하여 작성
print("안녕하세요!")
print("안녕하세요!")
print("안녕하세요!")
print("안녕하세요!")
print("안녕하세요!")

# 반복 구조를 이용하여 작성한 코드
for i in range(5):
	print("안녕하세요!")

# 2. 1부터 100까지의 합을 구하는 프로그램
sum = 0
for i in range(1,101):
	sum += i
print("1부터 100까지의 합은",sum,"입니다.")

"""중첩 for 문 실습하기"""
#중첩 반복문의 예1
for i in range(5):
	for j in range(10):
		print("*",end="")
	print("")

#중첩 반복문의 예2
for i in range(1,6):
	for j in range(1,i+1):
		print("*",end="")
	print("")