def solution(a, b, n): # 빈 병 a개 가져다주면 콜라 b병 주는 마트, 보유한 빈병
    answer = 0 #
    remain = n
    while remain >= a :
        give, empty = divmod(remain, a)
        remain = give*b + empty
        answer += give*b
    return answer

# 주의
# [ 풀이 ]
# b병 준다는 조건 사용 안함
# 테스트 케이스에 드러나있지 않은 문제 조건 빼먹지 말기