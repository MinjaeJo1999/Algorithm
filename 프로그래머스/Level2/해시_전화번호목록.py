# 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    dic = {}
    for i in phone_book:
        dic[i] = 0

    for target in phone_book:
        for j in range(len(target)):
            if target[:j] in dic: # dic -> 리스트에서 찾으면 시간 초과, 딕셔너리로 해결
                return False
    return True

# [ 풀이 ]
# 같은 맥락에서 계속 실수
# 자기 번호 제외하고 검사해야 / 자기 자신을 찾는 경우 예외 처리
# 번호 순서대로 입력하면서 검사하면 안됨 > 뒤에 번호가 접두사 될 수 있음
# *** 조건 잘 확인
# > "같은 전화번호가 중복해서 들어있지 않습니다."
# > 자기 자신 피하고 싶다면 n-1까지만 검사해주면 됨

# 첫 풀이 :
# TC 8,9,19 실패
# 효율성 테스트 TC 절반 시간 초과
# 합계: 79.2 / 100.0

# 2차 풀이 :
# 합계: 91.7 / 100.0
# 효율성 테스트 시간 초과
# -> 데이터 딕셔너리에 다시 저장해서 해결

# 이해 못한 풀이
# 출처 : https://school.programmers.co.kr/questions/44634

def solution(phone_book):
    lens = set([len(i) for i in phone_book])
    for i in lens:
        nolen = [x[:i] for x in phone_book if len(x) != i]
        yeslen = [x[:i] for x in phone_book if len(x) == i]
        if set(nolen) & set(yeslen):
            return False
    return True


# [ 문법 ]
# 딕셔너리, 딕셔너리 함수 사용
# 셋, 셋 함수 사용
