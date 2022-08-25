# N과 M (1) 15649
# https://www.acmicpc.net/problem/15649
# DFS

N, M = map(int, input().split())

values = []

def DFS():
  if len(values) == M:
    print(*values)
    return
  else:
    for i in range(1,N+1):
      if i not in values:
        values.append(i)
        DFS()
        values.pop()

DFS()
