# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43163
from collections import deque

def check(begin, word) :
    cnt = 0
    for i in range(len(begin)) :
        if begin[i] != word[i] : # 실수 , 조건 잘못 적용 (같은 문자 1개로 적용)
            cnt += 1
    return cnt

def bfs(begin, target, words, visited) :
    que = deque([begin])
    cnt = 0
    while que :
        compare = que.popleft()
        if compare == target :
            idx = words.index(compare)
            return visited[idx]
        for i in range(len(words)) :
            if not visited[i] and check(compare, words[i]) == 1 :  # 실수 , 조건 잘못 적용 (같은 문자 1개로 적용)
                if cnt == 0 :
                    visited[i] += 1
                    que.append(words[i])
                else:
                    visited[i] += visited[words.index(compare)] + 1
                    que.append(words[i])
        cnt += 1
    return 0

def solution(begin, target, words) :
    visited = [0 for _ in range(len(words))]
    result = bfs(begin, target, words, visited)
    return result


# 입출력 케이스 (출력 : 4)
begin, target, words = "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))


# ** 주의
# [ 풀이 ]
# 실수: 변환 과정 단계 카운트하는 로직 > visited에 단계 저장 > 풀이 복잡함
# 실수: 다른 문자 1개여야 한다는 조건 적용 반대로 함 (같은 문자 1개로)