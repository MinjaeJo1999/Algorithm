# ***주의
# [ 풀이 ]
# 시뮬레이션으로 접근했을 때 (배열 돌면서 앞뒤 값이 차이 비교, (start, end) 저장) 고려해야 할 예외사항이 너무 많음
# > 문제 잘못 이해함 .. 리스트 전체가 수열임
# k 값이 되는 것을 조건으로 두어 for문 순서대로 더하면 중간 조합 찾지 못하게 됨
# for문 말고 while문 사용해야 앞/뒤 요리조리 빼고 더할 수 있음 (인덱스로)
# 완전 탐색, 부분합 수열, 분할 정복, 동적 계획법 풀이 가능 : https://shoark7.github.io/programming/algorithm/4-ways-to-get-subarray-consecutive-sum
# 참고 : https://velog.io/@gomhyeok/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4%EC%97%B0%EC%86%8D%EB%90%9C-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4%EC%9D%98-%ED%95%A9
def solution(sequence, k):
    answer = []
    start = 0
    end = 0
    tmpStart = 0
    tmpEnd = 0
    dist = 1000001
    sum = sequence[0] #반드시 초기화

    while start < len(sequence) :
        if end == len(sequence)-1 : #인덱스 에러 방지
            if sum < k :
                break
        # sum < k 인 경우
        if sum < k :
            end += 1
            sum += sequence[end] #인덱스 에러 주의
        elif sum > k :
            sum -= sequence[start]
            start += 1
        elif sum == k :
            if (end - start) < dist :
                dist = (end - start)
                tmpStart = start
                tmpEnd = end
            sum -= sequence[start]
            start += 1
    answer.append(tmpStart)
    answer.append(tmpEnd)
    return answer

sequence = [1, 2, 3, 4, 5]
k = 7
print(solution(sequence, k))



