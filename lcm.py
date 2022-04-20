from math import gcd #표준라이브러리 math에서 gcd 호출

def lcm(a,b):
    return a*b // gcd(a,b) #a*b/a와 b의 최대공약수가 a,b의 최소공배수

print(lcm(10,12))
#결과 60
