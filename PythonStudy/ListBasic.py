"""리스트의 기본 실습하기"""

"1. 리스트(lsit)"
 # 여러 가지 자료를 저장할 수 있는 자료
 # 자료들을 모아서 사용할 수 있게 해 줌
 # 대괄호 내부에 자료들 넣어 선언
array = [273, 32, 103, "문자열", True, False]
print(array)

"2. 요소(element)"
 # 리스트의 대괄호 내부에 넣는 자료
print([1,2,3,4]) # 숫자로만 구성된 리스트
print(["안","녕","하","세","요"]) # 문자열로만 구성된 리스트
print([273, 32, 103, "문자열", True, False]) # 여러 자료형으로 구성된 리스트

"3. 인덱스(index)"
 # 리스트 내부의 요소를 각각 사용하려면 리스트 이름 바로 뒤에 대괄호 입력 후 자료의 위치를 나타내는 숫자 입력
list_a = [273, 32, 103, "문자열", True, False]
print(list_a[0])
print(list_a[1])
print(list_a[2])
print(list_a[3])
print(list_a[4])
print(list_a[5])

"리스트를 선언하고 요소에 접근하는 실습하기"
 # 리스트 선언 후 요소 접근
list_a = [273, 32, 103, "문자열", True, False]
print(list_a[0])
print(list_a[1])
print(list_a[2])
print(list_a[1:3])

 # 리스트의 특정 요소 변경 가능
list_a = [273, 32, 103, "문자열", True, False]
list_a[0] = "변경"
print(list_a)

 # 대괄호 안에 음수 넣어 뒤에서부터 요소 선택하기
list_a = [273, 32, 103, "문자열", True, False]
print(list_a[-1])
print(list_a[-2])
print(list_a[-3])

 # 리스트 접근 연산자를 이중으로 사용 가능
list_a = [273, 32, 103, "문자열", True, False]
print(list_a[3])
print(list_a[3][0])

 # 여러 개의 리스트를 가지는 리스트
list_a = [[1,2,3],[4,5,6],[7,8,9]]
print(list_a[1])
print(list_a[1][1])