n, x = map(int, input().split())
array = list(map(int, input().split()))
result = -1
start = 0
end = n-1

while start <= end :
    mid = (start+end) // 2
    if array[mid] == x :
        x_start = mid
        x_end = mid
        i = 1

        while array[mid] == x :
            s_flag = 0
            e_flag = 0
            if (mid-i) >= 0 and array[mid-i] == x:
                x_start = mid-i
                s_flag = 1
            if (mid+i) < n and array[mid+i] == x:
                x_end = mid+i
                e_flag = 1
            if not s_flag and not e_flag :
                break
            i += 1
        result = x_end - x_start + 1
        break
    if array[mid] > x :
        end = mid - 1
    elif array[mid] < x :  # 작거나 같을 경우
        start = mid + 1

print(result)

#bisec 모듈을 사용한 더 나은 풀이
from bisect import bisect_left, bisect_right

#값이 [left_value, right_value] 인 데이터의 개수를 반환하는 함수
# 1 2 3 4 5 6 일때
# [2, 5] => right_index = 3 / left_index = 4
def count_by_range(array, left_value, right_value) :
    right_index = bisect_right(array, right_value)
    print(right_index)
    left_index = bisect_left(array, left_value)
    print(left_index)
    return right_index - left_index

#n, x = map(int, input().split())
#array = list(map(int, input().split()))

#값이 [x, x] 범위에 있는 데이터의 수 계산
count = count_by_range(array, x, x)

if count == 0 :
    print(-1)
else:
    print(count)




# ** 주의
# [ 문법 ]
# 인덱스 초과 예외 처리 빼먹지 말기
# while문 빠져나오는 조건 고려하기
# bisect 함수 활용법
# > a = [1,2,3,4,5,6]
# print(bisect_left(a, 2)) // 1 (배열에 이미 있는 수면 해당 자리 인덱스 출력함)
# print(bisect_right(a, 2)) // 2 (배열에 이미 있는 수면 해당 자리 오른쪽 위치의 인덱스 출력함)