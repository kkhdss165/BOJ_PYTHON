n, m = map(int, input().split())

list = list(map(int, input().split()))

result = []
for x in list:
  if x < m:
    print(x, end=" ")
