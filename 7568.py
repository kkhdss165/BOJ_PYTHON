#덩치
#A B를 (x, y), (p, q)라고 할 때 x > p 그리고 y > q  A가 B보다 "더 크다"
#만일 자신보다 더 큰 덩치의 사람이 k명이라면 그 사람의 덩치 등수는 k+1이 된다. 

N = int(input())
list = []
for i in range(N):
  weight, height = map(int, input().split())
  list.append((weight, height))
  
ranking = [-1] * N

for i in range(N):
  count = 0
  for j in range(N):
    if i != j:
      if (list[j][0] > list[i][0] and list[j][1] > list[i][1]):
        count = count + 1
  ranking[i] = count + 1
  
print(*ranking)
