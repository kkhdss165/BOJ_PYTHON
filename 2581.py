#소수 출력

M = int(input())
N = int(input())

check = [True] * (N+1)

if N >= 1:
  check[0] = False
  check[1] = False

for i in range(2,N+1):
  for j in range(i+1,N+1):
    if j % i == 0 and check[j] == True:
      check[j] = False

sum = 0
min = None
for i in range(M, N+1):
  if check[i]:
    if min == None:
      min = i
      
    sum = sum + i

if sum != 0:
  print(sum)
  print(min)
else:
  print(-1)
