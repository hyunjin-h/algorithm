T=int(input())

for testcase in range(1,T+1):
    n=int(input())
    arr=list(map(int,input().split()))
    result=0
    sell=0
    for a in arr[::-1]:
        if a>=sell:
            sell=a
        else:
            result+=sell-a
    print('#{} {}'.format(testcase, result))
