def solution(A):
	mx = max(A) #A의 최대값
	freq = [0] * (mx+1)
    #갯수세기
	for a in A:
		freq[a] +=1

	div = {} #div[a]에 a의 약수값들 넣을거임
	for a in set(A): #중복없애고 순환
		div[a] = list(set([1, a]))
	i = 2
	while i*i <= mx:
		k = i
		while k <= mx:
			if k in div and not i in div[k]: #div에 key값이 k가 있고, div[k]안에 k의 약수 i가 없는 경우
				div[k] += list(set( [i, k // i] )) # 0들어가도freq[0]에 아무값없어서 상관없어
			k += i
		i += 1
	result = []
	for a in A:
		cnt = 0
		for d in div[a]:
			cnt += freq[d]
		result.append( len(A) - cnt )
	return result