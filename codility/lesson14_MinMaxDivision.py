def is_valid(A, K, max_sum):
    # 배열 A를 K개의 블록으로 나눌 때, 블록의 합이 max_sum 이하인지 확인
    block_sum = 0
    block_count = 0

    for element in A:
        block_sum += element
        if block_sum > max_sum:
            # 새로운 블록 시작
            block_sum = element
            block_count += 1

    # 나눈 블록의 수와 K 비교
    return block_count + 1 <= K


def solution(K, M, A):
    min_val = max(A) #Lower Bound
    max_val = sum(A) #Upper Bound

    while min_val <= max_val:
        mid = (min_val + max_val) // 2

        if is_valid(A, K, mid):
            max_val = mid - 1
        else:
            min_val = mid + 1

    return min_val