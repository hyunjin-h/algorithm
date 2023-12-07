n,m,s=map(int,input().split())
adj_arr=[[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    adj_arr[a][b]=1
    adj_arr[b][a]=1


visited=[None]*(n+1)

def bfs(i):
    queue=[]
    visited[i]=True
    queue.append(i)
    while len(queue)!=0:
        v=queue.pop(0)
        print(v)
        for w in range(1,n+1):
            if adj_arr[v][w] and not visited[w]:
                visited[w]=True
                queue.append(w)

print('[BFS 방문순서]')
bfs(s)
