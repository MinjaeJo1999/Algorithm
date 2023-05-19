from itertools import combinations, product
import copy

T = int(input())
for test_case in range(1, T + 1):
    num, n = map(int, input().split(' ')) # 최대 6자리 , 최대 10번
    arr = list(map(int, str(num)))
    # 시간 복잡도 체크 :
    # 6C2 -> 15 -> 중복 순열 -> 메모리 초과 에러
    idx = [i for i in range(len(arr))]
    cm1 = list(combinations(idx, 2))
    #print(cm1)
    pm1 = list(product(cm1,repeat= n))
    result = ''
    biggest = 0
    for i in pm1 :  # ((1,2) (1,2))
        tmp = copy.copy(arr)
        for j in i :
            a = j[0]
            b = j[1]
            tmp[a], tmp[b] = tmp[b], tmp[a]
        cnum = int("".join(map(str, tmp)))
        if biggest < cnum:
            biggest = cnum
            result = str(cnum)

    print("#"+str(test_case), result)

# *** 주의
# [ 풀이 ]
# 완전 탐색 시도 시 시간 초과
# 백트래킹, 가지치기 작업 필요

# [문법 ]
# 123 -> 끊어서 리스트화 -> list(map(int, str(num)))
# 중복순열 : product( iterable 객체, repeat = n)
# [1,2,3] -> 123 -> cnum = int("".join(map(str, tmp)))


# 정답 풀이 (출처 : https://mungto.tistory.com/212)

# 경우의 수 찾기, 매개변수로 몇번 바꿧는지 적는다.
def dfs(count):
    global answer
    # 횟수를 다 사용했다면
    if not count:
        # 숫자로 바꿔보고
        temp = int(''.join(values))
        # 가지고 있는 최대수보다 크다면 갱신
        if answer < temp:
            answer = temp
        return
    # 바꿔야 하니까 이중 포문
    for i in range(length):
        # 경우의 수를 찾는거니까 i보다 큰위치부터
        for j in range(i + 1, length):
            # 두개의 위치를 바꾸고 나서
            values[i], values[j] = values[j], values[i]
            # 가지치기 해야하니까 일단 합쳐보고
            temp_key = ''.join(values)
            # 어떤수가 몇회차에 나왔는지 체크 1이면 안나온거니까 경우의 수에 넣어주기
            if visited.get((temp_key, count - 1), 1):
                # 이숫자는 몇회차에 사용했으니까 체크해주고
                visited[(temp_key, count - 1)] = 0
                # dfs도 돌려주고
                dfs(count - 1)
            # 다 썻으면 원상복귀
            values[i], values[j] = values[j], values[i]


for t in range(int(input())):
    answer = -1
    value, change = input().split()
    # 바꾸기 편하려고 리스트화시킴
    values = list(value)
    change = int(change)
    # 계속 쓸꺼니까 캐스팅
    length = len(values)
    # 가지치기용 딕셔너리
    visited = {}
    dfs(change)
    print('#{} {}'.format(t + 1, answer))


# [ 문법 ]
#