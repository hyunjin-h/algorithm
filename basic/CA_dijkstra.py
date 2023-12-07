import sys

INF = sys.maxsize
# 노드의 개수, 간선 갯수, 시작 정점
n, m, s = map(int, input().split())

g = [None] * n  # 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
visited = [False] * n
D = [INF] * n  # 최단 거리 테이블을 모두 무한으로 초기화
D[s] = 0
previous = [None] * n  # 최단경로 기록을 위한 list
previous[s] = s  # 시작정점의 경로 초기화

# 모든 간선 정보를 입력받기 (0~n-1입력입니다. 1~n 입력이면 테이블들 n+1로 초기화했었어야함)
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    g[a].append((b, c))

#######################################
for k in range(n):
    m = -1  # m:min_vertex
    min_value = sys.maxsize

    # 가장 가까운 정점찾기
    for j in range(n):
        if not visited[j] and D[j] < min_value:
            min_value = D[j]
            m = j
    visited[m] = True

    # 정점 m에 인접한 w와 (m,w)의 가중치 wt에 대해
    for w, wt in list(g[m]):
        if not visited[w]:
            if D[m] + wt < D[w]:
                D[w] = D[m] + wt  # Prim 알고리즘과 다른 부분
                previous[w] = m

# 출력
print('정점', s, '(으)로부터 최단거리: ')
for i in range(n):
    if D[i] == INF:
        print(s, ' 와(과) ', i, ' 사이에 경로없음.')
    else:
        print('[%d %d]' % (s, i), '=', D[i])
print('\n정점', s, '(으)로부터의 최단경로')
for i in range(n):
    back = i
    print(back, end='')
    while back != s:
        print('<-', previous[back], end='')
        back = previous[back]
    print()
