def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def solution(A):
    P = prefix_sums(A)
    cnt = 0
    for i, a in enumerate(A):
        if a == 0:
            cnt += (P[-1] - P[i])
        if cnt > 1000000000:
            return -1
    return cnt
