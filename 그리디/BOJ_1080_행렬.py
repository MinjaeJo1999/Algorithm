# 링크: https://www.acmicpc.net/problem/1080
# 솔루션 참고 링크: https://velog.io/@dding_ji/baekjoon-1080
from sys import stdin

global n, m
n, m = map(int, input().split())
global a, b
a = [list(map(int,list(input()))) for _ in range(n)]
b = [list(map(int,list(input()))) for _ in range(n)]
moved = [(-1,0), (1,0), (0,-1), (0,1), (1,-1), (1,1), (-1,1), (1,1)]
global cnt
cnt = 0

#연산
def change(x,y) : # 0 < x < n / 0 < y < n
    global cnt
    cnt += 1
    a[x][y] = a[x][y] ^ 1
    for i in range(8) :
        if n>x+moved[i][0]>=0 and m>y+moved[i][1]>=0 : # 인덱스 에러 : 상한&하한 모두 지정해주어야
            moved_x = x+moved[i][0] # 연산자 실수 (+여야 하는데 -)
            moved_y = y+moved[i][1]
            a[moved_x][moved_y] = a[moved_x][moved_y] ^ 1

def check() : # A == B 로 끝나는 코드
    isSame = True
    for i in range(n) :
        for j in range(m) :
            if a[i][j] != b[i][j] :
                isSame = False
    return isSame

test = 0

for i in range(n) :
    for j in range(m) :
        test += 1
        if a[i][j] != b[i][j] :
            change(i,j) # 인덱스 에러
            result = check()
            if result : # 행렬a와 행렬b가 똑같아졌다면
                break

if not result :
    cnt = -1

# 정답
def flip(i, j):
    for x in range(i, i+3) :
        for y in range(j, j+3) :
            a[x][y] = 1 - a[x][y]
def sol() :
    n, m = map(int, stdin.readline().split())
    a = [list(map(int, stdin.readline().rstrip())) for j in range(N)]
    b = [list(map(int, stdin.readline().rstrip())) for j in range(N)]
    cnt = 0

    for i in range(n-2) : #줄바꿈 가능 횟수
        for j in range(m-2) :
            if a[i][j] != b[i][j] :
                flip(i, j)
                cnt += 1
            if a == b :
                break
            if a == b :
                break
    if a != b :
        print(-1)
    else :
        print(cnt)


# *** 주의
# [ 문법 ]
# 0000 (줄바꿈) 1111 (줄바꿈) [ [0, 0, 0, 0] , [1, 1, 1, 1]] 로 입력 받는 코드
# 입력 시 tip > 리스트 안 for문
# 함수 내에서 전역변수 사용
# 비트 연산자 ( &, | , ^, ~)
# 논리 연산자 not, 비트 연산자 ~ 구분
# 비트 연산자 ~ 관련 1의 보수, 2의 보수 표현법 기억해두기
# -------------------------------------------
# [ 알고리즘 ]
# 문제 이해 잘못함 (어떤 3 * 3크기의 부분 행렬에 있는 모든 원소) 이 부분
# > 테스트 케이스를 통해서 올바르게 파악했어야 하는 부분
# > 3 * 3 크기가 되지 않는 부분에서도 연산을 수행했음 (범위에 든 3*3 공간은 연산해야한다고 잘못 파악해서)
# 최소를 보장하는 조건 제대로 파악하지 못했음
# > a / b 다른 지점에서만 연산 수행함