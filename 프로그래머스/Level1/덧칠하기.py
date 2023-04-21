# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/161989

from collections import deque

# 솔루션 링크 : https://prod.velog.io/@ggb05224/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8D%A7%EC%B9%A0%ED%95%98%EA%B8%B0-python
def solution(n, m, section):
    answer = 0  # 페인트를 칠해야하는 최소 횟수
    section = deque(section)  # 앞에서부터 차례로 칠하기 위해 데큐 선언

    # 페인트 칠을 전부다 할 때까지 반복
    while section:
        start = section.popleft()  # 페인트칠 시작 지점

        while section and start + m > section[0]:
            section.popleft()
        answer += 1

    return answer


def my_wrong_solution(n, m, section):  # 구역 / 롤러 길이
    answer = 0
    length = 0
    i = len(section) - 1
    while i > 0:  # 1까지
        if m == 1:
            return len(section)
        if not length:  # length == 0 일 경우
            dif = section[i] - section[i - 1] + 1
        else:
            dif = section[i] - section[i - 1]
        length += dif
        if length < m:
            i -= 1
            # continue
        elif length == m:
            answer += 1
            length = 0
            i -= 1
            # continue
        elif length > m:
            answer += 1
            # continue

        if i == 0:  # 마지막 요소인지 확인
            if length:
                answer += 1
            break

    return answer

# *** 주의
# [ 풀이 ]
# 시간초과 남
# 리스트 역순으로 탐색할 땐 deque 활용부터 고려하자
