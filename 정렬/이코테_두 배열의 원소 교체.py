n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() #오름차순
b.sort(reverse=True) # 내림차순

for i in range(k) :
    if a[i] < b[i] :
        a[i], b[i] = b[i], a[i]
    else:
        break


result = 0
for i in range(len(a)) :
    result += a[i]

print(result)
# print(sum(a))

# 주의
# [ 문법 ]
# 파이썬 sort 함수 사용법
# > 내림차순 : sort.(reverse=True)
# 리스트의 합계 구할 때 sum() 함수 사용하자
# [ 풀이 ]
# for문 돌때는 if 조건문을 통해 중간에 break할 수 있는 경우를 반드시 고려해야
