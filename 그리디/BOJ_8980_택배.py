# 링크: https://www.acmicpc.net/problem/8980
# 솔루션 참고 링크: https://johoonday.tistory.com/156

# 조건 1: 박스를 트럭에 실으면, 이 박스는 받는 마을에서만 내린다.
# 조건 2: 트럭은 지나온 마을로 되돌아가지 않는다.
# 조건 3: 박스들 중 일부만 배송할 수도 있다.

# 오답 코드
def wrong():
    n, c = map(int, input().split())
    m = int(input())
    info = []
    for _ in range(m) :
        info.append(list(map(int, input().split())))
    info.sort(key = lambda x: (x[1], x[0]))
    in_truck= 0
    result = 0
    print(info)

    moved_box = [] # 도착지, 용량
    for i in range(1, n+1) :
        # 택배 내리기
        # moved_box 리스트 for문 돌면서 moved[j][0]==i
        print('-------', i, '--------')
        if len(moved_box) > 0 :
            for j in range(len(moved_box)) : # 해당 for문에서 moved_box length 계속 줄어들어서 index 에러
                print(j, moved_box)
                if moved_box[j][0] == i :
                    result += moved_box[j][1]
                    in_truck -= moved_box[j][1]
                    print(result, in_truck)
                    # del moved_box[j] # 내리고, 배열에서 삭제 > 굳이 삭제할 필요 없음
        # 택배 싣기
        # info 리스트 for문 돌면서 info[k][0]==i 탐색
        before = 0
        for k in range(len(info)) :
            if info[k][0] < before :
                continue
            elif info[k][0] == i :
                temp = in_truck + info[k][2]
                if temp <= c : # 트럭 용량 c를 초과하지 않는다면 > 전체 탑승 > moved_list 추가
                    in_truck += info[k][2]
                    moved_box.append((info[k][1],info[k][2])) # (도착지,화물 무게)
                elif temp > c and c-in_truck > 0 : # 트럭 용량 c를 초과한다면 > 남은 용량이 있을 경우, 그만큼 탑승 > moved_list 추가
                    moved_box.append((info[k][1], c-in_truck))
                    in_truck = c
                before = info[k][0]
    print(result)

# 정답 코드
def sol() :
    n, c = map(int, input().split())
    m = int(input())
    arr = []
    for _ in range(m) :
        arr.append(list(map(int, input().split())))
    arr.sort(key=lambda x: x[1])

    box = [c]*(n+1)
    answer = 0
    for s, e, b in arr :
        _min = c
        for i in range(s,e) : #구간에 택배 채워넣기
            _min = min(_min, box[i]) #현재 구간의 잉여 공간 파악
        _min = min(_min,b) # 잉여 공간 vs 전달할 택배 개수에서 더 작은 수가 넣을 수 있는 택배의 개수가 됨
        for i in range(s, e) : #구간에 넣은 택배 정보 업데이트
            box[i] -= _min # 넣은 만큼 값을 빼서 현재 잉여 공간 수치 업데이트
        answer += _min #넣어진 택배는 배송이 보장되므로 바로 박스 수 업데이트
    print(answer)

sol()

# **** 주의
# [ 문법 ]
# 1 2 3 (\n) 3 2 1 (\n) 형식 입력 받는 코드
# 리스트 원소 삭제 > del list[인덱스] or list.remove[아이템] or del list[list.index(아이템)]
# for문 range 값은 변동하지 않는 값으로 두어야 함 (줄어들면 인덱스 에러 생김)
# [ 과정 ]
# 더 가까운 마을이 목적지인 택배부터 채워넣음
#   > 하차 시마다 새로운 택배를 최대한 채워넣기 위함
#   > 더 먼 마을의 택배가 밀려서 최대치를 놓치는 반례를 찾지 못하였으므로 이대로 진행함
# [ 풀이 ]
# 정렬 (도착 가까운 순, 출발 가까운 순) / (출발 가까운 순) (도착 가까운 순) 서로 로직이 다름
# 전자로 해야 최댓값 도출 가능 > 전자 로직도 오답 코드에서 그침
#  > 하지만 어떻게 확신할 수 있는지 이해 못함