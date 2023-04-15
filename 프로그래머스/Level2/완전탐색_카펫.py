#링크: https://school.programmers.co.kr/learn/courses/30/lessons/42842
from itertools import permutations


def long_solution(brown, yellow):
    answer = []
    # 가로:x, 세로:y일 때 x*y, x+y 공식 도출
    x_plus_y =int( (brown + 4) / 2 ) # 실수방지 : int 없으면 float로 계산됨
    x_mult_y = yellow + brown
    arr = [i for i in range(1, x_plus_y + 1)]
    combi = list(permutations(arr, 2))
    for a, b in combi:
        if a + b == x_plus_y and a * b == x_mult_y:
            if a >= b:
                answer.append(a)
                answer.append(b)
                break # 실수방지 : 반드시 넣어줘야 , 안그럼 숫자 위치만 다른 같은 조합도 답에 추가됨
            else:
                answer.append(b)
                answer.append(a)
                break
    if not answer : # 실수방지 : 가로, 세로 길이가 같은 경우 (위의 순열 로직은 중복 허용하지 않으므로 이 경우 제외됨)
        answer.append(int(x_plus_y/2))
        answer.append(int(x_plus_y/2))

    return answer

brown = 8
yellow = 1
#print(long_solution(brown,yellow))

# **주의
# [ 풀이 ]
# for문에서 break
# 순열은 중복 허용하지 않는다는 점 주의
# > (n,n)와 같은 순열이 적용되지 않는 케이스 있다는 점 파악했어야
#공식1
# > brown = 2(x+y)-4        > 나눗셈 없으므로 int값 유지 가능
# > x+y = (brown+4) / 2     > 나눗셈이 들어가면 float 값이 도출된다는 점 유의
#공식2
# > x*y = yellow + brown
# [ 문법 ]
# 연산식에서 float => int로 바꿔주기


#완전 탐색 관점에서 더 직관적인 풀이
# 출처 : https://dev-note-97.tistory.com/87
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for b in range(1, total + 1): #1부터 total까지 차근차근 돌면서
        if (total / b) % 1 == 0:  #total / b = a  (자연수 조건, ex. (9 / 2) % 1 => 0.5가 됨)
            a = total / b #a * b = total (계산식에서 나온 공식1)
            if a >= b:  #가로 길이가 더 긴 조합이어야 하므로, (설령 이 파트에서 맞는 조합이 나오더라도 위치 변경 없이 패스함, 가로길이만 고려)
                if 2 * a + 2 * b == brown + 4:  #계산식에서 나온 공식2
                    return [a, b]

    return answer

print(solution(brown,yellow))