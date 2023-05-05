import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선의 개수를 입력받기
n,m = map(int, input().split())
#시작 노드 번호를 입력받기
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선 정보를 입력받기
for _ in range(m) :
    a, b, c = map(int, input().split())
    #a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

def dijkstra(start) :
    q = []
    #시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: #큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist : # ?? 이해 안되었던 부분 / 해당 코드를 통해 visited 배열 없이 방문 유무(최단거리 확보했는지의 유무)를 확인할 수 있음
            print(distance[now], dist, now, q)
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now] :
            cost = dist + i[1]
            if cost < distance[0] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

#다익스트라 알고리즘을 수행
dijkstra(start)

#모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1) :
    #도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF :
        print("INFNITY")
    #도달할 수 있는 경우 거리를 출력
    else :
        print(distance[i])

''' 입력값
6 11
1
1 2 2
1 4 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3 
4 5 1 
5 3 1
5 6 2
'''

# 이해
'''
if distance[now] < dist:  # ?? 이해 안되었던 부분
    print(distance[now], dist, now, q)
    continue
'''
# 다익스트라는 노드 순으로 탐색하는 것이 아니라
# 시작 노드부터 시작하되 '최단거리' 기준으로 탐색하면서 값 갱신함
# 그래서 heapq에는 같은 노드에 다른 거리 정보가 push 될 수가 있음 (힙 구조를 사용하므로 push된 순서가 아닌 최단거리 순으로 정렬됨)
# 예를 들어, heapq에 노드3에 대한 정보가 이미 있는데
# 중간 과정에서 노드3의 최단 거리값이 갱신되어 distance[3]의 값이 바뀌고, heapq에 해당 정보가 추가될 수 있음
# 그렇다면 이미 있는 정보값은 의미가 없어짐
# heapq에 있는 그러한 노드 정보를 pass 하도록 하는 로직임
# > distance 리스트와 heapq가 갱신 함께 한다고 생각했음
# > distance는 인덱스 == 노드이고 최소값이 갱신되는 공간이지만
# > 각 인접 노드의 값 갱신되는 모든 순서쌍이 다 담기는 공간 이라는 점 캐치하지 못했음

# 복습 요함