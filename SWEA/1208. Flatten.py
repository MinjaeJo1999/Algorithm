for test_case in range(1, 11):
    n = int(input()) # 덤프 횟수
    arr = list(map(int, input().split(' '))) # 입력 받기 # 만약 입력횟수 안주어져있고, 될때까지 입력하는 조건이라면?
    while n != 0 :
        arr_max = max(arr)
        max_idx = arr.index(arr_max)
        arr_min = min(arr)
        min_idx = arr.index(arr_min)
        arr[max_idx] -= 1
        arr[min_idx] += 1
        n -= 1
    print("#"+str(test_case), max(arr)-min(arr))