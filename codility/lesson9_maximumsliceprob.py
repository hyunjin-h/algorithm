#O(n)
def golden_max_slice(A):
    max_ending=max_slice=0
    for a in A:
        max_ending=max(0,max_ending+a)
        # +가 된다면 max_ending에 계속 쌓아가기
        # -라면 0부터 다시 시작하기

        # max_slice 찾기
        max_slice = max(max_slice, max_ending)

    return max_slice