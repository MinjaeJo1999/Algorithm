# 링크 : https://www.acmicpc.net/problem/1238
import heapq
INF = int(1e9)
n, m, x = map(int, input().split()) # 학생 수, 간선 수, 도착 마을
graph = [[] for i in range(n+1)] # 실수 : 배열 초기화 ([INF]로 함) 형태 정의한 뒤 코드 작성
for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a].append((b,c)) #a에서 b도시까지 걸리는 시간 c

distance = [INF] * (n+1)

# 학생들 각각 마을에 살고 있음 마을 -> 마을 간 이동 살피면 됨
# 시작점,끝점 같은 도로는 없으므로 같은 지점 -> 같은 지점 초기화 과정 생략
def dikjstra(start) :
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q :
        distant, now = heapq.heappop(q) # 실수 : 위치 거꾸로 초기화 함  (now, distant)
        if distance[now] < distant :
            continue
        for i in graph[now] : # graph[now] : (x, now~ x까지의 가중치)
            cost = distance[now] + i[1]
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dikjstra(x) # 오는 거리
time = [0] * (n+1)
for i in range(1, n+1) :
    time[i] = distance[i]

for i in range(1, n+1): # 가는 거리
        distance = [INF] * (n + 1) # 실수 : distance 초기화 필요
        dikjstra(i)
        time[i] += distance[x] # 실수 : x 위치의 distance 구해야 (i라고 잘못 씀)

print(max(time))


# 단방향이기 때문에 오는 길과 가는 길이 다를 수 있음
# (각각 다른 집) ~ X번 마을  (-> 다익스트라 반복 n번 반복) / X번 마을 ~ 집 (-> 다익스트라 가능)


# *** 주의
# [ 풀이 ]
# 다익스트라 틀 구현하는 과정에서 실수 잦음
# 정점의 개수가 많지 않으니 각각 다익스트라를 반복한다는 발상 자체는 맞았음

# <더 나은 발상>
# 다익스트라는 한 정점에서 모든 정점까지의 최단 경로를 구하는 알고리즘
# 그렇다면 모든 정점에서 한 정점으로 구하는 건 어떻게 해야 할까?
#  > 그래프를 다르게 만드는 방법으로 접근
#   > 역방향 그래프
# 역방향을 통해 X -> 특정노드의 역 방향 즉 특정노드 -> X까지 오는 경로를 역으로 타고 들어간다.
# 다시 이해 안되면 : https://kangmin1012.tistory.com/8

# 복습 요함