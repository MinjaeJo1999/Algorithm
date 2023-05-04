# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/155651

# 솔루션 출처 : https://moneygear.tistory.com/7/
from heapq import heappop, heappush

def solution(book_time):
    rooms = []
    book_time.sort(key = lambda _:_[0])
    for book in book_time :
        check_in = num(book[0])
        check_out = num(book[1]) + 10
        if len(rooms) != 0 and rooms[0] <= check_in :
            heappop(rooms)
        heappush(rooms,check_out)
    return len(rooms)

def num(HHMM) :
    return 60*int(HHMM[:2]) + int(HHMM[3:])

# [ 풀이 ]
# 정렬은 시작 시간 기준
# 객실 추가 기준은 끝나는 시간 기준
# 직관적인 이해 : 시작 시간, 끝나는 시간 어떤 걸 기준으로 두어야할지 헷갈렸음
# > 시작 시간 빠른 순으로 객실에 추가하되, 끝나는 시간 기준으로 객실 비어있는지 확인하면 됨
# > 힙을 사용하지 않았을 경우 (내 잘못된 풀이) 에서 객실마다 끝나는 시간에 대한 정보 추가하고
#   새로운 time마다 들어갈 수 있는 객실 있는지 체크하고 없으면 객실 추가하는 방식
# > 가장 빨리 비워진 객실을 찾으면 새로운 객실 필요한지 아닌지 바로 알 수 있음
# > 복습 많이 하면 좋을 문제

# [ 문법 ]
# heapq의 사용 (기본이 최소힙)
# heappop, heappush


'''
def my_solution(book_time):
    # 퇴실시간 기준 10분간 청소
    # [대실 시작 시간]
    # 회의실 문제랑 비슷
    # 양적 시간으로 수정
    time_list = []
    for time in book_time:
        start = int(time[0][0:2]) * 60 + int(time[0][3:])
        end = int(time[1][0:2]) * 60 + int(time[1][3:]) + 10  # 10분 청소시간
        time_list.append((start, end))
    time_list.sort(key=lambda x: (x[1], x[0]))

    answer = 1
    end_time = []
    end_time.append(time_list[0][1])
    for i in range(1, len(time_list)) :
        flag = False
        for j in range(len(end_time)) :
            if time_list[i][0] >= end_time[j] : #실수방지 : 부등호에 = 포함해야
                flag = True
        if not flag :
            answer +=1
            end_time.append(time_list[i][1])

    return answer
'''

'''
def my_solution(book_time):
    # 퇴실시간 기준 10분간 청소
    # [대실 시작 시간]
    # 회의실 문제랑 비슷
    # 양적 시간으로 수정
    time_list = []
    for time in book_time :
        start = int(time[0][0:2] ) *60 + int(time[0][3:])
        end = int(time[1][0:2] ) *60 + int(time[1][3:] ) +10 # 10분 청소시간
        time_list.append([start, end])
    time_list.sort(key = lambda x : (x[0] ,-x[1]))

    answer = 0
    room_list = []
    room_list.append(time_list[0])
    # 10 ~ 15
    # 9~ 12 / 11~12 / 14~16
    for i in range(1, len(time_list)) :
        flag = False
        for j in range(len(room_list)) :
            if (time_list[i][0] >= room_list[j][0] and time_list[i][1] <= room_list[j][1]) or \
                    (time_list[i][0] <= room_list[j][0] and time_list[i][1] <= room_list[j][1]) or (
                    time_list[i][0] < room_list[j][1] and time_list[i][1] > room_list[j][1]):
                continue
            else:
                flag = True
                room_list[j][1] = max(room_list[j][1], time_list[j][1])

        if not flag: room_list.append(time_list[i])

    answer = len(room_list)
    print(time_list)
    print(room_list)

    return answer
'''

# *** 주의
# [ 풀이 ]
# 두번의 시도 모두 15.8점
# 첫번째) 시작 시간 기준
# 두번째) 끝나는 시간 기준