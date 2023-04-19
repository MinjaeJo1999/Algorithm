#링크 : https://school.programmers.co.kr/learn/courses/30/lessons/169199

from collections import deque

# 솔루션 출처 : https://velog.io/@mimmimmu/PGS-%EB%A6%AC%EC%BD%94%EC%B3%87-%EB%A1%9C%EB%B4%87-%ED%8C%8C%EC%9D%B4%EC%8D%AC
def solution(board):
    answer = 0
    R = len(board)
    C = len(board[0])
    rx, ry = 0, 0
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'R':
                rx, ry = i, j

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs():
        q = deque()
        q.append((rx, ry))
        visited = [[0] * C for _ in range(R)]
        visited[rx][ry] = 1

        while q:
            px, py = q.popleft()
            if board[px][py] == 'G':
                return visited[px][py]
            for i in range(4):
                nx, ny = px, py
                while True:
                    nx, ny = nx + dx[i], ny + dy[i]
                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] == 'D':
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    if nx < 0 or nx >= R or ny < 0 or ny >= C:
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[px][py] + 1
                    q.append((nx, ny))
        return -1

    answer = bfs()
    if answer > 0:
        answer -= 1

    return answer



answer = float('inf')  # min()에서 갱신

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(board, r, c, move):  # 보드 정보, 위치값, move 횟수
    global answer
    if board[r][c] == 'G':
        answer = min(answer, move)
        return
    temp_r, temp_c = r, c
    for i in range(4):
        while True:  # 상,하,좌,우 중 한 방향 선택, 이동 가능할 때까지 이동
            if 0 <= r + dr[i] < len(board) and 0 <= c + dc[i] < len(board[0]):
                if board[r + dr[i]][c + dc[i]] == 'D':
                    break  # D 만난다면 이동하지 않음
                # D를 만나지도 않고, 범위를 벗어나지도 않는다면 이동
                r += dr[i]
                c += dc[i]
            else:  # 범위를 벗어난다면
                break
        if temp_r != r or temp_c != c:
            move += 1
            dfs(board, r, c, move)   # 이동 시에만 dfs
    return

from collections import deque

def my_bfs (board, r, c, move):
    dq = deque([])
    dq.append((r,c))
    visited = [[float('inf') for _ in range(len(board[0]))] for _ in range(len(board))]
    visited[r][c] = 0

    global answer
    if board[r][c] == 'G':
        answer = min(answer, move)
        return

    while dq:  # 상,하,좌,우 중 한 방향 선택, 이동 가능할 때까지 이동
            print(dq)
            row, col = dq.popleft()
            before_move = visited[row][col]
            temp_r, temp_c = row, col
            if board[row][col] == 'F' :
                return board[row][col]
            for i in range(4) : #상,하,좌,우 이동
                while True : #장애물/끝 만날 때까지 이동
                    if 0 <= row + dr[i] < len(board) and 0 <= col + dc[i] < len(board[0]):
                        if board[row + dr[i]][col + dc[i]] == 'D':
                            break  # D 만난다면 이동하지 않음
                        # D를 만나지도 않고, 범위를 벗어나지도 않는다면 이동
                        row += dr[i]
                        col += dc[i]
                    else:  # 범위를 벗어난다면
                        break
                if temp_r != row or temp_c != col: #이동에 성공했을 때만
                    dq.append((row, col))
                    visited[r][c] = min(visited[r][c], before_move+1)
                # -> BFS 로직 활용도 부족했음
                    '''
                            if not visited[nx][ny]: -> BFS 핵심, 먼저 방문했다면 해당 케이스가 현재 지점까지의 최단경로 보장
                    visited[nx][ny] = visited[px][py] + 1
                    q.append((nx, ny))
                    '''

    return -1

def my_solution(board):
    # 리코쳇 로봇
    # 격자모양 게임판
    # 시작~목표 최단거리
    # 상,하,좌,우
    global answer
    move = 0
    r = 0
    c = 0
    idx = 0

    for row in board:  # 시작 지점 찾기
        if 'R' in row:
            r = idx
            c = row.find('R')
            break
        idx += 1

    answer = bfs(board, r,c, move)
    #dfs(board, r, c, move)
    #if answer == float('inf') :
    #    return -1
    return answer

board =  ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(board)) # 7

# ***주의 (2)
# [ 풀이 ]
# DFS로 접근했으나 보드 칸 5*7에서도 recursion error
# 최대 보드 크기 100*100이므로 bfs로 접근하는 것이 좋음
# BFS 풀이 : 무한 반복
# 자주 사용하는 값 (ex. 행/열 정보)은 변수 만들어주자
