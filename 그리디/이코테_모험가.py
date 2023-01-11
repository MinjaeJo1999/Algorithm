n = int(input())
p = map(int, input().split())
p.sort()

group = 0
count = 0

for i in p:
    group += 1
    if i <= group:
        count += 1
        group = 0
    # else : > 마지막 단계에서 count 되지 못할 수도
    # group += 1
print(count)

# ***주의
# 입력 문자열의 list화
# for문 in 다음 대상 적절한 것으로 선택 (배열 자체거나 인덱스 값이거나)