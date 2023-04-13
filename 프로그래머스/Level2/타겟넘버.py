def dfs(numbers, idx,target, result):
    global answer
    #print(answer)
    #print("result,idx: ",result, idx)
    if idx == len(numbers) - 1:  # 종료조건 > 배열의 끝까지 왔다면
        if result == target:  # 값이 목표한 바와 같다면
            answer += 1  # 정답 +1
        return
    idx += 1
    dfs(numbers, idx, target, result+numbers[idx])
    dfs(numbers, idx, target, result-numbers[idx])

def solution(numbers, target) :
    global answer
    answer = 0
    result = 0
    dfs(numbers, 0,target, result+numbers[0])
    dfs(numbers, 0,target, result-numbers[1])

    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers,target))

# ***주의
# [ 풀이 ]
# 마지막 요소까지 다다라서, result 초기화해야 할 때 그 다음 단계는 뭐가 되지..?
# > result 전역변수로 사용하지 않고 (마지막에 출력해야 하는 값이 아니므로) 매개변수에 전달-전달
# ! 재귀함수 사용 시
#   1) 종료 조건 , return 방식 고려
#   2) 매개변수를 통해서 전달될 값 고려
#   3) 필요한 전역 변수 고려
#   2와 3 잘 구분해야 함
# [ 문법 ]
# 전역변수 활용

# 참고한 풀이 : https://daeun-computer-uneasy.tistory.com/69?category=1053494


# 더 나은 풀이 : https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%ED%83%80%EA%B2%9F%EB%84%98%EB%B2%84-BFSDFS
def good_solution(numbers, target):
    n = len(numbers)
    answer = 0
    def dfs(idx, result):
        if idx == n:
            if result == target:
                nonlocal answer
                answer += 1
            return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
    dfs(0,0)
    return answer