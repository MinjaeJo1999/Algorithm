import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n,m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)] #-> 노드 1부터 시작해서 +1?
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * (n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m) :
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c)) # graph[a] = [(a,b), (b,C)] <- 리스트 형태가..맞아?

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node() :
    # ? start 가 어딘지에 대한 정보가.. 필요하지 않나..?
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1) :
        if distance[i] < min_value and not visited[i] :
            min_value = distance[i]
            index = i
    return index

def dijkstra(start) :
    #시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start] :
        distance[j[0]] = j[1]  # 시작 노드와 연결된 간선 거리 정보 update
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1) :
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now] :
            cost = distance[now] + j[i]
            #현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]] :
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1) :
    # 도달할 수 없는 경우, 무한(infinity)라고 출력
    if distance[i] == INF :
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else :
        print(distance[i])


# 성능 분석 :
# 총 O(v) 번에 걸쳐서 최단 거리가 가장 짧은 노드 선형 탐색해야
# 전체 시간 복잡도는 O(v^2)
# 일반적으로 최단 경로 문제에서 전체 노드의 개수가 5000개 이하라면 이 코드로 문제 해결 가능
# 하지만, 노드의 개수가 10000개 넘어가는 문제라면 ?
