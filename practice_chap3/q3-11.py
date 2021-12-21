num1 = int(input("첫번째 숫자를 입력하세요 : "))
num2 = int(input("두번째 숫자를 입력하세요 : "))

sum = num1 + num2
print("%d + %d = %d" %(num1,num2,sum))
if sum % 3 == 0 :
    print("%d은(는) 3의 배수이다." %sum)
else :
    print("%d은(는) 3의 배수가 아니다." %sum)
    