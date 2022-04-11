##전치행렬 구하기
matrix=[[10,20,30],
        [40,50,60],
        [70,80,90]]
t1=[]
for i in range(len(matrix)):
    t_row=[]
    for row in matrix:
        t_row.append(row[i])
    t1.append(t_row)
print("전치 행렬=",t1)