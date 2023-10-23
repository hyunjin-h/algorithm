def primality(n):
    i=2
    while i*i<=n:
        if n%i==0:
            return False
        i+=1
    return True #나눠지는게 없으면 소수!