def solution(A):
    permutation = [0]*len(A)
    for a in A:
        if a-1 < len(permutation) and permutation[a-1] != 1:
            permutation[a-1] = 1
        else:
            return 0
    if sum(permutation) == len(A):
        return 1
    else:
        return 0