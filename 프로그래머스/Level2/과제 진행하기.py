# 출처: https://school.programmers.co.kr/questions/46645
def solution(plans) :
    plans.sort(key = lambda x: x[1]) #굳이 숫자로 바꾸지 않더라도 정렬 됨
    answer = []
    stack = []

    for subject, start, time in plans :
        h, m = map(int, start.split(':'))
        start = 60*h+m
        time = int(time)

        if stack :
            prev_subject, prev_start, prev_time = stack.pop()
            extra_time = start - prev_start

            if extra_time < prev_time : #남은 시간 안에 과제 처리 못하면
                stack.append((prev_subject, prev_start, prev_time-extra_time))
            else:
                answer.append(prev_subject)
                extra_time = extra_time - prev_time

                while stack and extra_time : #다른 과제도 더 처리할 수 있다면
                    prev_subject, prev_start, prev_time = stack.pop()
                    if extra_time <prev_time :
                        stack.append((prev_subject, prev_start, prev_time-extra_time))
                        break
                    else :
                        answer.append(prev_subject)
                        extra_time = extra_time - prev_time

        stack.append((subject, start, time))
    answer.extend([s for s,_,_ in stack[::-1]])
    return answer








def wrong_solution(plans):
    answer = []
    # 새과제 시작
    # 진행중이던 과제 stop
    # 진행중이던 과제 끝
    # 우선순위 ) 새과제, 진행중이었던 과제
    # 진행중 과제 여러개일 경우) 가장 최근부터
    for i in range(len(plans)):
        hour = int(plans[i][1][0:2])
        minute = int(plans[i][1][3:5])
        time = int(plans[i][2])
        plans[i][1] = hour*60 + minute
        plans[i][2] = time
    plans.sort(key=lambda x: x[1])
    hw = plans[0][0] #첫번째 과제 시작
    time = plans[0][1] #현재 시간
    hw_time = plans[0][2] #과제 하는데 걸리는 시간
    remain=[]
    for i in range(1, len(plans)) :
        # 새 과제 시작
            # 이전 과제 마무리 되었는지, 아니면 stop해야 하는지 확인
            if time+hw_time == plans[i][1] : # 진행 중이던 과제 마무리 가능 조건: 과제 끝 예상 시간 = 새 과제 시작 시간
                answer.append(plans[i-1][0]) # 끝낸 과제
            elif time+hw_time < plans[i][1] : # 진행 중이던 과제 마무리 가능 조건: 과제 끝 예상 시간 < 새 과제 시작 시간
                answer.append(plans[i-1][0]) #새 과제 끝냄
                # 이 경우 사이 시간에 밀린 과제 해치워야 함
                interval_time = (plans[i][1] - (time+hw_time))
                if remain :
                    for i in range(len(remain)-1,-1,-1) : # 가장 최근 과제부터 시작
                        if remain[i][1] <= interval_time : #사이 시간 안에 해결할 수 있다면
                            answer.append(remain[i][0])
                            interval_time -= remain[i][1] #실수방지 : 남은 interval 시간 업데이트, remove 전에 해야 인덱스 에러 안남
                            remain.remove(remain[i])
                        else: #t사이 시간 안에 해결할 수 없다면
                            temp1= remain[i][0]
                            temp2= (remain[i][1]- interval_time)  #할 수 있는 만큼 진행하고
                            remain.remove(remain[i])
                            remain.append((temp1, temp2)) #남은 부분 다시 업데이트
                            break #실수방지: 다음 남은 과제까지 넘어갈 시간이 없으므로 반복문 탈출
            else : #진행 중이던 과제 stop 해야 한다면 (조건: 진행 중이던 과제 마치는 예상 시간 > 새 과제 시작되는 시간)
                #숙제와 남은 시간 저장
                remain_time = hw_time - (plans[i][1] - time)
                remain.append((plans[i-1][0], remain_time)) # korean, 10

            time = plans[i][1] #현재 시간
            hw_time = plans[i][2] #소요 시간
    answer.append(plans[len(plans)-1][0])
    for item in reversed(remain) :
        answer.append(item[0]) #남은 과제 우선순위대로 처리
    return answer


#plans = [["1", "00:00", "30"], ["2", "00:10", "10"], ["3", "00:30", "10"], ["4", "00:50", "10"]]
plans = [["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]
print(solution(plans))
# 시작 순서 : "music", "computer", "science", "history"
# ["science", "history", "computer", "music"]

# ***주의
# [ 풀이 ]
# 히든케이스에서 런타임 에러남
# 런타임 에러 : 인덱스 관리 못해서
# 런타임 에러 해결한 뒤에도 정확도 40만 달성함
# 스택 없이 풀 수 있지만 분기 처리가 많아져서 어디서 실수 나는지 파악할 수 없게 됨
# 스택 함수를 사용하지 않았을 뿐이지 로직은 같음
    # > 전처리를 너무 복잡하게 함 , 되도록이면 원본 데이터는 건드리지 말고 변수에 옮겨와서 활용하자
    # > for문에서 기준을 i-1이 되도록 하면서 마지막 요소에 대한 고려가 복잡해짐
        # 이전 데이터를 기준으로 정답 업데이트가 이루어지는 것 맞음
        # 따라서 굳이 현재 데이터의 과제 완료 유무를 따로 처리하지 않아도 됨, remain을 다루는 로직 안에서 공통으로 처리 가능
# <솔루션>
# 정렬과 스택 사용
