def solution(A):
	buy = 200000
	profit = 0

	for a in A:
		buy = min(a, buy)
		profit = max(profit, a - buy) # a가 순차적으로 돌아서 buy가 a이전 주식가격의 최저가격임

	return profit