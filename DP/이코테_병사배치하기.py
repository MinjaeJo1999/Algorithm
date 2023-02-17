# 그리디 , DFS&BFS 로 접근해야 하는 문제와 어떤 차이점 있는지 고민
# LIS(Longest Increasing Subsequence) 문제와 로직 같음
# < 문제 >
# N명의 병사가 무작위로 나열되어 있다.
# 병사 배치 시 전투력 내림차순으로 배치하려 한다.
# 배치 과정에서 특정 위치에 있는 병사를 열외시키고, 남아 있는 병사의 수가 최대가 되도록 하고 싶다.
n = int(input()) # 병사의 수
array = list(map(int, input().split())) # 병사의 전투력
array.reverse() # LIS 문제로 변경
dp = [1] * n # 가장 작은 부분 수열은 자기 자신이므로 1부터 시작
for i in range(1, n) :
    for j in range(0, i) : # LIS 문제의 핵심
        if dp[i] > dp[i-1] :
            dp[i] = max(dp[i], dp[i-1])

print(n-max(dp))
