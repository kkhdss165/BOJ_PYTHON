#OX문제 연속으로 정답이면 추가 점수 1점(콤보)

n = int(input())
for i in range(n):
  ans = input()
  combo = 0
  sum = 0
  for ch in ans:
    if ch == 'O':
      combo = combo + 1
      sum = sum + combo
    else:
      combo = 0
  print(sum)
