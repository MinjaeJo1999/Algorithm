# 링크 : https://www.acmicpc.net/problem/3079
import sys
input = sys.stdin.readline
n, m = map(int, input().split()) # 심사 장소 , 사람 수
array = []
for i in range(n) :
    array.append(int(input()))

# start : 1명의 최소 심사시간 . end: 전체인원의 최대 시간
start = min(array)
end = max(array)*m

# 시간이 기준 (mid)
# 특정 시간 동안에 전체 인원 심사 받을 수 있다면, 더 짧은 시간 탐색 (end = mid-1)
# 특정 시간이 부족하다면, 더 긴 시간 탐색 (start = mid+1)
result = 0
while start <= end : # '=' 조건 반드시 들어가야
    mid = (start + end) // 2 #특정 시간대
    total = 0
    for i in range(n) :
         total += (mid // array[i])
         if total >= m :
             break
    if total >= m :
        end = mid-1
        result = mid
    if total < m :
        start = mid+1

print(result)

# *** 주의
# [ 풀이 ]
# 처음에 풀이 시간 초과 나는 방법으로 생각함
#   > 사람 숫자를 인덱스로, 입국 심사 장소 중 가장 시간이 오래 걸리는 것을 배열에 넣어서 그중에서 가장 작은 수를 찾는 방식
# [ 문법 ]
# 이 문제는 mid 값이 곧 정답이므로 mid 값의 정확도가 중요
# mid = (start + end) / 2 로 나누기 연산자 사용하면 소수점까지 결과 나옴
# mid = (start + end) // 2 로 몫 연산자 사용했을 때 올바른 결과값에서 +1 된 값이 나옴 ..
# 시간 초과 ( 범위 크면 sys 모듈 사용 )
#   > import sys , sys.stdin.readline