"""5. N을 입력 받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오(format 활용)"""

a = int(input("구구단의 아무단을 입력하세요."))
for i in range(1, 10):
    print(f"{a} X {i} = {a*i}")