# 링크  : https://www.acmicpc.net/problem/11399
import sys
input = sys.stdin.readline

n = int(input())
wait = list(map(int, input().split()))

wait.sort() # 오름차순 정렬
sum = 0
for i in range(n) :
    sum += wait[i]*(n-i)
print(sum)

# ** 주의
# [ 풀이 ]
# <수학적 귀납법 적용>
# S1 = wait[0]
# S2 = wait[0] + wait[1]
# ...
# Sn = wait[0] + wait[1] + ... + wait[n-1]
# answer = S1 + S2 + ...  + Sn
# <다른 풀이>
# answer += sum(wait[0:x])