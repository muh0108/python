score1 = int(input("필기시험 점수는?"))
score2 = int(input("실기시험 점수는?"))

if score1 >= 80 and score2 >=80 :
    result = '합격'
else :
    result = '불합격'

print(" - 필기시험 점수 : %d" %score1)
print(" - 실기시험 점수 : %d" %score2)
print(" - 판정 : %s" %result)