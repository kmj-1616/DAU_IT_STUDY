##일반함수를 람다함수로 바꾸어 호출하기
def avg(data):
    return sum(data)/len(data) #평균을 구하는 일반함수

d=[20,15,18,20]
print(avg(d)) #결과: 18.25

s1=tuple(map(str,d))
print(s1)

avg1=lambda data:sum(data)/len(data) #람다함수로 바꾸기: 함수를 한 줄로
print(avg1(d)) #결과: 18.25 로 같음