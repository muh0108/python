num = input("하이픈(-)이 포함된 11자리 휴대폰 번호는?")

only=num.replace("-","")
only2=num[0:3]+num[4:8]+num[9:]
print(" - 입력된 휴대폰 번호 :",num)
print(" - 하이픈 삭제된 휴대폰 번호 :",only)
print(" == num[0:3]+num[4:8]+num[9:] :",only2)