# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    a_cnt, b_cnt, c_cnt = 0, 0, 0
    a = [1, 2, 3, 4, 5]  # 5개
    b = [2, 1, 2, 3, 2, 4, 2, 5]  # 8개
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10개

    for i in range(len(answers)):
        # 0,1,2,3,4 (0,1,2,3,4 / 5,6,7,8,9 %5 ->
        a_idx = (i % 5)
        b_idx = (i % 8)
        c_idx = (i % 10)
        if answers[i] == a[a_idx]:
            a_cnt += 1
        if answers[i] == b[b_idx]:
            b_cnt += 1
        if answers[i] == c[c_idx]:
            c_cnt += 1

    answer_cdt = [a_cnt, b_cnt, c_cnt]
    max_idx = answer_cdt.index(max(answer_cdt))
    answer.append(max_idx + 1)
    for i in range(max_idx + 1, 3):
        if answer_cdt[i] == answer_cdt[max_idx]:
            answer.append(i + 1)
    # 더 나은 코드 > 그냥 max 값 구하고 for문 하나씩 돌면서 요소 찾는 것이 더 깔끔함
    return answer

# **주의
# [ 풀이 ]
# * 가장 많이 맞은 사람 구할 때
# > 잘못된 접근 : if-else 분기
# > 선택한 로직 : max index 값 구하고 그 이후 max와 같은 값 가진 요소 추가하기