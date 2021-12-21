print ("-" *50)
print ("    달러    원화    유로")
print ("-" *50)
daller = 10
while daller <= 100 :
    won = daller * 1080
    euro = daller * 0.81
    print("%7d %8.0f %7.1f" %(daller, won, euro))
    daller += 10
print ("-" *50)