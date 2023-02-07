# 링크 : https://www.youtube.com/watch?v=94RC-DsGMLo

n, m = map(int, input().split(' '))
array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end) : # start, end 위치 바뀌면 끝
    total = 0
    mid = (start+end) // 2
    for x in array :
        if x > mid :
            total += x - mid
        if total < m :
            end = mid-1
        else :
            result = mid #최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록, while 조건 불충족으로 빠져나올때 result 기록되어 있도록
            start = mid + 1

print(result)

# *** 주의
# [ 풀이 ]
# 절단기 높이 범위가 0~10억
#   > 탐색 범위가 크면 "이진 탐색"을 떠올려보자
# 적절한 "높이"를 찾는 방법으로 이진 탐색을 채택
#   > '현재 이 높이로 자르면 조건을 만족할 수 있는가?"
#       > "예" 혹은 "아니오"로 탐색 범위 좁혀서 해결

# 그렇다면 탐색 범위 어디부터 어디로 해야할까 ?
# 가장 작은 수 ~ 가장 큰 수 ? > 이미 나와 있음
# 절단기의 높이 범위가 0~10억
