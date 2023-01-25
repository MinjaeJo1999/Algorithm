# 링크 : https://www.acmicpc.net/problem/4963
import sys
sys.setrecursionlimit(10**7)

array = []
visited = [] #필요없음
cnt = 0

# 실수 많이 나옴
while True :
    w, h = map(int, input().split())
    if w==0 and h==0 : # 탈출 조건문
        break;
    array.append([]) # 탈출 조건문 이후에 작성
    for j in range(h): #행 개수만큼 반복
        array[cnt].append(list(map(int, input().split())))
    visited.append([[0] * w]*h)
    cnt += 1

# 상하좌우, 대각선
dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, -1, -1, 1 ]

def dfs(h,w,m,r,c) :
    if r<0 or r>=h or c<0 or c>=w : # 실수 : h,w 의 경우 같아도 안된다는 점
        return False
    if array[m][r][c] == 1 : # 인덱스 에러 주의
        array[m][r][c] = 2
        for a in range(8): # 실수
            dfs(h, w, m, r+dy[a], c+dx[a])
        return True
    return False


for i in range(len(array)) : #지도 하나를 탐색한 후 개수 프린트해야
    result = 0
    for j in range(len(array[i])) : #행
        for k in range(len(array[i][j])) : #열
            h = len(array[i])
            w = len(array[i][j])
            if(dfs(h,w,i,j,k)) : #인덱스 에러 주의
                result += 1
    print(result)

exit(0)

#지도 개수마다
#지도별로 섬 개수 탐색
#   > 모든 지점 탐색
#   > 1 만나는 지점에서 dfs, 이어져 있는 지점 모두 2로 변경
#탐색 끝나면 섬 개수 print

# **주의
# [ 문법 ]
# 사용하는 함수와 이름이 같은 변수명 사용하면 에러 남 (ex. map.append(list(map(int, input().split())))
# 행, 열에 매칭되는 x, y , 너비 w, 높이 h 헷갈리지 않기
# 다차원 배열의 경우 인덱스 사용할 때 실수할 확률 높으니 주의하기
#  > 알맞은 위치의 인덱스 사용
#  > 인덱스 접근 시 range 에러 고려하면서 코드 작성
# [ 풀이 ]
# 이코테 _ 음료수 얼려먹기 풀이 참고 (로직 동일)
# visited가 필요없는 것 같은데
# 재귀 특성이 있는 dfs 함수에 전체를 탐색하는 for문을 두면 좌표를 전달받아 탐색을 반복하는 dfs의 특성을 잘 활용하지 못하게 됨
# > for문이 필요한 로직은 함수 외부에서 사용하는 것이 좋다.
# 위 풀이 백준에서 런타임에러 (RecursionError)
# > 재귀가 너무 깊어짐
# > 재귀 한도 늘리는 코드로 해결  import sys / sys.setrecursionlimit(10**7)
# > dfs로 접근할 경우 w와 h의 최대가 50이어서 재귀깊이가 2500까지 들어갈 수 있음 (백준 한도는 1000)
# > bfs로 풀이시 런타임에러 피할 수 있음
# 입력과 계산을 따로 하면 삼차원 배열이 만들어져서 코드가 복잡해지고 인덱스 관련 실수가 잦아짐
#   > 입력 받으면서 지도별로 섬 개수 구할 수 있음
# 더 나은 코드 : https://velog.io/@hamfan524/%EB%B0%B1%EC%A4%80-4963%EB%B2%88-Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC

'''잘못 접근했던 코드
def dfs(r,c) :
    for a in range(len(array)) : #지도의 개수
        for i in range(len(array[a])) : #행 위치
            for j in range(len(array[a][0])) :
                if array[a][i][j] == 1 and not visited[a][i][j] :
                    array[a][i][j] = 2
                    for nx, ny in dx, dy :
                        if 0<=nx<h and 0<=ny<w and array[nx][ny]==1: # nx-h(행), ny-w(열)
                            visited[a][nx][ny] = 1
                            dfs(nx, ny)
'''