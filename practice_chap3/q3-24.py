print("="*50)
year = int(input("현재년은?"))
month = int(input("현재월은?"))
day = int(input("현재일은?"))
birthYear = int(input("출생년은?"))
birthMon = int(input("출생월은?"))
birthDay = int(input("출생일은?"))

print("="*50)
print("오늘날짜 : %d년 %d월 %d일" %(year, month, day))
print("생년월일 : %d년 %d월 %d일" %(birthYear,birthMon,birthDay))
print("-"*50)

if birthMon == month :
    if birthDay < day :
        age = year - birthYear 
    else :
        age = year - birthYear -1
elif birthMon < month and birthMon > 0:
    age = year - birthYear 
elif birthMon > month and birthMon < 13:
    age = year - birthYear -1
else :
    print("출생월은 1~12월까지로 입력해주세요")

print("만 나이 : %d세" %age)
print("="*50)