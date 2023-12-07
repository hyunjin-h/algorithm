n=int(input())

for i in range(1,n+1):
    cnt=0
    for s in str(i):
        if s=='3' or s=='6' or s=='9':
            cnt+=1
    if cnt==0:
        print(i,end='')
    else:
        for _ in range(cnt):
            print('-',end='')
    print(end=' ')