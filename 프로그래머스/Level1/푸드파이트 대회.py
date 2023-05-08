def solution(food):
    answer = ''
    right = ''
    for i in range(1,len(food)) :
        for _ in range(food[i]//2) :
                right += str(i)
    left = "".join(reversed(right))
    answer = right + '0' + left
    return answer


#출처 : https://dduniverse.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%91%B8%EB%93%9C-%ED%8C%8C%EC%9D%B4%ED%8A%B8-%EB%8C%80%ED%9A%8C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python
''' 더 간단한 로직 (이중 for문 해소, 최소 메모리 활용)
 for i in range(1, len(food)):
        temp += str(i) * (food[i]//2)
    return temp + '0' + temp[::-1]
'''

# [ 풀이 ]
# [ 문법 ]
# reversed() 사용법
# "".join(reversed(right))