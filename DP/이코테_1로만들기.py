# 문제 : 정수 X가 주어졌을 때, 정수 X에 사용할 수 있는 연산은 아래의 4가지
# 1. X가 5로 나누어 떨어지면, 5로 나눈다.
# 2. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 3. X가 2로 나누어 떨어지면, 2로 나눈다.
# 4. X에서 1을 뺀다.
# ex( 26 -> 25 -> 5-> 1 )

x = int(input())
dp = [0]*(x+1)
dp[0] = 0 #초기 설정

for i in range(2, x+1) : # 인덱스 1의 경우 자기 자신이 1이므로 연산을 수행할 필요가 없음
    dp[i] = dp[i-1] + 1
    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i//2]+1)
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 5 == 0 :
        dp[i] = min(dp[i], dp[i//5] +1)
print(dp[x])

dp = [0]*(x+1)
# 거꾸로 탐색하는 로직
for i in range(x, 0, -1) : # 26
    if dp[i-1] == 0 : # 처음 방문했을 때
        dp[i-1] = dp[i] + 1 # 25 = 1
    else :
        dp[i-1] = min(dp[i]+1, dp[i-1])
    if i % 2 == 0 :
        if dp[i //2] == 0 :  # 처음 방문했을 때
            dp[i // 2] = dp[i] + 1
        else :
            dp[i // 2] = min(dp[i//2], dp[i]+1)
    if i % 3 == 0 :
        if dp[i //3 ] == 0:  # 처음 방문했을 때
            dp[i // 3] = dp[i] + 1
        else:
            dp[i // 3] = min(dp[i // 3], dp[i] + 1)
    if i % 5 == 0 :
        if dp[i // 5] == 0:  # 처음 방문했을 때
            dp[i // 5] = dp[i] + 1
        else:
            dp[i // 5] = min(dp[i // 5], dp[i] + 1)
print(dp[1])





# *** 주의
# [ 풀이 ]
# 예시 기준 : 26 -> 25 -> 5-> 1
# 그리디 접근은 적절하지 않음
#  > 가장 큰 수로 나누는 것 말고, 다른 연산을 적절히 조합했을 때 최적의 해가 나올 수 있기 때문
# 의문 1. 내림차순으로 dp 리스트 탐색하는 것이 흐름 상 맞지 않나?
#   > 1 - > - > - > - > 26 / 26 - > - > - > - > 1 으로 탐색할 때 모두
#     ㄴ dp[i] 값의 의미 : i 값으로 도달할 때까지의 최적의 단계
#   > 오름차순 탐색 시엔 앞의 최적해를 활용해서 현재의 최적해를 찾는다면
#     ㄴ (-1) 연산이 있으므로 바로 이전 값의 최적해를 현재 최적해에 대입 후, 나누기 2 / 3 / 5 를 통해 현재 값이 되었을 경우와 비교하여 최적해를 구하면 됨
#   > 내림차순 탐색 시엔 목표값(1)으로 수렴하는 감소 단계를 밟으면서
#     ㄴ 특정 지점이 한번도 탐색되지 않은 경우와 지나간 이력이 있는 경우를 구분하여 값을 업데이트해주어야 함
# 요약하면,
# 1 -> 26 으로 가는 단계나 26 -> 1 로 가는 단계나 같은 과정이 나온다는 점만 안다면 의문이 해소됨