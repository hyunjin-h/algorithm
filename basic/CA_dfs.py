n,m,s=map(int,input().split())
adj_list=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
for i in range(1,n+1):
    adj_list[i].sort()

visited=[None]*(n+1)


# DFS 함수 정의
def dfs(v):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v)
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in adj_list[v]:
        if not visited[i]:
            dfs(i)
print('[DFS 방문순서]')
dfs(s)



# 모범답안
# dfs(v) 안에 adj_list[v].sort() 넣어서 표현