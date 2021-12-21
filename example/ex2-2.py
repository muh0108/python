"""
print()함수를 이용한 데이터 풀력
-작성자 : 홍길동
-일자 : 2021.11.02
"""
'''
작은 따옴표 세개를 
사용해도 됩니다!
'''
name = input("당신의 이름은?") #변수 name : 이름

#변수 birth : 탄생년
birth = int(input("당신의 태어난 해는?"))

age=2021-birth+1 #변수 age : 나이

print("%s님의 나이는 %d세 입니다." %(name, age))
