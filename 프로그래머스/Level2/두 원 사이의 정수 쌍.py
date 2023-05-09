# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181187#
def solution(r1, r2):
    answer = 0
    minY, maxY = r1, r2  # 최소, 최대로 가질 수 있는 y좌표
    # 1사분면에 대해서만 좌표값을 구하고 대칭이므로 *4한다.
    for x in range(0, r2):
        while r2 ** 2 < maxY ** 2 + x ** 2:
            maxY -= 1
        # minY 양수값을 유지
        while minY - 1 and r1 ** 2 <= (minY - 1) ** 2 + x ** 2:
            minY -= 1
        print("%d" maxY, minY)
        answer += (maxY - minY) + 1

    return answer * 4


def my_solution(r1, r2):
    answer = 0
    answer_arr = []
    # for : -m~m
    # for : -n~n
    # if ((x+2)**2-2*x*y)**0.5 가 범위 내에 있다면
    # answer +1
    start1, end1 = r2 * (-1), r2
    start2, end2 = r1 * (-1), r1
    #print(start1, end1, start2, end2)
    for x in range(1, end1+1):
        for y in range(1, end1+1): # 실수 : 범위 설정
            value = (x**2 + y**2) ** 0.5
            #print(x, y, value)
            if r1  <= value <= r2 : # 실수 : 제곱근 일관되게 적용
                answer += 1
                #answer_arr.append((x,y))

    answer += 8 #각 원 동/서/남/북 꼭짓점
    #print(answer_arr)
    return answer

r1 = 2
r2 = 3
print(r1 ** 2,r2 ** 2 )
print(solution(r1, r2))

# *** 주의
# [ 풀이 ]
# 시간 초과 풀이
# 이중 for문 해소해야
# > 4분면 점의 개수가 같다는 점을 활용
# > 1사분면 점의 개수만 구하고 * 4

# [ 문법 ]
# from math import floor,ceil,sqrt
# 파이썬에서의 삼항연산자
# > [True일 때] if a > 5 else [False일 때]