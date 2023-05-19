# 내풀이 : 실패
for test_case in range(1, 11):
    n = int(input())
    buildings = list(map(int, input().split('')))
    answer = 0

    for i in range(2, n-2):  # 마지막 2개는 높이 0
        height = buildings[i]
        left = max(buildings[i-2:i])
        right = max(buildings[i+1:i+3])
        if left >= height or right >= height:
            continue
        max_height = left if left >= right else right
        answer += (height - max_height)

    print("#"+test_case, answer)
# Error Message:
# Memory error occured, (e.g. segmentation error, memory limit Exceed, stack overflow,... etc)
# 해결 못함

# 다른 풀이 (출처 : https://whitehairhan.tistory.com/m/278)
for test_case in range(1,11):
    result = 0
    houseCount = int(input())
    house = list(map(int , input().split()))
    for i in range(2, houseCount-2):
        arMax = max(house[i-1],house[i-2],house[i+1],house[i+2])
        if house[i] > arMax:
            result += ( house[i] - arMax )

    print("#{} {}".format(test_case,result))