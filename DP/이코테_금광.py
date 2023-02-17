# 그리디 , DFS&BFS 로 접근해야 하는 문제와 어떤 차이점 있는지 고민
# n * m 크기의 금광이 있다.
# 채굴자는 첫번째 열부터 금을 캐기 시작
# 첫번째 열의 어느 행에서든 출발할 수 있음
# 이후 m-1번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동
# 채굴자가 얻을 수 있는 금의 최대 크기를 출력

dp = []
for tc in range(int(input())) :
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    index = 0
    for i in range(n) :
        dp.append(array[index: index+m])
        index += m

    for j in range(1,m) :
        for i in range(n) :
            if i == 0 : # 첫번째 행이면 왼쪽 위가 없으므로
                left_up = 0
            else :
                left_up = dp[i-1][j-1]
            if i == n - 1 : # 마지막 행이면 왼쪽 아래가 없으므로
                left_down = 0
            else :
                left_down = dp[i+1][j-1]
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n) :
        result = max(result, dp[i][m-1])
    print(result)


# *** 주의
# 행,열 탐색 시 i , j 인덱스 순서와 반복문 순서 일치하도록 주의
