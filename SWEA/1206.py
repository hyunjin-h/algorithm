for testcase in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    result = 0
    for i in range(2, n - 2):
        if max(arr[i - 2], arr[i - 1], arr[i], arr[i + 1], arr[i + 2]) == arr[i]:
            result += arr[i] - max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2])
    print('#{} {}'.format(testcase,result))