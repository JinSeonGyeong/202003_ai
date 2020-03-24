"""20. 1부터 100까지 369 게임을 하려고 한다.
3,6,9가 들어가는 부분에는 '짝' 을 출력하고,
5의 배수에는 '아자' 를 출력,
그외에는 수를 출력하는 프로그램을 만드시오."""

def num369(a):
    num = str(a)
    i = list(num)
    for i in num:
        if "3" in i or "6" in i or "9" in i:
            return True
    return False

def num5(b):
    num = str(b)
    i = list(num)
    for i in num:
        if "0" in i or "5" in i:
            return True
    return False

for j in range(1, 101):
    if num369(j) == True:
        print(str("짝"), end=' ')

    else:
        if num5(j) == True:
            print(str("아자"), end=' ')
        else:
            print(str(j), end=' ')
