# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/142086
def solution(s):
    answer = []
    for i in range(len(s)) :
        if i == 0 :
            answer.append(-1)
        else :
            tmp = s[0:i]
            tmp = list(reversed(tmp))
            #print(s[i], tmp)
            try :
                nearest = tmp.index(s[i])
                answer.append(nearest+1)
            except :
                answer.append(-1)
    return answer

s = "banana" # result = [-1, -1, -1, 2, 2, 2]
print(solution(s))

# 주의
# [ 풀이 ]
# list, reverse , reversed, find, index, try - except 적절한 방식으로 활용하기까지 시간 걸림
# find는 str에 대해서만 가능한 함수
# reversed, map 과 같이 객체 형태로 결과값 반환하는 함수 활용 시 주의