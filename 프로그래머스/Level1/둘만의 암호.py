def solution(s, skip, index):
    answer = ''
    skip = list(skip)
    for i in range(len(skip)):
        skip[i] = ord(skip[i]) - ord('a')
    for alpha in s:
        idx = 0
        temp = ord(alpha) - 97
        while idx < index:
            test = (temp + 1) % 26 # 실수 방지 : 확인할 때도 %26된 값으로 해야만
            if test in skip:
                temp += 1 # 실수 방지 : temp 값은 증가시켜야 무한루프 돌지 않음
                temp %= 26 # 실수 방지 : z 다음은 a
            else:
                idx += 1
                temp += 1
                temp %= 26
        temp = chr(temp + ord('a'))
        answer += temp
        # abcdefghi

    return answer

#result = happy
s = "aukks"
skip = "wbqd"
index = 5

#result = bbbbb
s = "zzzzz"
skip = "a"
index = 1
