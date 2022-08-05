a = list(map(str, input().split()))

for index, value in enumerate(a):
  a[index] = value[::-1]

a = list(map(int, a))
print(max(a))
