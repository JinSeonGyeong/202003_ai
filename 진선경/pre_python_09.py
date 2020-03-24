"""
9. 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
점수를 입력했을 때 해당 학점이 출력되도록 하시오.
81~100 : A
61~80 : B
41~60 : C
21~40 : D
0~20 : F
"""

def ipt():
    a = int(input("점수를 입력하시오."))

    if a > 80 and a <= 100:
        print("점수 등급은 'A' 입니다.")
    if a > 60 and a <= 80:
        print("점수 등급은 'B' 입니다.")
    if a > 40 and a <= 60:
        print("점수 등급은 'C' 입니다.")
    if a > 20 and a <= 40:
        print("점수 등급은 'D' 입니다.")
    if a > 0 and a <= 20:
        print("점수 등급은 'F' 입니다.")
    if a > 100 or a < 0:
        print("다시 입력하세요.")
        return ipt()


ipt()