import heapq

# 오름차순 힙 정룔(heap sort)
def heapsort(iterable) :
    h = []
    result = []

    #모든 원소를 차례대로 힙에 삽입
    for value in iterable :
        heapq.heappush(h, value)
    for i in range(len(h)) :
        result.append(heapq.heappop(h))
    return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)

# 실행 결과
# [ 0, 1,2,3,4,5,6,7,8,9]
# 삽입, 삭제 시간 복잡도 : O(logN)