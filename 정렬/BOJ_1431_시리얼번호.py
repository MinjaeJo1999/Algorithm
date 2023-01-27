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
                    if ord(before[i]) > ord(after[i]) :
                        return False
            return c < d # 아니면 False
        return len(before) < len(after) #아니면 Flase

for i in range(n-1) :
    for j in range(i+1,n) :
        if(array_sort(array[i], array[j])==False) :
            array[i], array[j] = array[j], array[i]

for i in array :
    print(i)

# 주의
# [ 문법 ]
# 문자열 알파벳, 숫자 구분해주는 내장함수 : isalpha, isdigit
# 변수 실수

