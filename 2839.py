#설탕 배달 문제
#N = 18일때, 3킬로 6개도 > 5킬로3개 3킬로 1개한개
#점화식 문제
# An = min(A(n-3) + 1, A(n-5) + 1)
#N < 5000 재귀 X

N = int(input())
list = [5000]*(N+1)
for i in range(3,N+1):
  if i == 3:
    list[i] = 1
  elif i == 5:
    list[i] = 1
  else:
    list[i] = min(list[i-3]+1, list[i-5]+1)
    
if list[N] >= 5000:
  print(-1)
else:
  print(list[N])
