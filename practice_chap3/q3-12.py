num = int(input("첫번째 숫자를 입력하세요 : "))

if num % 3 == 0  and num % 4 == 0:
    result = "3의 배수이면서 4의 배수이다."
elif num % 3 == 0:
    result = "3의 배수이다."
elif num % 4 == 0:
    result = "4의 배수이다."
else :
    result = "3의 배수도 4의 배수도 아니다."
    
print("%d은(는) %s" %(num, result))