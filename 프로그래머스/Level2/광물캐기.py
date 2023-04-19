# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/172927
# 출처 : https://evga7.tistory.com/130

a = [[1, 1, 1], [5, 1, 1], [25, 5, 1]] #묘기
res = 987654321
m = dict()
m["diamond"] = 0
m["iron"] = 1
m["stone"] = 2

# DFS 함수 구현
def go(idx, d, ir, s, minerals, p):
    # 종료 조건
    # 모든 광물을 캤거나 남은 도구가 없을때
    if idx >= len(minerals) or (not d and not ir and not s):
        global res
        # 현재까지 구한 값과 최솟값을 비교하여 갱신
        res = min(res, p)
        return

    dp = 0
    ip = 0
    sp = 0
    # 다음 5개의 광물에 대하여 더해준다.
    for i in range(idx, min(idx + 5, len(minerals))): # 묘기
        dp += a[0][m[minerals[i]]] #1-1. 캘 수 있는지도 모르면서 d,i,s 별로 덧셈을 하는지 이해가 안되었지만
        ip += a[1][m[minerals[i]]] #묘기 (리스트 구조 백분 활용)
        sp += a[2][m[minerals[i]]]

    # 다이아몬드를 채취하는 경우
    if d: #1-2. dp를 계산했어도, 다이아몬도 곡괭이가 없으면 해당 dp 계산은 무시되는 로직
        go(idx + 5, d - 1, ir, s, minerals, p + dp)

    # 철을 채취하는 경우
    if ir:
        go(idx + 5, d, ir - 1, s, minerals, p + ip)

    # 돌을 채취하는 경우
    if sp:
        go(idx + 5, d, ir, s - 1, minerals, p + sp)

    #트리로 그려보면
    #(시작) -> 다이아몬드 곡괭이 ->
    #                          다이아몬드 곡괭이
    #                          철 곡괭이
    #                          구리 곡괭이
    #      -> 철 곡괭이       ->
    #                          다이아몬드 곡괭이
    #                          철 곡괭이
    #                          구리 곡괭이
    #      -> 구리 곡괭이      ->
    #                          다이아몬드 곡괭이
    #                          철 곡괭이
    #                          구리 곡괭이

# 문제 해결 함수 구현
def solution(picks, minerals):
    global res
    # DFS 시작
    go(0, picks[0], picks[1], picks[2], minerals, 0)
    return res


#내 풀이
import math
def my_solution(picks, minerals):
    answer = 0
    sum_list = []
    #cnt = sum(picks)
    #length = math.ceil(len(minerals)/5) # 2-1. 모듈 끌어오기보단
    #if cnt < length :
    #   minerals = minerals[:cnt*5]
    if sum(picks)*5 < len(minerals) : #2-2. 다른 방법 가까이에 있음 / (곡괭이가 광물을 다 캐지 못할 경우)
        minerals = minerals[:sum(picks) * 5]
    for i in range(0, len(minerals), 5):
        dia, iron, stone = 0, 0, 0
        if i + 5 <= len(minerals):
            end = i + 5
        else :
            end = len(minerals)

        for i in range(i, end):
                if minerals[i] == 'diamond' :
                    dia += 1
                if minerals[i] == 'iron' :
                    iron += 1
                if minerals[i] == 'stone' :
                    stone += 1
        sum_list.append((dia, iron, stone))
    sum_list.sort(key = lambda x : (-x[0],-x[1],-x[2]))
    for list in sum_list:
        force = 0
        if picks[0] > 0 :
            picks[0] -= 1
            force = sum(list)
        elif picks[1] > 0 :
            picks[1] -= 1
            force = list[0]*5 + list[1] + list[2]
        elif picks[2] > 0 : #실수 방지 : else로 빼면 안됨 , 반드시 picks[2] 의 값 체크해주어야 함
            picks[2] -= 1
            force = list[0]*25 + list[1]*5 + list[2]

        answer += force
        '''start = sum_list[i]*5 #실수 방지 : 인덱스 관리
        if start + 5 <= len(minerals):
            end = start + 5
        else:
            end = len(minerals)
        force = 0
        if picks[0] > 0:
            picks[0] -= 1
            for j in range(start, end):
                force += 1
        elif picks[1] > 0:
            picks[1] -= 1
            for j in range(start, end):
                if minerals[j] == 'diamond':
                    force += 5
                else:
                    force += 1
        elif picks[2] > 0:
            picks[2] -= 1
            for j in range(start, end):
                if minerals[j] == 'diamond':
                    force += 25
                elif minerals[j] == 'iron':
                    force += 5
                else:
                    force += 1
        answer += force'''

    return answer

#picks =[1, 3, 2]
#minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
picks = [0, 1, 1]
minerals = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
print(solution(picks,minerals))

# ***주의 (2.75)
# [ 풀이 ]
# 구현으로 접근
# 첫번째 풀이 오류 : 기준을 잘못 정함, 다이아/철/구리 값에 차등 줘서 더한 후 가장 작은 값일수록 단단한 곡괭이 필요한 것으로 가정
#   > 틀린 이유 : 광물 5개 있는 구간과 광물 5개 미만 있는 구간을 해당 기준으로 비교하면 5개 미만 있는 그룹이 값 작을 수밖에 없음
#       > (다이아 개수, 철 개수, 구리 개수) 내림차순 정렬해야 함
# 내 풀이 37점
# > 정렬 문제로 접근하는 건 좋으나 오류 잡아내지 못함
#   > 함수화해서 가독성 높이기도 방법
# 8번 테스트 케이스 오류
# > 곡괭이가 광물을 다 캐지 못할 경우 예외 처리
#   > 2번 테스트케이스가 그러한 경우인데 8번 케이스 고려 못한 로직도 같은 답이 나오도록 되어있음
# 기타 고려해야 하지만, 이 문제에선 신경쓰지 않아도 문제 없는 요소 :
# 최악의 기준을 다이아 개수, 철 개수, 구리 개수가 제일 많은 순으로 잡고 정렬함
# 근거도 생각해야
# > 다섯 구간까지만 나뉘어서 가능한 기준
#   > (다이아, 철, 구리)가 (0, 5, 0) 인 케이스와 (1, 4, 0) 인 케이스에서도
#   > 5*25 = 125 / 50+25*4 = 150 로 다이아 개수가 더 많은 케이스가 최악의 경우가 됨

# [ 문법 ]
# if list[0] 일 때, 리스트 값이 0이 아니라 음의 정수여도 True 값 나옴

# <솔루션 풀이>
# 완전탐색 (DFS 활용)으로 접근