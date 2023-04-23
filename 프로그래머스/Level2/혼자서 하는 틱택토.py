# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/160585
# 유형 : 경우의 수

#솔루션 출처 : https://yuni0822.tistory.com/m/334
def isWin(board, x, y):
    leftY, rightY = (y - 1) % 3, (y + 1) % 3 # 묘기
    if board[x][y] == board[x][leftY] == board[x][rightY]: # 가로 빙고
        return True

    upX, downX = (x - 1) % 3, (x + 1) % 3 # 묘기
    if board[x][y] == board[upX][y] == board[downX][y]: # 세로 빙고
        return True

    # 대각선 빙고
    if (board[x][y] == board[upX][leftY] == board[downX][rightY]) or (board[x][y] == board[upX][rightY] == board[downX][leftY]):
        return True

    return False

def solution(board):
    n = len(board)

    oList, xList = [], []
    for x in range(n):
        for y in range(n):
            if board[x][y] == 'O':
                oList.append((x, y))
            elif board[x][y] == 'X':
                xList.append((x, y))

    if len(oList) < len(xList) or len(oList) >= (len(xList) + 2):
        return 0

    for x, y in oList:
        if isWin(board, x, y) and len(xList) != (len(oList) - 1):
            return 0

    for x, y in xList:
        if isWin(board, x, y) and len(xList) != len(oList):
            return 0

    return 1


def check(board) :
    diagonal = 0
    sero = 0
    garo = 0
    dic = {'O': 0, 'X': 0, '.': 0}
    for i in range(3) : # 가로 빙고 탐색
        if board[i][0] == board[i][1] == board[i][2] :
            dic[board[i][0]] += 1
            garo += 1

    for i in range(3) : # 세로 빙고 탐색
        if board[0][i] == board[1][i] == board[2][i] :
            dic[board[0][i]] += 1
            sero += 1

    if board[0][0] == board[1][1] == board[2][2] :
        dic[board[0][0]] += 1
        diagonal += 1

    if board[0][2] == board[1][1] == board[2][0] :
        dic[board[0][2]] += 1
        diagonal += 1

    o_scs = dic['O']
    x_scs = dic['X']
    if o_scs == 2 :
        if (garo == 1 and sero == 1) or (garo == 1 and diagonal == 1) or (sero == 1 and diagonal == 1) or diagonal == 2 :
            o_scs = 1
    if x_scs == 2 :
        if (garo == 1 and sero == 1) or (garo == 1 and diagonal == 1) or (sero == 1 and diagonal == 1) or diagonal == 2 :
            x_scs = 1

    return o_scs, x_scs

def my_solution(board):
    answer = 1
    # <성립 안되는 경우>
    # 1) O와 X의 성공 횟수를 세어봄
    #   > 성공횟수가 1회 이상임
    #   > O와 X 둘 다 성공함
    # 2) O와 X의 개수를 세어봄
    #   > O와 X 중 둘 중 하나가 이겼는데 게임이 계속 됨 (O와 X가 둘다 이기는 경우 포함. 1)에서 해결됨)
    #   > X 개수가 O 개수보다 많음 (X가 먼저 시작하는 경우 포함)
    # <성립 되는 경우>
    # 칸 모두 찼는데 승패 안남
    # 빈칸임
    o_cnt = 0
    x_cnt = 0
    o_scs, x_scs = check(board)
    if o_scs > 1 or x_scs > 1 or (o_scs==1 and x_scs==1) :
        return 0
    for i in range(3) :
        o_cnt += board[i].count("O")
        x_cnt += board[i].count("X")
    if not(0 <= o_cnt-x_cnt < 2) :
        return 0
    if x_scs > o_scs and o_cnt != x_cnt :
        return 0
    if x_scs < o_scs and not(o_cnt > x_cnt) :
        return 0

    return answer

#board = ["O.X", ".O.", "..X"] # 1
#board = ["OOO", "...", "XXX"] # 0
#board = ["...", ".X.", "..."] # 0
#board = ["...", "...", "..."] # 1
#board = ["00.", "0.0", "XXX"] # 0
#board = ['OXO','XOX','OXO'] # 1
board = ['OOO','XOX','XXO'] # 1

print(my_solution(board))
# 솔루션 참고 링크 : https://chamdom.blog/pg2-160585/
# <놓친 코너케이스>
# X가 승리했는데 O와 X의 수가 같지 않은 경우
# O가 승리했는데 O의 수가 X보다 많지 않은 경우
# O개수 - X개수의 값이 1 초과인 경우
# 빙고 2개인데 2개 빙고를 동시에 만드는 요소가 하나 존재할 경우
'''
OOO
XOX
XXO
'''
'''
OOO
XOX
XXO
'''
# 성공횟수가 2 이상이면 성립 불가능으로 판단한 조건 때문에 (if o_scs > 1 or x_scs > 1 or (o_scs==1 and x_scs==1))
# 위의 케이스가 성립 불가능으로 분리됨
# 성공횟수 셈하지 않아도 되는 이유
#   > O, X의 개수 차이를 통해 실수 유무 판단할 때 자연스럽게 제외됨
#   > 이 조건으로 인해 문제 없는 경우도 문제 있는 케이스로 잘못 분류되었음

# 조건의 포함관계를 잘 따져야 함
# 해당 조건이 어떤 종류의 예외 케이스들을 걸러낼 수 있는지에 대한 판단
# 기준을 추가하면 잘못된 분기를 추가되는 것이므로 케이스 분류에 오류가 날 수밖에 없음


# <다시 정리>
# 내가 생각한 성공 / 실패 케이스
# <성립 안되는 경우>
# 1) O와 X의 성공 횟수를 세어봄
#   > 성공횟수가 1회를 초과함 -> ***언제나 성립 불가능하진 않음
#   > O와 X 둘 다 성공함
# 2) O와 X의 개수를 세어봄
#   > O와 X 중 둘 중 하나가 이겼는데 게임이 계속 됨 (O와 X가 둘다 이기는 경우 포함. 1)에서 해결됨) -> *** 언제나 성립 불가능하진 않음
#   > X 개수가 O 개수보다 많음 (X가 먼저 시작하는 경우 포함)
# <놓친 코너케이스>
# X가 승리했는데 O와 X의 수가 같지 않은 경우
# O가 승리했는데 O의 수가 X보다 많지 않은 경우
# O개수 - X개수의 값이 1 초과인 경우
# 빙고 2개인데 2개 빙고를 동시에 만드는 요소가 하나 존재할 경우 성립 가능한 케이스로 분류되어야 함


# 아래 3가지 조건으로도 내가 생각한 기준으로 케이스 분류 가능함
# O의 개수-X의 개수가 0이거나 1인지를 체크했다면)
#   > O개수 - X개수의 값이 1 초과인 경우
#   > X 개수가 O 개수보다 많음 (X가 먼저 시작하는 경우 포함)
#   > 성공횟수가 1회를 초과하는 경우 중 성립 불가능한 케이스 걸러냄

# O가 이긴 정황을 확인했을 때, X의 개수 == O의 개수-1 인지를 체크했다면)
#  > O가 승리했는데 O의 수가 X보다 많지 않은 경우
#  > O와 X 둘 다 성공함

# X가 이긴 정황을 확인했을 때, X의 개수 == O의 개수 인지를 체크했다면)
#  > X가 승리했는데 O와 X의 수가 같지 않은 경우

