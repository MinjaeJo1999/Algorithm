def solution(players, callings) :
    answer = []
    players_map = {value: key for key, value in enumerate(players)} # 이름: key, 1(등수) : value
    for i in callings :
        idx = players_map[i]
        players_map[i] -= 1
        players_map[players[idx-1]] += 1 #실수방지 : 딕셔너리에서 정수값이 value 위치라는 점 잊으면 안됨
        players[idx-1], players[idx] = players[idx], players[idx-1]
    answer = players
    return answer

# index find 과정에서 시간 초과
def wrong_solution(players, callings):
    answer = []
    for i in range(len(callings)):
        idx = players.index(callings[i])
        # idx 번째 player와 앞선수의 위치가 바뀜
        players[idx], players[idx - 1] = players[idx - 1], callings[i]
    answer = players
    return answer

# ***주의
# [ 풀이 ]
# for문과 for문 아래 명령어가 독립적으로 callings 배열(크기:M)과 players 배열(크기:N)의 크기에 비례
# 시간복잡도는 둘의 곱인 O(MN)이 됨 일
# 일반적으로 O(n)에서 n의 값이 1억을 넘으면 통과가 어려움
# 문제 조건을 보면 백만*5만=5백억이라는 수가 나옴
# > 양방향 인덱싱을 이용해야 하고, 딕셔너리 두 개 또는 딕셔너리 하나와 리스트 하나가 필요
