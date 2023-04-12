def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)) :
        sum = 0
        for j in range(len(photo[i])) :
            if photo[i][j] in name: #실수방지 : i, j 누락시키지 않기
                idx = name.index(photo[i][j]) #실수방지 : index 없으면 ValueError 나므로 name 안에 존재 유무 먼저 확인
                sum += yearning[idx]
        answer.append(sum) #두번째 for문 통과 후 append
    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
print(solution(name,yearning,photo)) # [19, 15, 6]