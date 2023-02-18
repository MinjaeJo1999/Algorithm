# 링크 : https://www.acmicpc.net/problem/2579
'''
계단 오르는 데는 다음과 같은 규칙이 있다.

계단은 한 번에 한 계단씩 또는 두 계단씩 오를 수 있다. 즉, 한 계단을 밟으면서 이어서 다음 계단이나, 다음 다음 계단으로 오를 수 있다.
연속된 세 개의 계단을 모두 밟아서는 안 된다. 단, 시작점은 계단에 포함되지 않는다.
마지막 도착 계단은 반드시 밟아야 한다.
따라서 첫 번째 계단을 밟고 이어 두 번째 계단이나, 세 번째 계단으로 오를 수 있다. 하지만, 첫 번째 계단을 밟고 이어 네 번째 계단으로 올라가거나, 첫 번째, 두 번째, 세 번째 계단을 연속해서 모두 밟을 수는 없다.

각 계단에 쓰여 있는 점수가 주어질 때 이 게임에서 얻을 수 있는 총 점수의 최댓값을 구하는 프로그램을 작성하시오.
'''
# 솔루션 참고 링크 : https://bio-info.tistory.com/158
def solution () :
    n = int(input())
    array = [int(input()) for _ in range(n)]
    dp = [0] * (n)

    if len(array) <= 2:  # 계단이 2개 이하일 땐 sum으로 바로 출력
        print(sum(array))
    else:
        dp[0] = array[0]  # ***주의: input 값 영향 받은 리스트 초기화 시 길이 최소일 경우까지 고려해주어야 인덱스 에러 나지 않음
        dp[1] = array[0] + array[1]
        for i in range(2, n):
            dp[i] = array[i] + max(dp[i - 3] + array[i - 1], dp[i - 2])
        print(dp[n - 1])  # ***주의:  else 스코프 안에 있어야, 안그럼 if len(array) <= 2일 때 중복 출력


def wrong_answer () :
    n = int(input())
    array = []
    for i in range(n) :
        array.append(int(input()))

    array.insert(0, 0) #index 0 에 0 추가

    dp = [0] * (n+1)

    dp[0] = 0
    dp[1] = array[1]
    flag = 1 # 시작 -> 시작점은 계단에 포함하지 않으므로

    for i in range(2, n+1) :
        if flag == 0 :
            dp[i] = array[i] + dp[i-2]
            flag = 1
            continue
        if dp[i-1] > dp[i-2]:  # flag 사용하려면 어떤 값이 max가 되었는지 알아야
            flag -= 1
            dp[i] = array[i] + dp[i-1]
        else :  # flag 사용하려면 어떤 값이 max가 되었는지 알아야
            dp[i] = array[i] + dp[i-2]
            flag = 1

    print(dp[n])

# *** 주의
# [ 풀이 ]
# "연속된 3개의 계단 밟으면 안됨" -> 1,2,3 모두 지나가면 안됨 !!
#   > 연속 한칸 이동 3번으로 이동해서 flag 설정 잘못했음
# 모든 경우를 아우르는 점화식을 생각하자
# [ 문법 ]
# array.insert(0, 0) : index 0 에 0 추가
# 인덱스 에러 주의 : 리스트 값 세팅 시 주의 (해당 인덱스가 없을 수도 있다)
# 출력 타이밍 주의

