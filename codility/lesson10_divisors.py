#약수 갯수세기 함수
def divisors(n):
    i=1
    result=0
    while i*i<n: #1부터 √n까지 반복하면 모든 약수을 찾을 수 있음
        if n%i==0:
            result+=2
        i+=1
    if i*i==n:
        result+=1

    return result