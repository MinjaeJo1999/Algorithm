# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 풀이출처 : https://somjang.tistory.com/entry/Programmers-%EA%B5%AC%EB%AA%85%EB%B3%B4%ED%8A%B8-Python
def solution(people, limit) :
    answer = 0
    people.sort()
    start, end = 0, len(people)-1

    while start <= end :
        answer += 1
        if people[start] + people[end] <= limit :
            start += 1
        end -= 1
    return answer


def my_wrong_solution1(people, limit):
    answer = 1
    people.sort() #오름차순 정렬
    weight = 0
    for i in range(len(people)) :
        if people[i] == 0 : continue # 이미 반영됨
        weight += people[i]
        needs = limit-weight
        if needs < 0 : # 보트를 탈 수 없다면
            answer += 1 # 새 보트 준비 (보트 개수 카운트하는 타이밍 : 보트 다 차고 새로운 보트 준비할 때)
            weight = people[i] # 새 보트에 사람 태우기
            continue
        elif needs == 0 : # 보트에 나 혼자 들어가야 한다면
            answer += 1 # 새로운 보트 준비
            weight = 0
            continue
        else : # 보트에 탈 수 있다면
          try :
              idx = people.index(needs, i+1)  # 나만큼 들어갈 수 있는 보트 찾기
              weight = 0
              people[idx] = 0
              answer +=1
          except : # 그런 보트 없으면
              continue # 다음 탐색
                # 로직 오류 : if, elif,try 모두 해당안되고 except까지 온 케이스 처리 안해줌
    if not weight : answer -= 1
    return answer

# [ 풀이 ]
# 조건: 사람 최대 5만명
# 문제 제대로 안읽어서 어렵게 풀었음
# 보트에 탈 수 있는 최대 인원 2명!!!!!!!!!!
# 내가 찾은 반례  [20,30,40,50,60]
# [20, 30, 50], [40,60] 으로 나눌 수 있어야 한다고 생각했음

# 1차 풀이 :
# 1. 자신이 타면 만석이 되는 보트를 찾는다
# 2. 그런 보트가 없다면
# 테스트 케이스만 맞음
# 정확성: 20.0
# 효율성: 15.0
# 합계: 35.0 / 100.0


# 2차 풀이 : <- 순차적으로 접근해서 접근 방식이 처음부터 틀렸음
# while문 안 if, else 거치면서 i (인덱스) 값 다른 방식으로 증가시켜야 했음
# -> flag로 관리
def my_wrong_solution2(people, limit):
    max_boat = len(people) #실수
    boat = [ limit for i in range(max_boat)]
    people.sort()
    boat[0] -= people[0]
    answer = 1
    print(boat)
    for w in range(1,len(people)) :
      weight = people[w]
      i = 0
      dif = limit
      # while문 돌면서 자기 weight 만큼의 총량 있는지 확인 (100만날때까지)
      # 없으면 들어갈 수 있는 가장 작은 수에 들어감 (차이가 적을수록이 기준)
      # 새보트 타기 전까지 (100 만나기 전까지)
      flag = False
      while True :
        print(i)
        if boat[i] - weight >=0 and dif > boat[i]-weight:
          dif = boat[i]-weight
          flag = False
        if boat[i] == 100 :
          if flag : i -= 1
          break
        i += 1
        flag = True
      boat[i] -= weight
    try :
      answer = boat.index(100)
    except :
      answer = max_boat
    return answer
