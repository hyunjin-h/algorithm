def solution(A):
    nA = []
    for a in A:
        if len(nA) == 0 or a != nA[-1]:
            nA.append(a)
    front, distinct_cnt = len(nA) - 1, 0

    for back in range(len(nA)):

        abs_back_val = abs(nA[back])
        while front >= back:

            abs_front_val = abs(nA[front])
            if abs_back_val != abs_front_val:
                distinct_cnt += 1

            if abs_back_val >= abs_front_val:
                break
            else:
                front -= 1

    return distinct_cnt + 1
