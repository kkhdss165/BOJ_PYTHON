##ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고
##kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만
##aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
##같은 종류의 알파벳끼리 붙어 있어야함

testCase = int(input())
count = 0
for t in range(testCase):
  a = input()
  check = [False]*26
  before = ''
  is_group = True
  for ch in a:
    #전의 문자와 다른 경우
    if ch != before:
      if check[ord(ch)-97] == False:
        before = ch
        check[ord(ch)-97] = True
      else:
        is_group = False
        break
        
  if is_group:
    count = count + 1
  
print(count)
