#소수 출력

testCase = int(input())

list = list(map(int, input().split()))
max_value = max(list)
check = [True] * (max_value+1)

if max_value >= 1:
  check[0] = False
  check[1] = False

for i in range(2,max_value+1):
  for j in range(i+1,max_value+1):
    if j % i == 0 and check[j] == True:
      check[j] = False

count = 0
for i in list:
  if check[i]:
    count = count + 1

print(count)
