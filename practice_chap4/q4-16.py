str = input("문장을 입력해 주세요 :")
# res = ''  # 기존 문자열을 역순으로 담아줄 빈 문자열 선언
# i = 0
# while i < len(str) :
#     char = str[i]
#     if char == " ":
#         char = "-"
#     res = char + res
#     i+=1
# print(res)

i = len(str)-1
while i>=0:
    if str[i] == " ":
        print("-",end="")
    else:
        print("%s" %str[i],end="")
    i-=1
    

# for char in str:
#     if char == ' ':
#         char = '-'
#     res = char + res
    
# print(res)