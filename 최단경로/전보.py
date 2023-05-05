import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

def dijkstra(start) :
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q :
        dist, now = heapq.heappop(q)
        if distance[now] < dist :
            continue
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n, m, start = map(int, input().split()) # 도시의 개수, 통로의 개수, 메시지를 보내려는 도시
graph = [[] for i in range(n+1)] # 각 노드(= 인덱스)와 인접한 노드 정보 담는 리스트
distance = [INF] * (n+1)
for i in range(m) :
    x, y, z = map(int, input().split())
    graph[x].append((y,z))

dijkstra(start)

count = 0
max_distance = 0
for d in distance :
    if d != 1e9 :
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count-1
print(count-1, max_distance)

# *** 주의
# [ 풀이 ]
# 다익스트라 틀 외워서 활용
# 거리 문제에서 인덱스 잘 활용하기
#  > graph.append((x, y, z))  -> graph[x].append((y,z))

# 입력 예시
# 3 2 1
# 1 2 4
# 1 3 2
# 출력 예시
# 2 4