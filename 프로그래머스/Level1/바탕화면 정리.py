# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/161990

def my_solution(wallpaper):
    answer = []

    arr = []
    for i in range(len(wallpaper)):  # 행
        for j in range(len(wallpaper[i])):  # 열
            if wallpaper[i][j] == '#':
                arr.append((i, j))

    # start : 행 가장 높고(작고), 열 가장 왼쪽(작고) 위치
    # end : 행 가장 낮고, 가장 오른쪽 위치
    arr.sort()
    row_start = arr[0]
    row_end = arr[-1]
    arr.sort(key=lambda x: x[1])
    col_start = arr[0]
    col_end = arr[-1]

    answer = [row_start[0], col_start[1], row_end[0] + 1, col_end[1] + 1]
    return answer

# 20 m

#<더 효율적인 솔루션>
# 코드상 더 간결하고 효율적
# 파이썬 내장 함수의 시간복잡도 비교해볼 때
# sort : O(nlogn)
# min, max : O(n)

def solution(wall):
    a, b = [], []
    for i in range(len(wall)):
        for j in range(len(wall[i])):
            if wall[i][j] == "#":
                a.append(i)
                b.append(j)
    return [min(a), min(b), max(a) + 1, max(b) + 1]