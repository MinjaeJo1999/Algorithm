# 링크 : https://school.programmers.co.kr/learn/courses/11133/lessons/71159

INC = 0
DEC = 1

def func_a(arr):
    length = len(arr)
    ret = [0 for _ in range(length)]
    ret[0] = 1
    for i in range(1, length):
        if arr[i] != arr[i-1]:
            ret[i] = ret[i-1] + 1
        else:
            ret[i] = 2
    return ret

def func_b(arr):
    global INC, DEC
    length = len(arr)
    ret = [0 for _ in range(length)]
    ret[0] = -1
    for i in range(1, length):
        if arr[i] > arr[i-1]:
            ret[i] = INC
        elif arr[i] < arr[i-1]:
            ret[i] = DEC
    return ret

def func_c(arr):
    ret = max(arr)
    if ret == 2:
        return 0
    return ret

def solution(S):
    check = func_b(S)
    dp = func_a(check)
    answer = func_c(dp)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
S1 = [2, 5, 7, 3, 4, 6, 1, 8, 9]
ret1 = solution(S1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

S2 = [4, 3, 2, 1, 10, 6, 9, 7, 8]
ret2 = solution(S2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")

S3 = [1, 2, 3, 4, 5]
ret3 = solution(S3)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret3, "입니다.")

# [ 가져갈 것 ]
# 함수 구조화 하는 법
'''
1. 각 숫자가 바로 이전 숫자보다 증가했는지, 혹은 감소했는지 표시한 리스트를 만듭니다.
  1-1. "증가"는 "INC", "감소"는 "DEC"로 표시합니다.
  1-2. 첫 번째 숫자는 증가도, 감소도 하지 않았다는 의미에서 -1로 표시합니다.

2. 1단계에서 만든 증가, 감소 리스트를 이용해 각 숫자를 마지막으로 하는 지그재그 수열 중 가장 긴 것의 길이를 담은 리스트를 만듭니다.
  2-1. 바로 전 숫자가 "증가"이고 현재 숫자가 "감소"이거나, 전 숫자가 "감소"이고 현재 숫자가 "증가"이면,
       현재 숫자를 마지막으로 하는 지그재그 수열 중 가장 긴 것의 길이는 (바로 전 숫자를 마지막으로 하는 지그재그 수열중 가장 긴 것의 길이 + 1)입니다.
  2-2. 그렇지 않으면 현재 숫자를 마지막으로 하는 지그재그 수열 중 가장 긴 것의 길이는 2입니다.
  2-3. 단, 첫 번째 숫자의 길이는 1로 초기화합니다.

3. 2단계에서 구한 리스트에 담긴 값 중 최댓값이 부분 수열 중 가장 긴 지그재그 수열의 길이입니다.
  3-1. 만약 최댓값이 2라면 0을 return 합니다.
  3-2. 그 외에는 최댓값을 return 합니다.
'''
# DP로 접근하는 발상