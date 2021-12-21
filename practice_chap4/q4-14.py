num=1
sum=0
count=0
while num < 100:
    if( num % 2 == 1):
        sum+=num
        print("%6d" %sum, end="\t")
        count = count+1
        
        if count % 10 == 0 : 
            print()
    num=num+1