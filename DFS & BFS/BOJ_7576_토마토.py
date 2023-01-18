# 링크 : https://www.acmicpc.net/problem/7576
# 솔루션 참고 링크 : https://jae04099.tistory.com/entry/%EB%B0%B1%EC%A4%80-7576-%ED%86%A0%EB%A7%88%ED%86%A0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%95%B4%EC%84%A4%ED%8F%AC%ED%95%A8

from collections import deque

def wrong_answer() :
    m, n = map(int, input().split()) #열, 행

    tomato = []
    for _ in range(n) :
            tomato.append(list(map(int, input().split())))
    ''' -> 한줄로 줄이면
    tomato = [list(map(int, input().split())) for _ in range(n)] 
    '''

    days = 0
    final = [[1 for _ in range(m)] for _ in range(n)] # 목표치
    position = [] #익은 토마토 위치 저장
    empty_position = [] #토마토 없는 칸 위치 저장

    for i in range(n) :
        for j in range(m) :
            if tomato[i][j] == 1 :
                position.append((i,j))
            elif tomato[i][j] == -1 :
                empty_position.append((i,j))


    # for문 돌면서 (한 사이클이 하루)
    # -1에 고립되어 익지 못하는 토마토 있는지 확인 (-> 예외 처리 하지 않으면 while 무한 루프 돌게 됨)
    # 1인 부분 인덱스 저장
    # 저장해둔 1 위치 상하좌우 1로 변경 , 익은 토마토 위치 업데이트
    # -1일 경우 예외 처리 , -1로 인해 익지 못하는 토마토 있는지 확인 -> 있다면 break, 없다면 -1도 1로 변경 & 익은 토마토 위치 업데이트

    # 상하좌우
    dx = [0, 0, -1, 1] # 열
    dy = [-1, 1, 0, 0] # 행

    while tomato != final :
        print('while')
        for i,j in position :
            for k in range(4) :
                if i+dx[k] >= 0 and i+dx[k]<m and j+dy[k] >=0 and j+dy[k]<n :
                    moved_y = i + dy
                    moved_x = j + dx
                    if tomato[moved_y][moved_x] == 0 :
                        tomato[moved_y][moved_x] = 1
                        position.append((moved_y, moved_x))
                   # elif tomato[moved_y][moved_x] == -1 : -> 이 로직으론 빈 칸 예외에 대처하기 힘듦


        days += 1

    print(days)

    # -> 무한 루프에서 빠져나오지 못함



m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = 0

for i in range(n) :
    for j in range(m) :
        if tomato[i][j] == 1 :
            queue.append([i,j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4) :
            nx, ny = dx[i]+x, dy[i] + y
            if 0<=nx<n and 0<=ny<m and tomato[nx][ny] ==0 :
                tomato[nx][ny]  = tomato[x][y] + 1
                queue.append([nx, ny])
bfs()

for i in tomato :
    for j in i :
        if j == 0 :
            print(-1)
            exit(0)
    result = max(result, max(i))

# 처음 시작이 1이었으므로
print(result-1)

# *** 주의
# [ 풀이 ]
# dfs로 접근함
# 주변부 탐색은 bfs가 적합
# 시간의 흐름 bfs 돌면서 리스트값에 표기
# Q. bfs 단계가 어떻게 시간의 흐름과 일치하게 되는지 ?
#   > bfs 단계마다 1 위치의 상하좌우값이 바뀐다는 것 => 하루가 지났다는 의미이므로 bfs 수행 후 가장 큰 값을 찾으면
#   > 해당 값은 첫날부터 마지막날까지의 업데이트 흐름이 모두 반영된(영향을 받은) 토마토의 위치에서 나오는 값이므로 날짜의 흐름 확인 가능
# bfs의 역할 / bfs 이후 로직의 역할 구분
#   > 전자는 토마토를 익히는 과정, 후자는 칸마다 익힘 유무를 검토하면서 리스트에서 최댓값(=소요된 기한)을 찾는 과정
#   > 소요 기간 max 함수를 통해 얻음
# [ 문법 ]
# n, m, x, y, 행, 열 헷갈리지 말 것
# exit(0)의 사용


