print ("-" *50)
print ("\tcm\tmm\tm\tinch")
print ("-" *50)

for cm in range(1,51):
    mm = cm * 10
    m = cm * 0.01
    inch = cm * 0.3937
    print("\t%d\t%d\t%.2f\t%.2f" %(cm, mm, m, inch))

print ("-" *50)