def solution(park, routes):
    answer = [0,0]
    #딕셔너리로 해도 될듯
    #동: E, 서: W, 남:S, 북: N
    dr = {'E': 0, 'W': 0, 'S':1, 'N':-1} # N -> W로 오타냄
    dc = {'E': 1, 'W': -1, 'S':0, 'N':0}
    max_r = len(park)
    max_c = len(park[0])
    r,c = 0,0 #활용 과정에서 실수
    #시작 위치 찾기
    for i in range(len(park)):
        for j in range(len(park[i])) :
            if 'S' in park[i] :
                answer[0] , answer[1] = i,  park[i].index("S")
                break # 효율성 챙기자
    #print('시작:', answer)
    for route in routes :
        #print('----',route,'--------')
        dir, dist = route.split(' ')
        dist = int(dist)
        flag = True
        move_r = answer[0]
        move_c = answer[1]
        for i in range(dist) :
            move_r += dr[dir]
            move_c += dc[dir]
            if 0 <= move_r < max_r and 0 <= move_c < max_c: #max_r = len(park)-1로 설정해두고 < 라고 해서 오류
                if park[move_r][move_c] == 'X':
                    flag = False
            else:
                flag = False
        if flag :
            answer[0], answer[1] = move_r, move_c
        #print(answer)
    return answer

park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]

print(solution(park, routes))

# <실수>
# for문 다 돌고 난 후에 이동 지점 정보 갱신해야 함-> 중간에 막히면 전체를 물러야 하기 때문
# r,c 만들어놓고 사용을 안함.. 갱신되지 않은 값에 계속 더해줌
# 시작 지점 주어져 있다는 거 고려 안함

