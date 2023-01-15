# 링크 : https://www.youtube.com/watch?v=7C9RgOcvkvo

n, m = map(int, input().split()) #행(x)/렬(y)
ice = []
for _ in range(n) :
    ice.append(list(map(int, input())))

def dfs (x, y) :
    if x <= -1 or x >= n or y <=-1 or y >=m :
        return False
    if ice[x][y] == 0 :
        ice[x][y] = 1
        dfs(x-1, y) # 상
        dfs(x,y-1) # 좌
        dfs(x+1, y) # 하
        dfs(x, y+1) # 우
        return True
    return False

result = 0
for i in range(n) :
    for j in range(m) :
        if dfs(i,j) == True :
            result += 1

print(result)



# *** 주의
# [ 풀이 ]
# DFS로의 접근 이전에 풀이 방법 고안해야
# 이어져 있는 0들 중 하나만 카운트해야 함
# > 첫번째 0을 만났을 때 연결되어 있는 모든 0이 다음 회차에 카운트 되지 않도록 해야 함
# > 0이면 카운트, 1이면 패스하도록 함
# > 첫번째 0을 만났을 때 깊이 우선 탐색법으로 연결된 모든 0을 1로 만들어주면 OK
# 상하좌우 이동 있을 시 인덱스 범위 에러 예외 처리 잊지 말것
