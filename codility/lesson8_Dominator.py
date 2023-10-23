def solution(A):
    n = len(A)
    #가장 많이 나온 수 찾기
    size = 0
    for k in range(n):
        if (size == 0):
            size += 1
            value = A[k]
        else:
            if (value != A[k]):
                size -= 1
            else:
                size += 1

    candidate = -1
    if (size > 0):
        candidate = value

    idx = []
    for k in range(n):
        if (A[k] == candidate):
            idx.append(k)

    if (len(idx) > n // 2):
        return idx[0]
    else:
        return -1