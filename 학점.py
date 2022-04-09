##학점 계산 프로그램
num=int(input("점수=>"))
if num>=90 :
    grade='A'
elif num>=80 :
    grade='B'
elif num>=70 :
    grade='C'
else:
    grade='F'

print("당신의 점수 %d, 학점 %c"%(num,grade))