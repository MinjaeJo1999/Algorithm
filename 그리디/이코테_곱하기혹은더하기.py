# 링크: https://www.youtube.com/watch?v=2zjoKjt97vQ&feature=emb_rel_pause

s = input()
result = int(s[0])

for i in range(1, len(s)):
  num = int(s[i])
  if num <= 1 or result <=1 :
    result += num
  else :
    result *= num

print(result)

# ***주의
# 입력받은 문자열 int 처리
# range 함수 활용법
# 0,1이 예외 숫자가 된다는 것