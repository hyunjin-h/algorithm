def solution(A):
	max_ending = 0
	max_slice = A[0]
	for a in A:
		max_ending = max(a, max_ending + a) # a부터 reset(0 아님!)
		max_slice = max(max_slice, max_ending)
	return max_slice