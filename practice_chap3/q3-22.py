ft = int(input("첫 번째 시간의 시를 입력하세요:"))
fm = int(input("첫 번째 시간의 분을 입력하세요:"))
st = int(input("두 번째 시간의 시를 입력하세요:"))
sm = int(input("두 번째 시간의 분을 입력하세요:"))

first = str(ft)+":"+str(fm)
second = str(st)+":"+str(sm)


if ft < st :
    past = first
    late = second
elif ft > st :
    past = second
    late = first
elif ft == st:
    if fm < sm :
        past = first
        late = second
    else :
        past = second
        late = first

print("- 빠른 시간 %s" %past)
print("- 늦은 시간 %s" %late)