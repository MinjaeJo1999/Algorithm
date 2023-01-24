# 링크 : https://www.acmicpc.net/problem/1697
# 솔루션 참고 링크: https://wook-2124.tistory.com/273
# 참고 링크 : https://programmers-story.tistory.com/9
from collections import deque

n, k = map(int, input().split())
max = 100000
root = [0 for _ in range(max+1)] # 두배곱으로 인해 k 보다 큰 수에 접근할 수도 있으므로 여분 값 두기

def bfs(start) :
    que = deque([start])
    while que :
        x = que.popleft()
        if x==k :
            return root[x]
        for nx in (x-1, x+1, x*2) :
            if 0<=nx<=max and not root[nx] : #인덱스, 방문체크 필수
                que.append(nx)
                root[nx] = root[x] + 1


def bfs2(start) :
    que = deque([start])
    while que :
        x = que.popleft()
        if x==k :
            return root[x]
        for nx in (x*2, x+1, x-1) :
            if 0<=nx<=max and not root[nx] :
                que.append(nx)
                root[nx] = root[x] + 1

print(bfs(n))
root = [0 for _ in range(max+1)]
print(bfs2(n))



# *** 주의 (의문점 미해결)
# [ 풀이 ]
# DFS > 시간 초과
# BFS > 갈 수 있는 3가지 루트를 BFS 경로로 탐색
# cnt 계산하는 데서 막힘 > 이전 값에서 +1씩 축적하면서 root 배열에 시간 흐름 저장, 마지막에 최댓값
# 방문한 곳은 배열에 시간 업데이트 하지 않음
# > WHY ?
#   > 매 초 방문할 수 있는 위치를 순차적으로 접근하기 때문에 값에 도달한 순간의 시간이 최소가 됨
#       > Q. 예를 들어 x번 위치를 먼저 방문하는 A 루트와 x번 위치를 나중에 방문하는 최적의 해를 보장하는 정답 루트가 있다면,
#       > x번의 위치는 A루트 이후로 업데이트 되지 않아 정답 루트까지 가는 시간을 정확히 계산할 수 없지 않나?
#           > 정답 루트에 x번 위치가 포함되어 있다면, x번 위치까지 가장 빠르게 도달하는 루트는 A루트이므로, X번까지의 A루트를 확보하고 다시 정답까지의 최적 루트를 찾으면 됨
#           > 이러한 논리에 따라 결국 x번 위치에 가장 빠르게 도달하는 A루트가 정답 루트일 것임 (정답 루트에 x번 위치가 포함되어 있다면)
# for nx in (x-1, x+1, x*2) 에서 순서 중요, x*2 x+1 x-1 순으로 탐색하면 오답
# > WHY ? (미해결)
#   > 가까운 곳부터 순차적으로 탐색해야
#   > 반례 못찾음
# [ 문법 ]
# 인덱스 초과 관련 예외 처리
