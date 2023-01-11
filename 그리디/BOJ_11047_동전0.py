# 링크: https://www.acmicpc.net/problem/11047

n , k = map(int, input().split()) # N: 동전의 종류 , K: 가치의 합
value = []
for i in range(n) :
    value.append(int(input()))
value.sort(reverse=True)

cnt = 0 # 필요한 동전 개수

for i in value :
    if i <= k : # 1000 ,30  5500
        cnt += k // i
        k %= i
        if k <= 0 :
            break


print(cnt)

# ***주의
# 입력 받아오는 방법
# 변수 어떻게 사용하고 있는지 잘 파악
# 정답에 빨리 도달했을 경우 break 항상 고려