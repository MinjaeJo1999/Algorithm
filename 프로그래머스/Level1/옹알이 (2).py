# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/133499

import re
def solution(babbling):
    # 각 원소에 속한 발음 가능한 단어를 숫자로 치환
    for i in range(len(babbling)):
        babbling[i] = babbling[i].replace('aya','1')
        babbling[i] = babbling[i].replace('ye','2')
        babbling[i] = babbling[i].replace('woo','3')
        babbling[i] = babbling[i].replace('ma','4')

    cnt = 0
    # 각 단어마다 확인
    for babble in babbling:
        # 숫자가 아닌 문자가 남아 있는 경우
        if re.findall('[a-z]',babble): continue
        # 숫자만 남아있지만 연속된 숫자가 존재하는 경우
        elif '11' in babble or '22' in babble or '33' in babble or '44' in babble: continue
        # 숫자만 존재하며 연속된 숫자가 없는 경우
        else: cnt += 1
    return cnt

# re 모듈 사용
# replace 함수 사용

def my_solution(babbling):
    answer = 0
    dic = ['aya','ye','woo','ma']
    for target in babbling :
        s = 0
        e = 2 # 단어 최소 두자리이므로
        before = ''
        flag = True
        while True :
            if e > len(target) :
                flag = False
                break
            if target[s:e] in dic :
                if before == target[s:e] :
                    flag = False
                    break
                else :
                    before = target[s:e]
                    flag = True
                    if e == len(target) : break
                s = e
                e = s+2
            else :
                e += 1
                flag = False
        if flag :
            answer += 1
    return answer

    # 유의 : 연속한 같은 발음 찾기 (불연속이면 상관없음)
    # for문
    # while문: 단어별로 발음할 수 있는지 check
    # idx 0 부터 end index 늘려가면서 dic에 있는지 체크
    # -> 있다면 다음 시작 인덱스는 마지막 인덱스 다음으로 갱신
    # -> 이전 단어 뭐였는지 저장
    # 탈출 조건 : end 값이 단어 길이보다 클 때
    #   > 해당 조건이 유효하기 위해선 ayaye 와 ayaa인 케이스 구분해야 함
    # flag 통해 answer 추가 여부 판단
    # 알맞은 flag True / False 거쳐야 함
    #   > 답이 되는 것 : end == len(단어)인 순간이 무조건 있음

def my_solution1(babbling):
    answer = 0
    dic = ['aya', 'ye','woo','ma']
    for word in babbling :
        a = 0
        list = [0 for _ in range(4)]
        for i in range(1,len(word)+1) :
            if word[a:i] in dic :
                    if i < len(word)-1 and word[i] == word[i+1] :
                            print(word[a:i])
                            break
                    idx = dic.index(word[a:i])
                    list[idx] += 1
                    a = i
                    break
        if max(list) == 1 : answer+=1
    return answer

# 로직 구현 중 오류
# > 오류 못 잡음
# > 다시 풀기