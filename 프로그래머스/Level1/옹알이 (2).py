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