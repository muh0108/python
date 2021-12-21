num = int(input("수를 입력하세요 : "))

if num<=9 and num>0:
    print("%d은(는) 한 자리 숫자이다." %num)
elif num<=99 and num>=10:
    print("%d은(는) 두 자리 숫자이다." %num)
elif num <=999 and num>=100:
    print("%d은(는) 세 자리 숫자이다." %num)
else:
   print("오류! %d은(는) 범위(0~999) 이외의 숫자이다." %num)