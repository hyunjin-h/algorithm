def solution(A):
    # leader 찾기
    size = 0
    for k in range(len(A)):
        if (size == 0):
            size += 1
            candidate = A[k]
        else:
            if (candidate != A[k]):
                size -= 1
            else:
                size += 1
    if size <= 0:
        return 0

    # prefix sum ->이 지점에서 끊으면 왼쪽,오른쪽 leader 갯수 알 수 있게됨
    idx = [0]
    for k in range(len(A)):
        offset = 0
        if (A[k] == candidate):
            offset = 1
        idx.append(idx[-1] + offset)
        # 해당 숫자(A[k])가 leader가 맞으면 offset=1이므로 개수 추가된 상태로 idx 리스트에 값 저장됨
        # idx엔 왼쪽 leader 갯수 저장됨
    res = 0
    # 여기서 idx[-1]은 총 leader 갯수
    if (idx[-1] > len(A) // 2):
        for i, k in enumerate(idx[1:]):
            if k > (i + 1) // 2 and idx[-1] - k > (len(A) - (i + 1)) // 2:  # 왼쪽, 오른쪽 각각 체크
                res += 1
    return res