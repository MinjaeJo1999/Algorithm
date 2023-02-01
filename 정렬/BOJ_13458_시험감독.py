# 링크 : https://www.acmicpc.net/problem/13458
import sys
input = sys.stdin.readline

n = int(input()) # 시험장의 개수
A = list(map(int, input().split())) # 응시자의 수
b, c = map(int, input().split()) # 총감독관, 부감독관

# cnt += 시험장 개수만큼 총감독관
cnt = n
for i in range(n) :
    temp = A[i] - b
    # 시험장마다 (응시자 수 - B명) // C
    if temp>0 and temp%c == 0 :
        cnt += (temp//c)   #나누어 떨어지면 +몫
    elif temp>0 :
        cnt += (temp//c + 1)   #나누어 떨어지지 않으면 +(몫+1)
print(cnt)

# ** 주의
# [ 문법 ]
# 나머지 : % , 몫 : //
# [ 풀이 ]
# if문 구조 더 나은 버전
# if temp > 0
#       if a%b==0
#       else