"""3.Enter key를 눌러 주사위를 던지게 한 후, 주사위의 눈이 높은 사람이 승리하는
간단한 주사위 게임을 만드세요"""

import random

print("주사위를 굴려주세요.")
a = input("첫번째 선수 Enter를 누르세요.")
b = input("두번째 선수 Enter를 누르세요.")
a = random.randint(1, 6)
b = random.randint(1, 6)

if a > b:
    print(a, b, "첫번째 선수가 이겼습니다!")
if a < b:
    print(a, b, "두번째 선수가 이겼습니다!")
if a == b:
    print(a, b, "둘 다 비겼습니다.")
