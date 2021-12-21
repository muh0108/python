num1 = int(input("첫 번째 정수는?"))
num2 = int(input("두 번째 정수는?"))
num3 = int(input("세 번째 정수는?"))

if num1 > num2 and num1>num3:
    largest = num1
elif num2 > num1 and num2>num3:
    largest = num2
elif num3 > num1 and num3>num2:
    largest = num3

print("%d, %d, %d중에서 가장 큰 수는 %d입니다." %(num1,num2,num3, largest))