
# 할 수 있는 실수를 모두 저지른 오답
input = input()
result = ''
sum = 0

for i in range(len(input)):
    if input[i] >= 'A' and input[i] <='Z': #유효한지 확인
        result = result + input[i]
    else :
        sum += int(input[i])

result = result + str(sum)
print(result)


# 정답
def sol() :
    data = input()
    result = []
    value = 0

    #문자를 하나씩 확인하며
    for x in data :
        #알파벳인 경우 결과 리스트에 삽입
        if x.isalpha() :
            result.append(x)
        else : value += int(x)

    #알파벳을 오름차순으로 정렬
    result.sort()

    #숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
    if value != 0 :
        result.append(str(value))

    #리스트를 문자열로 변환하여 출력
    print(''.join(result))

# ***주의
# 조건 충족했는지 체크 (알파벳 오름차순 조건 까먹음)
# 예외 조건 체크 (숫자가 존재하지 않을 경우 고려안함)
# isalpha 함수
# append 함수 (extend, insert 함수와 같이 기억)
# join 함수 (EX: '구분자'.join(리스트) )