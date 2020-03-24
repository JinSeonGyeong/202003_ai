""""2.if문을 이용해 첫번째와 두번 수, 연산기호를 입력하게 하여 계산값이 나오는 계산기를 만드시오"""

a = float(input('첫번째 숫자를 입력하시오.:'))
b = float(input('두번째 숫자를 입력하시오.:'))
c = input("연산기호를 넣으시오.:")
d = ['+', '-', '*', '/', '%']
if c == d[0]:
    print(a + b)
if c == d[1]:
    print(a - b)
if c == d[2]:
    print(a * b)
if c == d[3]:
    print(a / b)
if c == d[4]:
    print(a % b)
else:
    print("잘못입력하였습니다.")
