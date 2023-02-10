# 링크 : https://www.acmicpc.net/problem/2343
import sys
input = sys.stdin.readline
n, m = map(int, input().split()) #강의의 수, 블루레이의 수
array = list(map(int, input().split())) #동영상 재생시간

result = 0
# start, end , mid => 블루레이 녹화 시간을 의미
start = max(array) # 주의 : min이 아니라 max
end = sum(array) # 범위 설정 더 작게 해도 될 것 같은데 .. 맞나? -> 블루레이가 1개인 경우도 있으니까..
while start <= end :
    mid = (start + end) // 2
    total = 0
    cnt = 1
    for i in range(n) :
        if total+array[i] <= mid :
            total += array[i]
        else :
            total = array[i]
            cnt += 1 # 시간 초과 시 여기서 조건 브레이크
    if cnt <= m :
        end = mid - 1
        result = mid
    if cnt > m :
        start = mid +1

print(result)

# 주의
# [ 풀이 ]
# 틀렸습니다!
#   > start 값 설정 잘못함
#   > start = min(array)은 더 큰 나머지 강의 동영상들을 어떤 블루레이에도 넣을 수 없게 되므로 틀린 최솟값
# cnt 카운트하는 타이밍
#   > 새로운 블루레이 꺼내면서 +1 해주므로 첫 시작을 1로 설정해야