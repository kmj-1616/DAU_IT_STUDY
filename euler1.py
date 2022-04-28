##오일러 함수 e 구하기
from week06.prg05 import * #factorial 함수 호출하기
def euler(n):
    output=0
    for i in range(n+1):
        output+=1/factorial(i)
    return output
print(round(euler(20),4))
