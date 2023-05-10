# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/86971

import copy
def my_wrong_solution(n, wires):
    answer = 100

    def dfs(tree, idx, node):
        i = idx
        while True:
            if not tree[i] and i != 1:
                return
            if i==1 and not tree[i] : # 맨 처음 파라미터인 1이 비어있을 경우 예외처리
                i+=1
                continue
            target = tree[idx]
            for j in range(len(target)):
                connect = target[j] # 연결되어 있는 송전탑
                node.append(connect) # 실수: 인덱스 에러
                del tree[i][j]
                dfs(tree, connect, node)
        node = set(node)
        print(node)
        difference = n - len(node)
        print(difference)
        return difference

    for i in range(len(wires)):
        tmp = copy.deepcopy(wires)
        del tmp[i]
        tree = [[] for _ in range(n + 1)]
        for node, connect in tmp:
            tree[node].append(connect)
        answer = min(answer, dfs(tree, 1, [1])) # 탐색 시작하는 idx
    return answer

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
#print(solution(n, wires))


# *** 주의
# [ 풀이 ]
# 접근 :
# 1. 완전 탐색 : wires에 주어진 모든 간선을 하나씩 지우는 경우의 수
# 2. 각 경우마다 dfs 돎
#     > 1부터 시작해서 (1이 비어있으면 그 다음) dfs로 방문할 수 있는 노드 다 방문
#     > 방문한 노드 리스트에 추가
# 3. 방문 마쳤다면 set으로 중복 노드 없애고
# 4. 전체 노드 - 방문한 노드 (=갈라진 두쪽 중 한쪽의 노드 개수)
# 구현 실패함 (시간 초과, return 조건 부적절)


# 풀이 출처 : https://velog.io/@s2ul2/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4level2-%EC%A0%84%EB%A0%A5%EB%A7%9D%EC%9D%84-%EB%91%98%EB%A1%9C-%EB%82%98%EB%88%84%EA%B8%B0-Python%ED%8C%8C%EC%9D%B4%EC%8D%AC
# bfs 활용
from collections import deque

def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    cnt = 0
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        #print(v, end=' ')
        cnt += 1
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return cnt

def solution1(n, wires):
    answer = n - 2 #  두 전력망이 갖게 되는 송전탑의 개수 차이의 절댓값 중 최댓값 (만약 n이 9일때 최대 절댓값은 두 전력망이 1과 8일때 즉 7이된다.)
    for i in range(len(wires)):
        tmps = wires.copy()
        graph = [[] for i in range(n+1)]
        visited = [False] * (n+1)
        tmps.pop(i) # i번째 전선 제거
        for wire in tmps:
            x, y = wire
            graph[x].append(y)
            graph[y].append(x)
        for idx,g in enumerate(graph):
            if g != []: # n개의 송전탑 중 다른 송전탑과 연결된 송전탑을 시작점으로 지정
                start = idx
                break
        cnts = bfs(graph, start, visited) # bfs를 이용하여 시작점에서 다른 송전탑 탐색함. 이때 탐색 가능한 송전탑 개수를 cnts에 담음(이는 즉 연결된 송전탑의 개수임)
        other_cnts = n - cnts # 전력망을 둘로 나눌 때 첫번째 전력망 개수는 cnts이므로 나머지 전력망 개수는 n - cnts로 구한다.
        if abs(cnts - other_cnts) < answer:
            answer = abs(cnts - other_cnts)
    return answer


# 집합 활용 , 이해 못함
def solution2(n, wires):
    ans = n
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
        s = set(sub[0])
        [s.update(v) for _ in sub for v in sub if set(v) & s]  # 집합연산자 & : 교집합 연산,   집합연산자 update : 여러데이터를 한번에 추가
        ans = min(ans, abs(2 * len(s) - n))
    return ans


# 풀이 출처 : https://velog.io/@ledcost/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-86971-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A0%84%EB%A0%A5%EB%A7%9D%EC%9D%84-%EB%91%98%EB%A1%9C-%EB%82%98%EB%88%84%EA%B8%B0-level-2-DFS-or-UF
# DFS 풀이
def DFS(v, graph, visited, check_link):
    cnt = 1
    visited[v] = True

    for adj_v in graph[v]:
        # 방문 이력이 없고, 그 간선이 임시로 없앤 간선이 아닌 경우
        if visited[adj_v] == False and check_link[v][adj_v]:
            cnt += DFS(adj_v, graph, visited, check_link)

    return cnt


def solution3(n, wires):
    answer = INF

    # 없앤 간선인지 아닌지 체크 값이 들어있는 리스트
    check_link = [[True] * (n + 1) for _ in range(n + 1)]

    graph = [[] for _ in range(n + 1)]
    cnt_all = []

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        visited = [False] * (n + 1)

        check_link[a][b] = False  # a-b 간선 끊기
        cnt_a = DFS(a, graph, visited, check_link)
        cnt_b = DFS(b, graph, visited, check_link)
        check_link[a][b] = True  # a-b 간선 다시 연결

        answer = min(answer, abs(cnt_a - cnt_b))

    return answer


# 다른 풀이 : 유니온 파인드 (개념 학습 전)

#복습 요함, 이해 미완