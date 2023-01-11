# 링크: https://www.acmicpc.net/problem/16206
# 솔루션 참고 링크:
# https://art-coding3.tistory.com/51
# https://devlibrary00108.tistory.com/256

# 오답 (밑에 정답)
import sys

# n: 케이크 개수 , m: 자를 수 있는 횟수
n, m = map(int, input().split())
cake = list(map(int, input().split()))

cnt = m # 자르는 횟수
cakes = 0 # 케이크 개수

# k개 초과할 때 예외 처리
for i in range(n) :
    temp = cake[i]//10
    if cake[i] % 10 == 0 and cnt-temp+1 >=0 : # 10의 배수여서 남김없이 자를 수 있는 케이크
        cnt = cnt - temp + 1
        cakes += temp
        continue
    elif cake[i] % 10 != 0 and cnt-temp >=0 : # 10의 배수가 아니어서 잘랐을 때 잉여가 남는 케이크
        cnt = cnt - temp
        cakes = cakes + temp
        continue
    elif cake[i] > 10  and cnt-temp < 0 : # 제한된 횟수에 걸려서 자르다가 말아야 하는 케이크
        cakes = cakes + cnt #자른 횟수 만큼만 사용할 수 있는 케이크가 생김 (ex. 길이 13이라면 10 / 3 )
        cnt = 0
        break # break 해줘야 나머지 케이크들 pass 가능
    else :
        break

print(cakes)

# 정답 풀이
def sol() :
    n, m = map(int, sys.stdin.readline().split())
    cakes = list(map(int, sys.stdin.readline().split()))
    cakes.sort()
    cakes.sort(key = lambda x: x%10)
    cake_cnt = 0

    for cake in cakes :
        cnt = cake // 10
        if not cake%10 : #if: 10의 배수일 경우 30 > 10 / 10 / 10 > 2번(몫-1) 자르면 3개(몫)만큼 나옴
            if cnt-1 < m : # if: 자른 횟수 초과 검토 / cnt-1 => 몫-1
                cake_cnt += cnt # 만들어진 케이크 개수
                m -= cnt-1 # 사용한 횟수 업데이트 / cnt-1 => 몫-1
            else : # 자를 수 있는 횟수(몫-1)가 남은 횟수보다 크거나 같다면
                cake_cnt += m # 자른 횟수만큼 길이 10 케이크가 나옴 (ex. cake 30 m 1 이라면 > 10 / 20 이 되므로)
                m -= m # 남은 횟수 소진
        else : # 10의 배수가 아닐 경우
            if cnt <= m : # cnt => 몫만큼 잘라야 길이 10 케이크를 모두 얻음 (ex. cake 32 m 3 > 10 / 10 / 10 / 2)
                cake_cnt += cnt
                m -= cnt
            else :
                cake_cnt += m
                m -= m
    print(cake_cnt)




# ***주의
# 내 코드 <틀렸습니다> 로 나오는데 그러한 코너케이스 찾지 못함
#  > 사유1: 롤케이크 크기 작은 것부터 잘라야 최대값이 나온다는 점 파악하지 못함
#  > 사유2: 10의 배수인 것부터 잘라야 최대값이 나온다는 점 파악하지 못함
# [a b c d e] 형식의 입력값 받아오는 법 : list(map(int, input().split()))
# break 처리해야 하는 경우 고려
# 시간 초과 방지 sys 모듈 사용 : sys.stdin.readline().split()

