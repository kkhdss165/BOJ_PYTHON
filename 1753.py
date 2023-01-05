# 1753 번
# 최단경로

import sys
import heapq
from collections import deque
input = sys.stdin.readline

def solution():
    V, E = map(int, input().split())
    K = int(input().rstrip())

    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append([v, w])

    # print(graph)

    visited = [-1 for _ in range(V+1)]

    heap =[]

    # print(visited)
    def BFS(start):
        visited[start] = 0
        heapq.heappush(heap, (0, start))

        while heap:
            weight, now = heapq.heappop(heap)

            for next, nw in graph[now]:
                next_wei = weight + nw

                if next_wei < visited[next] or visited[next] == -1:

                    visited[next] = next_wei
                    heapq.heappush(heap, (next_wei, next))

    BFS(K)
    # print(visited)
    for i in visited[1:]:
        print('INF' if i == -1 else i)

solution()
