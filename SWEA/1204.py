import sys
sys.stdin = open("input.txt", "r")

T=int(input())
for testcase in range(1,T+1):
    n=int(input())
    score = list(map(int, input().split()))
    cnt = [0 for _ in range(101)]

    for i in score:
        cnt[i] += 1
    max_index = [i for i, v in enumerate(cnt) if v == max(cnt)]

    print(f'#{n} {max(max_index)}')