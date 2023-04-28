def solution(t, p):
    answer = 0
    plen = len(p)
    tlen = len(t)
    p = int(p)
    for i in range(tlen-plen+1) : #실수 방지 : +1
        current = t[i:i+plen] # 실수 방지: plen 자리에 테스트 케이스 1개에만 부합하는 정수 넣어버림
        current = int(current)
        if current <= p :
            answer +=1
    return answer

t = "3141592"
p = "271"
t = "500220839878"
p = "7"
print(solution(t,p))