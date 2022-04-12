##팩토리얼을 계산하는 코드를 for반복문 말고도 재귀함수로 작성할 수 있다.

def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)

#5!을 구해보자.
print("5!=",factorial(5))
