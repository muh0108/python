price = int(input("책값은?"))
cut = int(input("할인율은?"))
deli = int(input("배송료는?"))
pay = price-(price*(cut/100))+deli

print("책 값 : %d원" % price)
print("할인율 : %d" %cut)
print("배송료 : %d원" %deli)
print("결제금액 : %d원" %pay)