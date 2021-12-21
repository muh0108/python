count=0

for num in range(200,801):
    if num%5 !=0 :
        print(num,end="\t")
        count+=1
        
        if count %10 ==0:
            print()