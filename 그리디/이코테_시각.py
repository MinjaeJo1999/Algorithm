n = int(input())
count = 0

# 00시 00분 00초~ N시 59분 59초
for a in range(n + 1):
    # 시 <= 5 / 분 <= 60 / 초 <=60
    if '3' in str(a):
        count += 60 * 60
        continue
    else:
        count += 15 * 60 + 45 * 15

print(count)

# 더 나은 버전
def sol():
    h = int(input())
    count = 0
    for i in range(h+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i)+str(j)+str(k):
                    count += 1
    print(count)

# **주의
# 최대 경우의 수 파악하기 > 범위가 넓지 않다면 시간복잡도 덜 고려해도 됨
# 범위 60이 아니라 59까지라는 점
