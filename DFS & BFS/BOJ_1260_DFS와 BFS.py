# 링크 : https://www.acmicpc.net/problem/1260
# 솔루션 참고 링크 : https://ji-gwang.tistory.com/291
# 정점 활용하는 방식

from collections import deque

def dfs(v) :
    visited_d[v] = True
    print(v, end=' ')

    for i in graph[v] :
        if not visited_d[i]:
            dfs(i)

def bfs(v) :
    q = deque([v])
    visited_b[v] = True
    while q :
        node = q.popleft()
        print(node, end=' ')

        for i in graph[node] :
            if not visited_b[i] :
                visited_b[i] = True
                q.append(i)

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

''' 비효율적 입력 코드 
input_graph = []

for _ in range(m) :
    input_graph.append(list(map(int, input().split())))
input_graph.sort(key = lambda x : x[0]) # 오름 차순 정렬
graph = [[] for _ in range(n+1)]

# 입력 받아 오면서 바로 해당 리스트로 정렬할 수 있음
# 인덱스: 정점 , 배열값: 정점과 연결된 노드 집합으로 정리 (ex. graph[1] = (2,3) )
for i in range(n+1) : #(n+1)이어야 n번 정점까지 간선 정보 기록할 수 있음
    for j in range(m) :
        if input_graph[j][0] == i:
            graph[i].append(input_graph[j][1])
        if input_graph[j][1] == i:
            graph[i].append(input_graph[j][0])

print(graph)
'''

visited_d = [False]*(n+1)
visited_b = [False]*(n+1)

bfs(v)
dfs(v)


# **주의
# [ 문법 ]
# 파라미터 넘겨줄 때 (넘겨줘야 하는 요소와 전역인 요소 구분)
# 정렬 함수 내 람다 함수 사용
# 2차원 배열 만드는 법 : graph = [[] for _ in range(n+1)]
# length 정해진 1차원 배열 만드는 법 : visited = [False]*n+1
# 줄바꿈 없이 출력 : print(node, end=' ')
# [ 풀이 ]
# 탐색 순서 마지막에 none이 나오는 문제
# graph 리스트를 잘못 구성했기 때문
# 양방향이라면 노드 순서 상관없이 간선으로 관계는 기준 노드별로 중복으로 기재해주어야 함
# 잘못된 리스트 : [[], [2, 3, 4], [4], [4], []]
# 맞는 리스트 :  [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]
# None 출력되는 에러 : print(dfs(v)) -> print 함수 잘못 사용해서