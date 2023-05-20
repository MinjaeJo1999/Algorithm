# 완전 탐색
from itertools import combinations
T = int(input())
for test_case in range(1,T+1) :
    n = int(input())
    # n*n -> 놓일 수 있는 위치
    # 위치 -> 행렬화  예를 들어 2*2인데 3이 나왔다면 2번째 행 첫번째임 3//2 3%2 =
    pos = [i for i in range(n*n)]
    answer = 0
    combi = list(combinations(pos, n)) #위치 조합
    for c in combi : # 나올 수 있는 모든 위치 탐색
        possible = True
        j = [[0 for _ in range(n)] for _ in range(n)]  # 행렬
        flag = True
        for i in c : # 위치 표시하면서 체크
            row = i // n
            col = i % n
            if max(j[row]) == 1 : # 열 체크
                flag = False
                break
            for a in range(n) : # 행 체크
                if j[a][col] == 1 :
                    flag = False
                    break

            # 대각선 체크
            # 왼쪽 위
            a = row +1
            b = col +1
            while -1 < a < n and -1 < a < n and -1 < b < n and -1 < b < n :
                if j[a][b] == 1 :
                    flag = False
                    break
                a += 1
                b += 1
            # 왼쪽 아래
            a = row -1
            b = col -1
            while -1 < a < n and -1 < a < n and -1 < b < n and -1 < b < n :
                if j[a][b] == 1 :
                    flag = False
                    break
                a -= 1
                b-= 1

            # 오른쪽 위
            a = row -1
            b = col +1
            while -1 < a < n and -1 < a < n and -1 < b < n and -1 < b < n :
                if j[a][b] == 1 :
                    flag = False
                    break
                a -= 1
                b += 1

            # 오른쪽 아래
            a = row +1
            b = col -1
            while -1 < a < n and -1 < a < n and -1 < b < n and -1 < b < n :
                if j[a][b] == 1 :
                    flag = False
                    break
                a += 1
                b += 1

            if flag : # 여기까지 왔으면 flag True일 수밖에 없음
                j[row][col] = 1
            else :
                possible = False # 의미 없음
                break

        if possible and flag :
            answer += 1

    print("#"+str(test_case), answer)

# *** 주의
# [ 풀이 ]
# 내풀이 : 오답
# 채점용 input 파일로 채점한 결과 fail 입니다.
# (오답 : 10개의 테스트케이스 중 5개가 맞았습니다.)

# 맞는 풀이
# 출처 : https://seongonion.tistory.com/m/103
# 시각적 이해 : https://jehwanyoo.net/2022/01/26/n-queen-%EB%AC%B8%EC%A0%9C-%EB%B0%B1%ED%8A%B8%EB%9E%98%ED%82%B9/
# 행 체크 필요 없는 이유 : N*N 체스판에 N개 퀸이므로 행 당 하나씩 있을 수밖에 없음, 그렇게 dfs 구성

n = int(input())
ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x): # x까지만 검사해도 되는 이유: x 아래는 아직 0임
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i): # 열 체크,
            return False
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return
    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):
                n_queens(x + 1)
n_queens(0)
print(ans)


# 복습 요함
# 다른 풀이도 이해하기