#factorization=인수분해

# array F 준비!, 자기의 약수 중 가장 작은 소수 arr
def arrayF(n):
    F=[0]*(n+1)
    i=2
    while i*i<=n:
        if F[i]==0:
            k=i*i
            while k<=n:
                if F[k]==0:
                    F[k]=i
                k+=i
        i+=1

# O(log x)
def factorization(x, F):
    primeFactors = []
    while (F[x] > 0):
        primeFactors += [F[x]]
        x /= F[x]
    primeFactors += [x]
    return primeFactors
