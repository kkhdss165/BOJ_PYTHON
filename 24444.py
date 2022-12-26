# 24444
# https://www.acmicpc.net/problem/24444
# BFS
from collections import deque

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    src, dst = map(int, input().split())
    # print(src, dst)
    graph[src].append(dst)
    graph[dst].append(src)

for sub_graph in graph:
    sub_graph.sort()

visited = [0] * (N + 1)

def BFS(start):

    que = deque()
    que.append(start)

    visited[start] = 1
    count = 1

    while que:
        now = que.popleft()
        for i in graph[now]:
            if visited[i] == 0:
                count += 1
                visited[i] = count
                que.append(i)

BFS(R)

for v in visited[1:]:
    print(v)
