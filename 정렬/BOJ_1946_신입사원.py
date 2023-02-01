# 링크 : https://www.acmicpc.net/problem/1946
import sys

def accept(array) :
    array.sort(key = lambda x: x[0])
    result = 1 #서류 전형 1등을 미리 합격시키고 시작
    standard = array[0][1]
    for i in range(1, len(array)) :
        if array[i][1] < standard : #  if array[i][1] < array[i-1][1] :
            result += 1
            standard = array[i][1]
    return result

t = int(input())
answer = []
for _ in range(t) :
    n = int(input())
    score = []
    for j in range(n) :
        score.append(list(map(int, sys.stdin.readline().split())))
    answer.append(accept(score))

for i in answer :
    print(i)


# ***주의
# [ 문법 ]
# array.sort(key = lambda x : (a, b) )
# 인덱스 실수 주의 : 순서쌍 배열 만들어준 거 까먹고 인덱스 하나만 써서 비교함 ex) array[i] < array[i-1]
# [ 풀이 ]
# 주어진 데이터 '성적'으로 읽어서 문제 해석에 어려움이 있었음, 성적이 아니고 순위!
# 두 분야의 순위가 모두 낮은 비교군이 있을 경우 탈락 <- 이렇게 올바른 이해를 하기까지 시간이 걸렸음
# <시간 초과 에러>
#   >  sys.stdin.readline()로 해결
#   > 사용 습관화 하자!
# <틀렸습니다!>
#   > 앞의 순위랑 비교 시 기준을 바로 앞 데이터의 순위랑 비교하면 안됨
#   > 해당 데이터는 탈락한 데이터일 수도 있기 때문