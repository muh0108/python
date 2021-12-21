name = input("이름을 입력하세요 :")
time=int(input("일주일간 일한 시간을 입력하세요 :"))
pay = 12000 #시급
ot = 0 #초과근무시간(40시간을 초과한 시간)

if time > 40 :
    ot = time - 40 #40시간을 초과한 시간을 ot에 저장
    res = 40 * pay + (ot * pay * 1.5) #정상근무시간 40시간은 시급그대로, 초과근무시간에 시급*1.5
else :
    res = pay * time #초과근무시간이 없으면 시간당 시급으로 그대로 책정

print("- 이름 : %s" %name)
print("- 일주일간 일한 시간 : %d시간"%time)
print("- 오버타임 : %d시간" %ot)
print("- 주급 : %d원" %res) 