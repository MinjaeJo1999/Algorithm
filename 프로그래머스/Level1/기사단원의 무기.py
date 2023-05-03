# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/136798

def prime_num(num) : # 약수 구하는 함수
    cnt = 0
    for i in range(1, int(num**0.5)+1): #실수 : 범위 설정 num+1
        if num % i == 0 :
           cnt += 1
           if i ** 2 != num :
                cnt += 1
    return cnt


def solution(number, limit, power):
    answer = 0
    for i in range(1, number + 1):
        cnt = prime_num(i)
        #print(cnt)
        if cnt > limit:
            answer += power
        else:
            answer += cnt

    return answer

# result = 10
number = 5
limit = 3
power = 2
print(solution(number,limit,power))

# [ 풀이 ]
# 시간 초과
# > 1 ≤ number ≤ 100,000
# 10만 >