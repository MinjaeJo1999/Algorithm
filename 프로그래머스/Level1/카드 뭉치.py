# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/159994

from collections import deque
def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    for target in goal :
        if cards1 and target == cards1[0] : # 실수 방지 : 배열에 요소 있는지 확인
            cards1.popleft()
            continue
        elif cards2 and target == cards2[0] :
            cards2.popleft()
            continue
        else :
            return 'No'
    return 'Yes'

cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
print(solution(cards1, cards2, goal))

# [ 풀이 ]
# 실수 방지 확인
# 공간적으로 비효율
# 다른 풀이 : 그냥 카드 2개 가각 인덱스 따로 관리하면 됨
