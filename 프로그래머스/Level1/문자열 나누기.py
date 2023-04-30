# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    answer = 0
    x_cnt = 0
    not_x = 0
    x = s[0]
    #for문, 마지막 문자열까지
    i = 0
    flag = False
    while i < len(s) :
            if flag :
                x = s[i]
                flag = False
            if x == s[i] :
                x_cnt += 1
            else :
                not_x += 1
            #if 횟수 같아지면
            if x_cnt == not_x and x_cnt != 0 :
                #answer+1
                answer += 1
                #cnt 초기화
                x_cnt, not_x = 0, 0
                flag = True
            i += 1
    #다 읽었는데 cnt 다르다면
    if x_cnt != not_x :
        answer += 1
    return answer

# [ 풀이 ]
# Flag 활용하지 않는 법 고민 (코드 가독성 위해)