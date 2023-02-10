# *** 미해결 ***
# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/64062
# 이해 못한 솔루션 : https://developer-ellen.tistory.com/27
# 이해할 수 있는 솔루션 : https://esoongan.tistory.com/150

# 틀린 풀이
from bisect import bisect_left, bisect_right

def count(array) : # 연속된 0의 구간 중 가장 많이 반복된 구간의 0 개수를 리턴
    result = -1
    start = bisect_left(array, 0)
    cnt = 0

    '''잘못된 로직
    for i in range(start, len(array)-1) :
        if array[i] == 0 :
            cnt += 1
            if array[i+1] != 0 :
                result = max(result, cnt)
                cnt = 0'''

    if array[start] == 0 :
        cnt = 1
    else :
        cnt = 0
    for i in range(start+1, len(array)) :
        if array[i] == 0 :
            if array[i-1] == 0 :
                cnt += 1
            else :
                result = max(result, cnt)
                cnt = 1
        if i == len(array)-1 : #마지막 원소의 cnt 까지 업데이트 해주어야 함
            result = max(result, cnt)
    return result

def wrong_solution(stones, k):
    answer = 0
    stones_2 = [0 for i in range(len(stones))]
    # mid는 건널 수 있는 최대 인원을 의미
    start = 1
    end = max(stones)

    while start <= end:
        mid = (start + end) // 2
        for i in range(len(stones)) :
            if stones[i] - mid > 0 :
                stones_2[i] = 1
            else :
                stones_2[i] = 0
        cnt = count(stones_2)
        # print(stones_2, cnt, mid)
        if cnt <= k-1 :
            # ㄴ1차 오판 : k-1를 기준으로 놓았었음
            # n번째 사람이 건너고 나서 연속된 0이 k개 만들어지고 그 다음 사람은 건너지 못하게 되는 흐름이므로 기준은 k로 두어야 함
            # 요약하면, 사람이 건넌 다음에 징검다리 횟수가 차감된다는 점을 고려했어야 함
            # ㄴ2차 오판: k-1을 기준으로 두어야하는 것이 맞음
            # 순차적으로 건너갔을 때, 연속된 0이 k개 만들어진 직후부터 건너면 안되기 때문
            # 기준을 k로 두면 해당 타이밍을 정확하게 캐치하지 못함
            # 예를 들어, k=2 이고, [3,3,5,5,5] 일때,
            # 3명이 건넜다고 가정하거나 4명이 건넜다고 가정할 때 모두 [0, 0, 1, 1, 1] 배열이 만들어짐 (위의 로직에 따르면)
            # k-1일 때에서 가장 큰 mid 값을 구하고 거기에서 +1(=>마지막으로 건널 수 있는 한 사람)을 해야 정확함
            start = mid + 1
            answer = mid
        else:
            end = mid - 1
    answer += 1
    return answer

# stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
#stones = [100, 500, 100, 200]
#k = 2
#print(wrong_solution(stones, k))
#test = [0, 1, 0, 0]
#print(count(test))

# *** 주의점
# [ 풀이 ]
# 이분 탐색 접근 : "최댓값"을 구하는 문제라면 이분 탐색 생각
# 이분 탐색 시, answer 저장하는 시점이 항상 헷갈림
# bisect 활용해서 연속된 0의 시작과 끝을 구하는 방식으로 접근
#   -> 마이너스가 나올 수 있으므로 틀린 접근
# 연속된 0 개수 세는 파트에서 로직 구성
# <자가 풀이 최종 결과>
# 정확성 테스트 : 테스트 25개 중 테스트 1 제외 성공
# 효율성 테스트 : 모두 시간 초과

# 정답 풀이
def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)

    while left <= right:
        count = 0
        mid = (left + right) // 2
        for s in stones:
            if s - mid <= 0:
                count += 1
            else:
                count = 0

        if count == k:
            break
        if count < k:
            left = mid + 1
        else:
            right = mid - 1
            answer = mid
    return answer+1

# *** 미해결 ***
# 건넌 직후 count의 값은 해당 인원이 징검다리를 건널 수 있는지에 대한 기준이 될 수 없다는 것
# Q. 왜 answer = mid 기록하는 코드가 count >= k 스코프에 가있는지
# count < k 가 정답인 최댓값을 찾아나가는 파트인데
# count >= k 에서 answer를 기록한 시점을
# "마지막 사람이 징검다리를 건넌 후 더이상 건널 수 없는 징검다리의 상태가 되었을 때" 로 이해하면 됨
# k = 3 , 현상태가 [0, 0, 1, 1, 0, 0] 일때 마지막 사람이 건너가고 나면 [0, 0, 0, 0, 0, 0] 으로 count는 6이 됨
# 여기서 드는 의문은, else 스코프에 걸릴 때,
# 해당 시점 mid 인원이 징검다리를 건너지 못하는 상황이 발생한 것을 끝으로 while문을 마친다면 answer에 오답이 저장된다는 것
#   > 이 반례가 없을 것이라는 걸 증명하지 못해서 미해결..
# 이후 더 작은 범위인 왼쪽을 탐색하면서 mid 값은 줄어듦 (정답은 최댓값을 구해야 함) <- 이 지점에서도 흐름이 부자연스럽다고 느낌
# 대략적으로 이해해보자면, else 스코프는 mid 값을 감소시키는 영역, count==k에서 가장 작은 mid 값을 찾는다
# "마지막 사람이 징검다리를 건넌 후 더이상 건널 수 없는 징검다리의 상태가 되었을 때" 를 찾아야하므로
# k-1을 기준으로 비교할 땐 count == k-1에서 가장 큰 mid 값, k를 기준으로 비교할 땐 count == k에서 가장 작은 mid 값을 찾아야 함
'''
        if count < k:
            left = mid + 1
        else:
            right = mid - 1
            answer = mid
    return answer
'''
# 아래 코드로 바꾸면 이해가 됨
#  if count < k )
#  탐색 범위 오른쪽으로 넓혀가면서 count가 0~k-1인 경우에 해당하는 인원 중 최대 인원을 정답으로 저장
#  위의 인원에서 한 명만 더 가면 더이상 건널 수 없는 징검다리의 상태가 완성됨
#       > 두 명 이상이 더 갈 수도 있는 상태이진 않을까 ?
#           > No. 위의 if 문에 걸린다면 mid 값은 계속 커지므로 최대 mid 값을 찾아내고 while문을 탈출하게 됨
'''
        if count < k:
            left = mid + 1
            answer = mid

        else:
            right = mid - 1
    return answer+1
'''

stones = [2,4,3,3,2,1,4,2,5,1]
k = 3
print(solution(stones, k))