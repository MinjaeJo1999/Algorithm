# 링크: https://www.acmicpc.net/problem/1931
# 솔루션 참고 링크: https://suri78.tistory.com/26

n = int(input())
time = []

for i in range(n) :
    s, e = map(int, input().split())
    time.append((s,e))

time.sort(key=lambda x: (x[1], x[0])) # 끝나는 시간 오름차순 후 시작 시간 오름차순 정렬

end_time = time[0][1]
cnt = 1 # 미리 한타임 넣어두고 시작
for i in range(1,n) :
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]
print(cnt)

# *** 주의
# 처음부터 잘못된 아이디어로 접근
#  > 시작시간 & 회의진행시간을 엮어 기준으로 삼았음
#  > 끝나는 시간을 기준으로 할 생각을 못함
#  > 시작시간보다 끝나는 시간이 더 중요하다는 것을 생각했어야 (얼마나 오래 지속되었는지를 반영하는 첫번째 지표이므로)
# 예외케이스 고려 : 끝나는 시간 오름차순 정렬만 하면 예외 케이스 처리하지 못함
#  > 시작 시간도 오름차순으로 정렬되어야 함