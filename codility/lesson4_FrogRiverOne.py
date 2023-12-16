def solution(X, A):
    rlist= [0] * X
    etime = 0
    for i, a in enumerate(A):
        if rlist[a-1] != 1:
            rlist[a-1] = 1
            etime+=1
        if etime == X:
            return i
    return -1
