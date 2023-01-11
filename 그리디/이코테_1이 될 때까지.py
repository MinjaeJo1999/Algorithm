# 링크: https://www.youtube.com/watch?v=2zjoKjt97vQ&feature=emb_rel_pause

n = int(input())
k = int(input())
count = 0

while n != 1:
    if n % k != 0:  # k가 n의 약수가 아니라면
        n -= 1
        count += 1
    else:
        n /= k
        count += 1

print(count)


# 더 나은 버전
def solution(n, k):
    n, k = map(int, input().split())
    result = 0

    while True:
        target = (n // k) * k
        result += (n - target)
        n = target
        if n < k:
            break
        result += 1
        n //= k

    result += (n - 1)
    print(result)

# **주의
# map 함수의 활용 : n, k = map(int, input().split())
# 시간복잡도 줄이는 방법 고민해보기