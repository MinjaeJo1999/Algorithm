# ***주의
# [ 풀이 ]
# 순열 :
# > 공식 (nPr)
# > 서로 다른 n개중에 r개를 선택하는 경우의 수
# [ 문법 ]
# <풀이1>
# 순열 활용 : from itertools import permutations
# permutatotion 적용 시 만들어지는 순열 : per += list(permutations(nums, i))
# join 활용 :new_nums = [int(("").join(p)) for p in per]  (리스트값을 문자열로 합칠 때)
# 제곱 연산자 : **
# <풀이2>
# list, map, set

from itertools import permutations

def solution1(numbers):
    answer = []
    nums = [n for n in numbers]                   # numbers를 하나씩 자른 것
    per = []
    for i in range(1, len(numbers)+1):            # numbers의 각 숫자들을 순열로 모든 경우 만들기
        per += list(permutations(nums, i))        # i개씩 순열조합
    new_nums = [int(("").join(p)) for p in per]   # 각 순열조합을 하나의 int형 숫자로 변환

    for n in new_nums:                            # 모든 int형 숫자에 대해 소수인지 판별
        if n < 2:                                 # 2보다 작은 1,0의 경우 소수 아님
            continue
        check = True
        for i in range(2,int(n**0.5) + 1):        # n의 제곱근 보다 작은 숫자까지만 나눗셈 (합성수라면 제곱근 전의 범위까지만 돌아도 약수가 모두 나옴, 나머지 약수는 앞의 약수와 대응되는 약수임)
            if n % i == 0:                        # 하나라도 나눠떨어진다면 소수 아님!
                check = False
                break
        if check:
            answer.append(n)                      # 소수일경우 answer 배열에 추가

    return len(set(answer))                       # set을 통해 중복 제거 후 반환

numbers = "011"
print(solution1(numbers))


#다른 풀이 : https://iambeginnerdeveloper.tistory.com/122
# 소수 판별 함수
def is_prime_number(x):
    if x < 2:
        return False

    for i in range(2, x): #범위 줄이지 않고 모두 시도해보는 방법
        if x % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0

    num = []
    for i in range(1, len(numbers) + 1):
        # 순열 모듈 사용해서 나올 수 있는 모든 수 조합
        num.append(list(set(map(''.join, permutations(numbers, i)))))
    per = list(set(map(int, set(sum(num, [])))))

    for p in per:
        if is_prime_number(p) == True:
            answer += 1

    return answer