# 출처 : https://velog.io/@minmong/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv.1-%EB%AA%85%EC%98%88%EC%9D%98-%EC%A0%84%EB%8B%B9-Python-velog
def solution(k, score):
    answer = []
    a=[]
    for i in score:
        if len(a)<k:
            a.append(i)
        else:
            if min(a)<i:
                a.remove(min(a))
                a.append(i)
        answer.append(min(a))
    return answer


def my_solution(k, score):
    answer = []
    stage = []
    # for, score 만큼
    for i in range(len(score)) :
        if len(stage) < k:
            stage.append(score[i])
            stage.sort(reverse = True)
            answer.append(stage[-1])
            continue
        elif len(stage) == k : # -> else로 해도 무방
            if score[i] > stage[-1] : #
                stage[-1] = score[i]
                stage.sort(reverse = True)
                answer.append(stage[-1])
                continue
            elif score[i] == stage[-1] : # 실수 : 같은 경우도 포함
                answer.append(stage[-1])
                continue
        answer.append(stage[-1]) # 실수 : 위 분기에 포함되지 않는 케이스 처리
    return answer


# [ 풀이 ]
# if 문 사용할 경우 여러 케이스 적절하게 분기되는지 확인 필요
# 같은 논리의 로직 반복된다면 코드 단순화하는 법 고민하기
# 정렬보다 min, max 함수 (더 효율성 높은 거) 먼저 사용해보기