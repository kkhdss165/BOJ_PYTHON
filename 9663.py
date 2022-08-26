# N-Queen 9663
# https://www.acmicpc.net/problem/9663
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.
# 같은 직선이 있지 않고, 대각선으로 안만남
# 대각선은 두 수의 차이, 두수의 합

import sys

#추가할때 기존의 것과 추가한것만 탐색
def check(n):
  for i in range(n):
    if rows[i] == rows[n]:
      return False
    if n - i == abs(rows[n]-rows[i]):
      return False
  return True

N = int(sys.stdin.readline())

count = 0
rows = [0] * N
visited = [False] * N

def DFS(x):
  global count
  if x == N:
    count += 1
  else:
    for y in range(N):
      rows[x] = y
      if check(x):
        visited[x] = True
        DFS(x+1)
        visited[x] = False
        
DFS(0)

print(count)
