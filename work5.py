###BMI계산하기
weight=float(input("체중(kg)을 입력=>"))
height=float(input("키(m)를 입력=>"))
bmi=weight/(height**2)
print("당신의 BMI는 %10.3f입니다"%bmi)
