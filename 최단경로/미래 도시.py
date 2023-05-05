INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1) :
    graph[a][a] = 0

for i in range(m) :
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split()) # k번 회사를 거쳐 x회사로

for i in range(1, n+1) :
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

answer = graph[1][k] + graph[k][x] # 스타트 지점 명시 x
if answer == INF :
    print(-1)
else :
    print(answer)

# 입력 예시
'''
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
'''

# ** 주의
# 플로이드 워샬의 2차원 배열
# graph = [[INF]*(n+1) for _ in range(n+1)]
# 자기 자신 -> 자기 자신으로 가는 배열 비용 초기화 빼먹지 말기