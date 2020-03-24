"""11. 최대공약수를 구하는 함수를 구현하시오"""

a = int(input("숫자를 입력하시오.:"))
b = int(input("숫자를 입력하시오.:"))
def min(a, b):
    while b:
        a, b = b, a % b
    return a

print(min(a, b))

"""인터넷에서 찾아봄."""