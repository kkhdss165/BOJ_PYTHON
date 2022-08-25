# N과 M (2) 15650
# https://www.acmicpc.net/problem/15650
# DFS

N, M = map(int, input().split())

values = []

def DFS(start):
  if len(values) == M:
    print(*values)
    return
  else:
    for i in range(start,N+1):
      if i not in values:
        values.append(i)
        DFS(i+1)
        values.pop()

DFS(1)
