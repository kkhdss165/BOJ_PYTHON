# N과 M (3) 15651
# https://www.acmicpc.net/problem/15651
# DFS

N, M = map(int, input().split())

values = []

def DFS():
  if len(values) == M:
    print(*values)
    return
  else:
    for i in range(1,N+1):
      values.append(i)
      DFS()
      values.pop()

DFS()
