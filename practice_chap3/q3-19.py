pay = int(input("구매 금액은?"))

if pay > 10000 and pay <= 50000 :
    rate = 5
elif pay > 50000 and pay <= 300000 :
    rate = 7.5
elif pay > 300000 :
    rate = 10
else :
    rate = 0
discount = pay*(rate/100)
res = pay-(pay*(rate/100))
print("구매금액 %d:" %pay)
print("할인율 : %.1f" %rate)
print("할인금액 : %.0f" %discount)
print("지불금액 : %.0f" %res)