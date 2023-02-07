#이진 탐색 소스 코드
def binary_search1(array, target, start, end) : # 재귀함수
    if start > end :
        return None
    mid = (start+end) // 2
    if array[mid] == target :
        return mid
    elif array[mid] > target :
        return binary_search1(array, target, start, mid-1)
    else :
        return binary_search1(array, target, mid+1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search1(array, target, 0, n-1)
if result == None :
    print("원소가 존재하지 않습니다.")
else :
    print(result + 1)


#반복문 사용
def binary_search(array, target, start, end) :
    while start <= end :
        mid = (start + end ) // 2
        if array[mid] == target :
            return mid
        elif array[mid] > target:
            end = mid-1
        else :
            start = mid + 1
    return None

result = binary_search(array,target, 0, n-1)
if result == None :
    print("원소가 존재하지 않습니다.")
else :
    print(result + 1)