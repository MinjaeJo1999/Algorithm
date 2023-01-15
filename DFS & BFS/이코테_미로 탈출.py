# 링크 : https://www.youtube.com/watch?v=7C9RgOcvkvo
from collections import deque

def bfs(x, y) :
    queue = deque()
    queue.append((x,y))

    while queue :
        x, y = queue.popleft() # 1. 큐에서 빼기

        # 상하좌우로 이동할 수 있는 칸 방문
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
            if graph[nx][ny] == 0 :
                continue
            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny)) #2. 큐에 인접 노드 더하기
    return graph[n-1][m-1]


n,m = map(int, input().split())
graph=[]
for _ in range(n) :
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [ -1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))

# *** 미완 주의
# [ 풀이 ]
# 1) 왜 최단거리를 보장할 수 있는지 이해되지 않음
# 2) 상하좌우 이동에 우선 순위를 고려하지 않아도 되는 이유 찾지 못함
# >  1, 2 이유 : 최단거리 루트가 최단거리 아닌 제 n의 루트가 지나는 길을 미리 지날 때 배열값이 1이 아닌 더 큰 양수값(거리값)으로 바뀌게 되므로,
#               해당 지점에서 최단거리가 아닌 루트의 이동이 끊기고, 최단 거리가 보장됨
# 배열값을 이동 거리 저장하는 공간으로 활용