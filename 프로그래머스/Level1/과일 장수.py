# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(k, m, score):  # k: 사과 최대 점수, m: 사과의 수
    answer = 0
    score.sort(reverse=True)

    for i in range(len(score//m)):  # 정렬된 상태이므로 min 사용하지 않아도 최소값 구할 수 있음
        target = score[i * m:i * m + m] # 공간 효율성 떨어짐
        mini = min(target)
        if mini > k: result = k * m
        else: result = mini * m
        answer += result

    return answer

# [ 풀이 ]
# 코드 압축 1:
#    length = len(score)
#    share = length // m
# >     for i in range(len(score//m))
# 졸다 풀어서 문제 잘못 이해
# > 최저 품질이 K 점수를 넘으면 K 점수로 통일하는 것으로 이해함

# 코드 압축 2:
# for문 내부에서
# answer += score[i * m + m - 1] * m
