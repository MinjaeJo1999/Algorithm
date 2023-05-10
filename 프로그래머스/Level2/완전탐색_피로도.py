# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations

def my_solution(k, dungeons):
    dungeons.sort(key=lambda x: (-x[0]))  # 효율성 약간 챙기기 (확률 높을 것 같은 케이스 .. )
    arr = [i for i in range(len(dungeons))]  # 인덱스를 의미
    case = list(permutations(arr, len(arr)))
    answer = 0
    for target in case:
        tmp = k
        cnt = 0
        for i in target:  # 던전 방문 순서
            needs, use = dungeons[i][0], dungeons[i][1]
            if tmp >= needs:
                tmp -= use
                cnt += 1
            else:
                continue
        answer = max(answer, cnt)

    return answer


k = 80
dungeons = [[80,20],[50,40],[30,10]]
print(my_solution(k, dungeons))

# [ 풀이 ]
# 잘못된 처음 접근 :  소모 필요도가 적은 순, 최소 필요도가 높은 순으로 정렬
# > 만약 TC가 해당 정렬로 해도 되도록 주어져 있었다면 틀리는 것
# > TC가 정렬은 기준이 될 수 없다는 걸 친절하게 알려준 케이스였음
# 조합 사용 시 시간 복잡도 확인 : 8! -> 괜찮음 -> 완전탐색 적용 가능

# < 다른 풀이 >
# DFS, BFS로도 접근 가능
# 풀이 출처 : https://velog.io/@soorim_yoon/DFS%EC%99%84%EC%A0%84%ED%83%90%EC%83%89-%ED%94%BC%EB%A1%9C%EB%8F%84-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Level2

answer = 0
def DFS(k, cnt, dungeons, check):
    global answer
    answer = max(answer, cnt)
    for i in range(len(dungeons)):
        if check[i] == 0 and k >= dungeons[i][0]:  # 방문하지 않은 던전이고, 현재 피로도가 해당 던전을 방문하기 위한 최소 피로도보다 크면
            check[i] = 1
            # ** 중요 **
            # 이전 노드로 다시 back할 때, check 값만 0으로 바꿔줄 뿐 아니라
            # 현재 피로도의 수도 해당 노드를 방문하기 전의 피로도로 다시 복구해줘야 한다.
            # 따라서, 직접적으로 k 값과 cnt 값을 바꿔주기 보다는, DFS 함수 내에서 보내주는 매개변수의 값을 수정해줘야 한다.
            DFS(k - dungeons[i][1], cnt + 1, dungeons, check)
            check[i] = 0


def solution(k, dungeons):
    # answer = 0
    global answer
    check = [0] * len(dungeons)  # 방문 여부 체크하는 배열

    # cnt: 탐험한 던전 개수, k: 남은 피로도
    DFS(k, 0, dungeons, check)  # 0: 방문한 던전의 개수를 0으로 DFS 함수에 넘겨준다.

    return answer


#이때, 한 번에 탐색할 수 있는 DFS의 끝단까지 탐색을 완료한 후 다시 이전 단계로 돌아가는 작업을 해줘야한다.
#이 과정에서 이전노드로 돌아갈 때, 방문 여부(check 배열)와 방문 횟수(cnt)를 이전 노드까지 탐색했을 때의 값으로 복구해줘야 한다.
#answer를 전역 변수로 선언한다. answer(최종 탐험 횟수)를 전역변수로 선언하여 DFS 함수 내에서 계속 갱신되는 cnt 값과 비교하고, cnt값이 answer보다 큰 경우 answer를 해당 cnt 값으로 새롭게 갱신한다.