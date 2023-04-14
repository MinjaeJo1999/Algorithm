from collections import deque


# 행 (1,1) 부터 시작
# 검은색은 벽
# 동,서,남,북
# 최단거리 구해야
# 도착할 수 없을 경우 -1
def bfs(maps, que):
    # 상,하,좌,우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    #print('1.', que)
    while que:
        r, c = que.popleft()
        for i in range(4):
            nr = r+ dr[i]
            nc = c+ dc[i]
            if nr < 0 or nr >= len(maps) or nc < 0 or nc >= len(maps[0]):  # 범위 벗어난 경우
                continue #나머지 너비 탐색 계속 해야하므로
            elif maps[nr][nc] == 0 :  # 해당 조건 까먹음
                continue
            elif maps[nr][nc] == 1:
                maps[nr][nc] = maps[r][c]+1
                que.append((nr, nc))

    return maps[len(maps)-1][len(maps[0])-1]

def solution(maps):
    answer = 0
    que = deque()
    que.append((0, 0))

    answer = bfs(maps, que)
    if answer == 1 :
        answer = -1
    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))

# ***주의
# [ 풀이 ]
# <실수들>
#벽 조건 까먹음
#bfs 안에서 재귀호출
#비효율적 for문 구성 (의미없는 노드 que에 추가되는 로직)
#continue 해야할 때 return
#0,1 숫자입력인데 문자열로 비교함
