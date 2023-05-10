# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    _dict = {k:[] for _,k in clothes}
    for v,k in clothes :
        _dict[k].append(v)
    res = 1
    for v in _dict.values() : # values 반환값 바로 활용 가능
        res *= (len(v)+1) # len으로 바로 활용 가능
    return res -1


from itertools import combinations
def my_solution(clothes): # 시간 초과
    answer = 0
    # 의상이 하나라도 다르거나 착용 의복 개수가 다르면 OK
    dic = {}
    for i in clothes:
        if i[1] in dic:
            dic[i[1]] += 1
        else:
            dic[i[1]] = 1
    arr = list(dic.keys())
    for i in range(1, len(arr) + 1):
        # i개 고를 때
        combi = list(combinations(arr, i))

        for j in combi:  # 실수: 튜플형태 , (문자열, 문자열, 문자열, 문자열) -> (정수형, 정수형, 정수형 ) 취급함
            result = 1 #실수: 초기화 시점
            for k in range(len(j)):  # i도 됨
                result *= dic[j[k]]
            answer += result # 실수: 업데이트 시점

    return answer

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))

#*** 주의
# [ 풀이 ]
# 1차 풀이 시간 초과,  합계: 96.4 / 100.0
# 시간 초과 이유 : 옷이 30개라면 조합 30C1, 30C2, 30C3 --- 30C1의 조합에서 나오는 케이스를 모두 거치는 것이므로
# 수가 기하급수적으로 늘어남
# <솔루션 발상>
# 어떻게 접근하면 솔루션을 파악할 수 있었을까?
# > 조합으로 접근했던 이유 : 종류별로 가지고 있는 의복 수 a*b*c 를 했을 때 옷을 하나만 입는 케이스를 포함시키지 못했다
# > 이 문제를 다른 방식으로 해결할 고민을 했어야 함
# > 투명 의복을 하나 포함시키면 하나씩 입는 경우의 수도 모두 나옴
# > 마지막에 모두 투명 의복을 입는 케이스 하나만 빼주면 됨