def solution(N):
	i = 1
	result = (N+1)*2 # N*1의 면적도 N이랍니다
	while (i * i < N):
		if (N % i == 0):
			result = min(result, i*2 + (N//i)*2 )
		i += 1
	if (i * i == N):
		result = min(result, i*4 )
	return result