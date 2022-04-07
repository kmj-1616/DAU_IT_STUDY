sum2=0
data=list(map(int,input("데이터 입력==>").split(" ")))
avg=sum(data)/len(data)
for val in data :
    sum2+=(val-avg)**2
print("평균:%5.3f,합계:%5d"%(avg,sum(data)))
print("최대값:%5d,최소값:%5d,범위:%5d"%(max(data),min(data),max(data)-min(data)))
print("분산:%10.4f"%(sum2/len(data)))
