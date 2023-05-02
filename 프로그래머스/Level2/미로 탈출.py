from collections import deque

def solution(maps):
    answer = -1
    # 레버를 만났는지 확인하는 변수

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    start_r = 101
    start_c = 101
    end_r = 101
    end_c = 101
    l_r = 101
    l_c = 101

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'S':
                start_r = i
                start_c = j
            elif maps[i][j] == 'E':
                end_r = i
                end_c = j
            elif maps[i][j] == 'L':
                l_r = i
                l_c = j

    #visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    visited = []

    def bfs(a, b, time):
        dq = deque([])
        dq.append((a, b))
        nonlocal visited
        visited = [[0] * len(maps[0]) for _ in range(len(maps))] # 실수 : bfs 2번 실행되므로 초기화 필요
        visited[a][b] = time

        while dq:
            r, c = dq.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < len(maps) and 0 <= nc < len(maps[0]) and maps[nr][nc] != 'X' and visited[nr][nc] == 0:
                    dq.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1

    bfs(start_r, start_c, 0) # S-> L
    if visited[l_r][l_c] == 0 :
        return -1 #레버 거치지 못했을 경우
    bfs(l_r, l_c, visited[l_r][l_c]) # S-> E
    if visited[end_r][end_c] == 0 :
        return -1 #도착지점에 도달하지 못했을 경우
    answer = visited[end_r][end_c]

    # 레버 못만났거나 start 처음부터 막혔을 경우 -1 반환
    return answer

# 이때 아직 레버를 당기지 않았더라도 출구가 있는 칸을 지나갈 수 있습니다.
# S에서 L로 갈때 E를 지날 수 있음

maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"] # 16
maps = ["SEOOO", "OXXXO", "OXXXO", "OXXXO", "LOOOO"]
#maps = ["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"] # -1
print(solution(maps))

# ** 주의 (55m)
# [ 풀이 ]
# 1차 풀이 : 합계: 30.4 / 100.0
# 2차 풀이 : 성공
# > S -> L 이후 L-> E 전에 visited 초기화해주는 것으로 해결
# > visited nonlocal로 사용해서 scope 밖에서 reference 에러 뜨는 것도 해결
# [ 문법 ]
# visited 배열 생성 시 : [[0] * len(maps[0]) for _ in range(len(maps))]
# > 0 * r 아니고 [0] * r

# + 할일
# 다른 코드 이해 안하고 넘어감