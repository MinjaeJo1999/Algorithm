def solution(s):
    answer = ''
    i = 0
    tmp = ''
    dic = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
           'eight': '8', 'nine': '9'}
    keyList = dic.keys()
    while True:
        if i == len(s): break
        if s[i].isdigit():
            answer += s[i]
        else:
            tmp += s[i]
            if tmp in keyList:
                answer += dic[tmp]
                tmp = ''  # 실수 : 초기화 시점
        i += 1

    return int(answer)

s = "one4seveneight"
print(solution(s))

# [ 풀이 ]
# 더 나은 코드 :
# 로직은 동일
# 굳이 딕셔너리 사용하지 않고, 리스트의 인덱스-데이터로 매칭시킬 수 있음 -> arr.index(tmp)
# [ 문법 ]
# isdigit() 외에 isnumeric()도 있음
# 차이 : digit은 단일 글자가 숫자모양으로 생겼으면 True를 리턴하고 isnumeric은 숫자값 표현에 해당하는 텍스트까지 인정
# + isdecimal() 함수는 주어진 문자열이 int형으로 변환이 가능한지 알아내는 함수