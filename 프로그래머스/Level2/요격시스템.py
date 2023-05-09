# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181188?language=python3

def solution(targets):
    answer = 1
    targets.sort(key=lambda x: (-x[1]))  # end 지점 내림차순 정렬
    std_scope = targets[0][0]  # 실수 : 기껏 내림차순 정렬시켜놓고 [-1][0] 마지막 값 가져옴
    # 뒤에서부터 비교
    for i in range(1, len(targets)):
        # x[1] 기준으로 내림차순 정렬
        start, end = targets[i][0], targets[i][1]
        # 타겟 x[1]이 현재 범위 밖이면 answer +1
        if end <= std_scope:
            answer += 1
            std_scope = start
            continue
        # 범위 변수 : 범위 작은 순으로 갱신 -> x[0] 값 기록
        std_scope = max(targets[i][0], std_scope)  # 뒤에서부터 비교하므로 클수록 앞에 있는 값

        # 주의
        # 시작, 끝점은 범위에 포함되지 않음 부등호 사용 시 주의
    return answer

# ***주의
# [ 풀이 ]
# 풀이 힌트 : 오름차순 정렬 혹은 내림차순 정렬
# 첫 풀이 54.0 / 100
# 실수 해결 후 100
# * 막대기 , 범위 키워드 나오는 문제는 정렬, 시작값, 끝값으로 접근해보기