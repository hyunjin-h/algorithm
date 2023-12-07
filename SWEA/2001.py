import sys
sys.stdin = open("input.txt", "r")

T=int(input())
for test_num in range(1,T+1):
    n,m=map(int,input().split())
    fly=[list(map(int,input().split())) for _ in range(n)]
    cnt=[]
    for i in range(n-m+1):
        for j in range(n-m+1):
            sum_fly=0
            for k in range(m):
                for l in range(m):
                    sum_fly+=fly[i+k][j+l]

            cnt.append(sum_fly)
    print(f'#{test_num} {max(cnt)}')