month =int(input("월을 숫자로 입력하세요 :"))

if month == 12 or month <3 :
    print("%d월은 겨울입니다." %month)
elif month <6 :
    print("%d월은 봄입니다." %month)
elif month <9 :
    print("%d월은 여름입니다." %month)
elif month <12 :
    print("%d월은 가을입니다." %month)  
else :
    print("%d(은)는 달에 포함되지 않아요" %month)  
    