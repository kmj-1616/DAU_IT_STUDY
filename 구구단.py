##입력한 수의 구구단을 출력하는 프로그램
su=int(input("수를 입력="))
for i in range(1,10,1):
    print("%d*%d=%d"%(su,i,su*i))