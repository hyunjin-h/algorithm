n=int(input())
arr=[[0]*n for _ in range(n)]
print(arr)
ans=0
for i in range(n):
    for j in range(n):
        for k in range(n):
            arr[k][j]=1
            for l in range(n):
                arr[i][l]=1
        sum_cnt=0
        for a in range(n):
            sum_cnt+=arr[a].count(0)
        ans+=sum_cnt
        arr=[[0]*n for _ in range(n)]
print(ans)