# 24445 번
import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0 for _ in range(N+1)]

def BFS(start):
    que = deque()
    que.append(start)

    count = 1
    visited[start] = count

    while que:
        now = que.popleft()

        temp_graph = graph[now]
        temp_graph.sort(reverse= True)
        for next in temp_graph:
            if visited[next] == 0:
                count += 1
                visited[next] = count
                que.append(next)

        # print(visited)

BFS(R)

for i in visited[1:]:
    print(i)
