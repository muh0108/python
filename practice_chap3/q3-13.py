#왼쪽에서 세번째 자리의 수가 짝수인지 홀수인지 판별하는 프로그램
num = input("숫자를 입력하세요 : ")
a = int(num[2])

if a % 2 == 0 :
    result = "짝수이다."
else :
    result = "홀수이다."

print("%d은(는) %s" %(a, result))