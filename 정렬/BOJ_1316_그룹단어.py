def check(word) :
    alphabet = [0 for _ in range(26)]
    idx = ord(word[0]) - ord('a')
    alphabet[idx] += 1
    for i in range(1, len(word)) :
        idx = ord(word[i]) - ord('a')
        if word[i] != word[i-1] and alphabet[idx]!=0 :
            return False
        alphabet[idx] += 1
    return True

n = int(input())
words =[]
cnt = 0
for i in range(n) :
    words.append(input())
    if(check(words[i])) :
        cnt += 1
print(cnt)

# 더 나은 솔루션 (참고 : https://ooyoung.tistory.com/79)
def sol() :
    N = int(input())
    cnt = N

    for i in range(N):
        word = input()
        for j in range(0, len(word) - 1):
            if word[j] == word[j + 1]:
                pass
            elif word[j] in word[j + 1:]:
                cnt -= 1
                break

    print(cnt)

# **주의
# [ 문법 ]
# 알파벳 숫자 변환 : ord() , 아스키코드 문자 변환 : chr()
# [ 풀이 ]
# 내 풀이 메모리 사용이 더 큼 (alphabet 리스트 사용 때문에)
# 현재 인덱스 이전 혹은 이후 부분의 내용을 탐색할 때 리스트 슬라이싱 적극 활용