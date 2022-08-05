testCase = int(input())

for i in range(testCase):
  n, a = input().split()
  for ch in a:
    for j in range(int(n)):
      print(ch,end="")
  print()
