# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/160586

# 출처 : https://ryong9rrr.github.io/pgm-Lv1-%EB%8C%80%EC%B6%A9-%EB%A7%8C%EB%93%A0-%EC%9E%90%ED%8C%90/
def solution1(keymap, targets):
    keytable = {}
    for keys in keymap: # 키맵 정보를 바탕으로 알파벳별 다이얼 회전 횟수 기록한 테이블 생성
        for i, key in enumerate(keys):
            if key not in keytable:
                keytable[key] = i + 1
            else:
                keytable[key] = min(keytable[key], i + 1)

    result = []
    for target in targets:
        clicked = 0
        for key in target:
            if key not in keytable:
                clicked = -1
                break
            clicked += keytable[key]
        result.append(clicked)

    return result


#출처 : https://velog.io/@heyggun/4%EC%BD%941%ED%8C%8C-60.-LV-1.-%EB%8C%80%EC%B6%A9-%EB%A7%8C%EB%93%A0-%EC%9E%90%ED%8C%90
import numpy as np

answer = []

for target in targets:
    tmp_num = 0
    for t in target:
        num_lst = []
        for k in keymap:
            try:
                num_lst.append(k.index(t)) #index 의 에러 발생을 효율적으로 활용한 예
            except:
                num_lst.append(np.inf)

        tmp_num += (min(num_lst) + 1)

    if tmp_num == np.inf:
        answer.append(-1)
    else:
        answer.append(tmp_num)

answer


# 삼중 포문 -> 바람직하지 않음
def my_solution(keymap, targets):
    answer = []
    for target in targets:
        cnt = 0
        flag = True
        alpha = list(target) # -> 리스트로 만들지 않아도 됨
        for letter in alpha: # target별 다이얼 count 세는 scope
            idx = [] # 실수방지 : 초기화 위치
            flag = True
            for i in range(len(keymap)):
                temp_idx = keymap[i].find(letter)
                idx.append(temp_idx)
            if idx.count(-1) == len(keymap) :
                answer.append(-1)
                flag = False
                break
            min_idx = 100
            for element in idx :
                if element != -1 and element < min_idx :
                    min_idx = element
            cnt += (min_idx +1)
        if flag :
            answer.append(cnt)

    return answer


#keymap = ["ABACD", "BCEFD"]
#targets = ["ABCD","AABB"]
#keymap = ["AA"]
#targets = ["B"]
#keymap = ["AGZ", "BSSS"]
#targets = ["ASA","BGZ"]
#keymap = ["ABDE"]
#targets = ["ABCE"]
keymap =  ["A"]
targets=["A","B"]
print(solution(keymap, targets))
# result : [9, 4]


# [ 풀이 ]
# 대수비교 시, -1 보다 큰 정수 중 가장 작은 idx가 있는지 없는지 확인하고 갱신해야 하는 것이 까다로웠음
# [-1,-1] -> -1
# [0, -1] -> 0
# [0, 1]  -> 0
# 이 되도록 로직 구성 (for문 사용 밖엔 답이 없는 것인가)
# -> -1일 때를 inf 처리해주면 min으로 구할 수 있음
# <틀렸습니다!>
#   >  keymap =  ["A"] targets=["A","B"] 예상 result : [1, -1] 인데 [-1]로만 나옴
#   > -1인 케이스 return 따로 처리하는 것이 아니라 배열에 해당 결과 추가하는 로직으로 가야 함