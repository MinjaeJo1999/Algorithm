# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42883

# 풀이 출처 : https://chiefcoder.tistory.com/37
def solution(number, k):
    answer = []

    for i in number:
        while k > 0 and answer and answer[-1] < i:
            answer.pop()
            k -= 1
        answer.append(i)

    return ''.join(answer[:len(answer) - k])

def my_wrong_solution(number, k):
    answer = ''
    arr = [int(i) for i in number]
    length = len(arr) - k

    if length == 0: # 주어진 배열 길이 == 구성해야 하는 길이인 경우
        answer += "".join([str(i) for i in arr])
        return answer

    maximum = max(arr[0:len(arr) - k]) # 가장 큰 첫번째 숫자 고름 (숫자 길이 보장하는 범위 확보)
    answer += str(maximum)
    idx = arr.index(maximum) + 1 # 다음 숫자부터 탐색
    for i in range(0, idx):
        arr[i] = 0
    length -= 1
    while True:
        if len(arr[idx:]) == length:  # 필요한 개수만큼 남았다면
            answer += "".join([str(i) for i in arr[idx:]])  # 그대로 더함
            break
        if idx >= len(arr) - 1: # 끝 인덱스까지 왔을 경우
            break
        tmp = arr[idx:len(arr) - length + 1] #
        answer += str(max(tmp))
        idx = arr.index(max(tmp)) + 1
        length -= 1

    return answer

number, k = "1924", 2
print(solution(number,k))


# *** 주의
# [ 풀이 ]
# arr 범위 쪼개면서 max 값 찾는 방식으로 접근
# 합계: 8.3 / 100.0
# 시간 초과 에러 다수
# 주어진 테스트케이스만 통과

# 접근 시 문제에서 제시한 대로 숫자를 버리는 것이 아니라,
# 최댓값을 찾아서 result에 추가하는 식으로 함
# 생각 쓸데없이 복잡하게 함
