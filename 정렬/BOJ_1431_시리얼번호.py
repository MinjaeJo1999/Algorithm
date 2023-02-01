# 링크 : https://www.acmicpc.net/problem/1431

n = int(input())
array = []
for _ in range(n) :
    array.append(input())

def num_sum(a, b) :
    a_sum = 0
    b_sum = 0
    for i in range(len(a)) :
        if a[i].isdigit() :
            a_sum += int(a[i])
        if b[i].isdigit() :
            b_sum += int(b[i])
    return a_sum, b_sum

def array_sort(before, after) :
        if len(before) == len(after) : # 서로 길이가 같다면
            c, d = num_sum(before, after)
            if c == d :
                for i in range(len(before)) :
                    if before[i] < after[i] :
                        return True
                    elif before[i] == after[i] :
                        continue
                    return False # 빼먹었다가 틀림 (반드시 있어야), 들여쓰기 위치 주의
            return c < d # 아니면 False
        return len(before) < len(after) #아니면 Flase

for i in range(n-1) :
    for j in range(i+1,n) :
        if(array_sort(array[i], array[j])==False) :
            array[i], array[j] = array[j], array[i]

for i in array :
    print(i)

# 더 나은 풀이 : https://hongcoding.tistory.com/61
def sum_num(inputs) :
    result = 0
    for i in inputs :
        if i.isdigit() :
            result += int(i)
    return result

def sol() :
    n = int(input())
    arr = []
    for i in range(n) :
        arr.apend(input())
    arr.sort(key = lambda x: (len(x), sum_num(x), x))

# 주의
# [ 문법 ]
# 문자열 알파벳, 숫자 구분해주는 내장함수 : isalpha, isdigit
# 변수 실수
# a = 'abc' ,  for i in a   <= 가능
# [ 풀이 ]
# 알파벳 사전순 비교에서 삽질
#   > 알파벳 차례대로 비교하면서 더 아랫 글자이면 바로 True 리턴
#   > 같으면 다음 글자 비교 (continue)
#   > 더 윗글자이면 False 리턴
# 이 되도록 동작해야
# if 조건문으로 해결해서 코드 복잡
# return 구문의 위치 주의
# 더 나은 코드
#   > sort 함수 이용해서 간결하게 작성 가능

