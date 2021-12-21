print("서비스 만족도 :")
print("1 : 매우만족")
print("2 : 만족")
print("3 : 불만족")

a = int(input("서비스 만족도는?(1/2/3)"))
pay = int(input("음식 값은? "))

if a == 1 :
    service = "매우만족"
    tip = pay*0.2
elif a == 2 :
    service = "만족"
    tip = pay*0.1
elif a ==3 :
    service = "불만족"
    tip = 0

print("서비스 만족도 : %s , 팁 : %d원" %(service,tip))
