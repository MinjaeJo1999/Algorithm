position = input()
r_c = [1, 2, 3, 4, 5, 6, 7, 8]

dx = [-2, -2, 2, 2, -1, 1, 1, -1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]

count = 0

# 선2후1 {상하좌우 * 좌우 } -> 8
for i in range(8) :
    moved_x = int(position[1]) + dx[i] #행(1)
    moved_y = ord(position[0]) - ord('a') + 1 + dy[i] #열(a)
    if moved_x in r_c and moved_y in r_c :
        count += 1

print(count)

# 더 나은 버전
def sol():
 input_data = input()
 row = int(input_data[1])
 column = int(ord(input_data[0])) - int(ord('a'))+1

 # 나이트가 이동할 수 있는 8가지 방향 정의
 steps = [(-2,-1), (-1,-2), (1,-2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

 #8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
 result = 0
 for step in steps:
     #이동하고자 하는 위치 확인
     next_row = row + step[0]
     next_column = column + step[1]
     #해당 위치로 이동이 가능하다면 카운트 증가
     if next_row >= 1 and next_row <= 8 and next_column >=1 and next_column <=8:
         result += 1

 print(result)


 # ***주의
 # 행렬 잘 구분, a(열)1(행)
 # 리스트 순서쌍 형식 가능
 # ord 함수