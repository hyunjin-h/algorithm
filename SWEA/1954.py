#dx,dy를 활용. 벽이나 이미 채워진곳 부딪히면 방향 전환

T=int(input())
# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def in_range(x,y):
    return x>=0 and x<n and y>=0 and y<n and arr[x][y]==0
for testnum in range(1,T+1):
    n=int(input())


    arr=[[0]*n for _ in range(n)]
    x,y=0,0
    move_dir=0


    for i in range(1,n*n+1):
        arr[x][y] = i
        nx,ny=x+dx[move_dir], y+dy[move_dir]
        if in_range(nx,ny):
            x,y=nx,ny
        else:
            move_dir=(move_dir+1)%4
            x,y= x + dx[move_dir], y + dy[move_dir]

    print(f'#{testnum}')
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()
