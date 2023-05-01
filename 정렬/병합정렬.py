def MergeTwoArea(arr, left, mid, right) :
    fIdx = left; #왼쪽 파트 가리키는 화살표
    rIdx = mid+1; #오른쪽 파트 가리키는 화살표

    sortArr = [0] * len(arr) #정렬한 결과 저장 array
    sIdx = left; #정렬 시작해야 하는 위치

    while(fIdx <= mid and rIdx <= right) : #분할된 범위 내에서 왼/오 파트 요소 하나씩 비교하며 정렬
        if arr[fIdx] <= arr[rIdx] : # 왼 <= 오 (정렬된 상태)
            sortArr[sIdx] = arr[fIdx]
            fIdx += 1
        else :
            sortArr[sIdx] = arr[rIdx]
            rIdx += 1
        sIdx += 1

    if(fIdx > mid) : #왼쪽 파트가 먼저 정렬을 마친 경우
        for i in range(rIdx, right+1) : #나머지 오른쪽 부분 리스트에 옮겨줌
            sortArr[sIdx] = arr[i];
            sIdx += 1
    else : #오른쪽 파트가 먼저 정렬을 마친 경우
        for i in range(fIdx, mid+1) : #나머지 왼쪽 부분 리스트에 옮겨줌
            sortArr[sIdx] = arr[i];
            sIdx += 1

    for i in range(left, right+1) : #정렬 중인 배열 arr에 sortArr의 결과 옮김
        arr[i] = sortArr[i];


def MergeSort( arr, left, right) : #정렬 대상, 정렬 범위 left~right
    # 중간 지점 계산
    if left < right : #재귀 종료 조건
        mid = (left+right) / 2
        #둘로 나눠서 각각 정렬
        MergeSort(arr, left, mid)
        MergeSort(arr, mid+1, right)
        #정렬된 두 배열 병합
        MergeTwoArea(arr, left, mid, right)


arr = [3,2,4,1,7,6,5]
MergeSort(arr, 0, len(arr)-1)
for i in range(len(arr)):
    print(arr[i], ' ')
