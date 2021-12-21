#점수에 따라 등급(A,B,C,D,F)판정하기

grade = input("등급을 입력해 주세요(A+,A,B+,...,F): ")

if grade == "A+" :
    score = 4.5
elif grade == "A" :
    score = 4.0
elif grade == "B+" :
    score = 3.5
elif grade == "B" :
    score = 3.0
elif grade == "C+" :
    score = 2.5
elif grade == "C" :
    score = 2.0
elif grade == "D+" :
    score = 1.5
elif grade == "D" :
    score = 1.0
else :
    score = 0
    
print("등급 : %s, 평점 : %.1f" %(grade,score))
    