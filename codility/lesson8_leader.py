#Lesson8_Leader
#O(n)

def goldenLeader(A):
    n=len(A)
    #제일 많이 등장하는 수 찾기(stack알고리즘과 유사)
    size=0
    for k in range(n):
        if size==0:
            size+=1
            value=A[k]
        else:
            if value!=A[k]:
                size-=1
            else:
                size+=1
    #제일 많이 등장한 수가 과반초과인지 확인
    candidate=-1
    if size>0:
        candidate=value
    leader=-1
    count=0
    for k in range(n):
        if A[k]==candidate:
            count+=1
    if count>n//2:
        leader=candidate
    return leader