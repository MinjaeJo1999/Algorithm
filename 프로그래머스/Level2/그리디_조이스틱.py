

def my_wrong_solution(name):
    answer = 0
    start = ord('A')
    arr = [chr(start + i) for i in range(26)]
    current = ['A' for _ in range(len(name))]

    now_cs = 0     # 현재 커서 위치
    target_cs = now_cs     # 다음 커서 위치
    for i in range(now_cs + 1, len(name)):
        if current[i] == name[i]:  # A=A일 때
            target_cs += 1
            continue
        else:
            target_cs += 1
            break
    print('시작: ', now_cs, target_cs)
    while True:
        print('while: ', now_cs)
        if name == current:
            break

        # <알파벳>
        # 현재 알파벳과 타겟 알파벳의 인덱스 차이 구하기
        target_idx = arr.index(name[now_cs])
        current_idx = arr.index(current[now_cs])  # A가 아닌 경우가 혹시 있을까봐
        print('1. ',target_idx, current_idx)
        idx_dif = abs(target_idx - current_idx)
        print('2. ',idx_dif)
        # 차이가 13 초과일 때 : 목표 지점까지 아래로 이동)
        if idx_dif > 13:
            print('3. ',name, current)
            while True:
                if current_idx == target_idx:
                    print('5-1. ',current_idx, target_idx)
                    current[now_cs] = name[now_cs]
                    print('6-1. ',name, current)
                    break
                current_idx -= 1
                answer += 1
                if current_idx == -1:
                    current_idx = 25

        # 나머지 : 위로 이동
        else:
            print('4. ',name, current)
            while True:
                if current_idx == target_idx:
                    print('5. ',current_idx, target_idx)
                    current[now_cs] = name[now_cs]
                    print('6. ',name, current)
                    break
                current_idx += 1
                answer += 1
                if current_idx == 25:
                    current_idx = 0

        if now_cs >= len(name)-1 : # 종료조건
            print('end')
            break

        # 현재 커서과 다음 커서의 인덱스 차이 구하기 (abs)
        dif = target_cs - now_cs  # abs 안취해도 항상 양수일걸 ..?
        print('7. ',dif)
        # 차이가 len // 2 초과일 때 : 커서 목표 지점까지 왼쪽 이동
        if dif > (len(name) // 2):
            while True:
                if target_cs == now_cs:
                    break
                now_cs -= 1
                answer += 1
                if now_cs == -1:  # 음수 범위라면 무조건 이 지점 지나야
                    print(now_cs)
                    now_cs = len(name) - 1
        else:
            while True:
                if target_cs == now_cs:
                    break
                now_cs += 1
                answer += 1
                if now_cs == len(name) :
                    now_cs = 0  # 이건 무슨 케이스지 ?
                    # 나머지 : 커서 목표 지점까지 오른쪽 이동
                    # 음수 되는 지점 예외처리 잘 해줘야
                    # 이동하면서 움직인 횟수 카운트
                    # 현재 커서 업데이트

        # <다음 커서 위치> (다음 턴에 현재 커서 위치, 다음 커서 위치 주어야)
        target_cs = now_cs
        for i in range(now_cs + 1, len(name)):
            if current[i] == name[i]:  # A=A일 때
                target_cs += 1
                continue
            else:
                target_cs += 1
                break
        print('8.', now_cs, target_cs)
        print('카운트 현황: ', answer)

                # 이동하면서 음수 되는 지점 예외 처리 잘해주기
    # 이동하면서 움직인 횟수 카운트
    return answer

name = "JEROEN"
print(solution(name))


# *** 주의
# [ 풀이 ]
# 1차 풀이 : 합계: 25.9 / 100.0

'''
1. 현재 커서, 다음 커서 알고 있는 상황
2. 현재 커서의 알파벳, 바꾸어야할 알파벳 
	=> 횟수 카운트 
2. 현재 커서 -> 다음 커서로의 이동 횟수 카운트
	=> 마지막 단계에서는 .. 패스해야하는 과정
	=> 
'''

# [ 문법 ]
# ord() : 문자 -> 아스키코드
# chr() : 아스키코드 -> 문자

