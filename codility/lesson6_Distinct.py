def solution(A):
    if len(A) == 0:
        return 0
    A.sort()
    cnt = 1
    for i in range(1, len(A)):
        if A[i] != A[i-1]:
            cnt+=1
    return cnt
