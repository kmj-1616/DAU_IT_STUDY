##factorial 재귀함수

def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)

print("5!=",factorial(5))