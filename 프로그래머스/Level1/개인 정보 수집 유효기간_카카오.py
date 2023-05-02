# 링크: https://school.programmers.co.kr/learn/courses/30/lessons/150370

def my_solution(today, terms, privacies):
    answer = []
    today_year, today_month, today_day = map(int, today.split('.'))

    # 약관 종류 딕셔너리 생성
    dic = {}
    for term in terms:
        name, month = map(str, term.split(' '))
        dic[name] = int(month)  # 실수 방지, 형변환

    # for , 프라이버시
    for i in range(len(privacies)):
        target = privacies[i]
        # 문자열 파싱
        # 년도, 달, 일 / 약관 종류
        year = int(target[:4])
        month = int(target[5:7])
        day = int(target[8:10])
        term = target[-1]

        # 약관 종류에 따라서 달에 +n
        month += dic[term]
        # 만약 12 넘었으면 %12 , // 연산으로 몫만큼 년도 추가
        if month > 12:
            a, b = divmod(month, 12)
            # 실수 : 나머지가 0일 경우 예외처리
            if b == 0:
                month = 12
                year += (a - 1) # > month 12, 기간 12인 경우 예외처리 (24%12 => 2 이므로 1년 더 뛰어넘는 오류 생김)
            else:
                month = b  # 실수 (=, 나머지를 대입해야)
                year += a  # 실수 (몫을 더해야)

        # 일 : 현재 일 -1
        # 만약 0이면 28로 변경 , 달도 -1 (결과 0이면 12로 변경)
        day -= 1
        if day == 0:
            day = 28
            month -= 1
            # 연산 시 0이 나올 경우 예외처리 수행해야
            if month == 0:
                month = 12
                year -= 1
        print(year, month, day)

        # 실수 : 파기해야 할 정보를 append
        # 계약일 < 현재 날짜인 케이스 append
        if today_year < year:
            continue
        elif today_year == year:
            if today_month < month:
                continue
            elif today_month == month:
                if today_day <= day:  # 실수 : 날짜 똑같으면 파기 의무 x
                    continue

        answer.append(i + 1)

    return answer

# 실수 많았음
# 14, 17 TC 불통과
# month 12 , 기간 12 인 경우 / 12-1월 or 28-1일 경계처리 해준 뒤 통과

# <더 나은 솔루션>
# > 양적 시간으로 접근
# 2000 ≤ YYYY ≤ 2022 이므로 2000 빼고 시작해도 될 것 같음
#출처 : https://velog.io/@isayaksh/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Programmers-%EA%B0%9C%EC%9D%B8-%EC%A0%95%EB%B3%B4-%EC%88%98%EC%A7%91-%EC%9C%A0%ED%9A%A8%EA%B8%B0%EA%B0%84-Python-7a0bfe4f
def dateToDay(date):
    year, month, day = map(int, date.split("."))
    return (year * 12 * 28) + (month * 28) + day


def solution(today, terms, privacies):
    answer = []

    # today
    today = dateToDay(today)

    # terms
    termsInfo = dict()
    for term in terms:
        term = term.split()
        termsInfo[term[0]] = int(term[1]) * 28

    # privacies
    for i in range(len(privacies)):
        date, term = privacies[i].split()
        if dateToDay(date) + termsInfo[term] <= today:
            answer.append(i + 1)

    return answer