def solution(A):
	A = [1] + A + [1] #시작과 끝지점에 1삽입
	matches = [0]*len(A)
	fib = fibonacciDynamic(len(A))
	for e in range(1, len(A) ):
		if A[e] == 0:
			continue
		min_cnt = len(A)
		for j in fib[2:]: #피보나치배열돌기
            # 현재위치랑 피보나치수가 일치하거나,// 현재위치가 피보나치수가 크고 점프 전 위치에 온적 있을때(?)
			if e - j == 0 or (e - j >= 0 and matches[e - j] != 0):
				min_cnt = min(min_cnt, matches[e - j] + 1)
		if min_cnt != len(A):
			matches[e] = min_cnt #match[현재위치]에 최소 카운트 삽입
	if matches[-1] != 0:
		return matches[-1]
	else:
		return -1

def fibonacciDynamic(n):
	fib = [0] * (n+2)
	fib[1] = 1
	for i in range(2, n + 2):
		fib[i] = fib[i - 1] + fib[i - 2]
		if fib[i] > n:
			return fib[:i+1]
	return fib