def solution(ingredient):
    answer = 0
    # 아래, 위 -> 스택
    # 빵, 야채, 고기, 빵
    i = 0
    stack = []
    for i in range(len(ingredient)) :
        stack.append(ingredient[i])
        if stack[-4:] == [1,2,3,1] :
            for _ in range(4) :
                stack.pop()
            answer += 1

    return answer

def wrong_solution(ingredient):
    answer = 0
    # 아래, 위 -> 스택
    # 빵, 야채, 고기, 빵
    i = 0
    while i < len(ingredient):
        tmp = ingredient[i:i + 4]
        if tmp == [1, 2, 3, 1]:
            del ingredient[i:i + 3]
            answer += 1
            i = ingredient.index(1)
            continue
        i += 1

    return answer


# *** 주의
# [ 풀이 ]
# 시간 초과 주의
# pop() 사용해야
# [문법]
# 리스트 슬라이싱 stack[-4:]