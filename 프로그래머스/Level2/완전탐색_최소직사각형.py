def solution(sizes) :
    for i in range(len(sizes)) :
            if sizes[i][0] < sizes[i][1] :
                sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
    sizes.sort(reverse=True)
    max_w = sizes[0][0]
    sizes.sort(key =lambda x : -x[1])
    max_h = sizes[0][1]
    answer = max_w*max_h

    return answer


#제대로 잘못 푼 문제.. 발상을 효율적으로 활용하자
def wrong_solution(sizes):
    answer = 0
    sizes.sort(reverse=True)  # 내림차순 정렬
    max_w = sizes[0][0]
    max_w_h = sizes[0][1]
    sizes.sort(key=lambda x: -x[1])
    max_h = sizes[0][1]
    max_h_w = sizes[0][1]
    #print('max_w, max_h', max_w, max_h)
    if max_w > max_h:  # 최댓값이 가로 길이에서 나올 때
        for i in range(len(sizes)):
            if sizes[i][1] > sizes[i][0]: #가로 > 세로가 되도록 값 교환
                sizes[i][1], sizes[i][0] = sizes[i][0], sizes[i][1]
        sizes.sort(key=lambda x: -x[1])
        #print(sizes)
        h = sizes[0][1]
        answer = max_w * h
        #print('1번')
    elif max_w < max_h:  # 최댓값이 세로 길이에서 나올 때
        for i in range(len(sizes)):
            if sizes[i][0] > sizes[i][1]: # 가로 < 세로가 되도록 값 교환
                sizes[i][1], sizes[i][0] = sizes[i][0], sizes[i][1]
        sizes.sort(key=lambda x: -x[1])
        w = sizes[0][0]
        answer = max_h * w
        #print('2번')
    else:  # max_w == max_h일 때
        # 가로 > 세로가 되도록 값 교환 / 세로 > 가로여도 상관없음
        for i in range(len(sizes)):
            if sizes[i][1] > sizes[i][0]: #가로 > 세로가 되도록 값 교환
                sizes[i][1], sizes[i][0] = sizes[i][0], sizes[i][1]
        sizes.sort(key=lambda x: -x[1])
        h = sizes[0][1]
        answer = max_w * h

    return answer

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))

# ***주의
# [ 풀이 ]
# 처음 풀이 : 40점
# ㄴ else 고침
# 두번째 풀이 : 90점
# ㄴ 테케 2개 통과 못함

''' 잘못 푼 부분
    else:  # max_w == max_h일 때
        if max_w_h < max_h_w:
            answer = max_h * max_w_h
            #print('3번')
        elif max_h_w < max_w_h:
            answer = max_w * max_h_w
            #print('4번')
        else:  # 이 경우도 길이 같다면
            answer = max_w * max_h
            #print('5번')
'''