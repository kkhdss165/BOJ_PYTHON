# 11657 번
# 최단경로 타임머신 추가

import sys
import heapq
from collections import deque
input = sys.stdin.readline
inf = sys.maxsize
def solution():
    N, M = map(int, input().split())

    graph = []
    for _ in range(M):
        A, B, C = map(int, input().split())
        graph.append((A, B, C))


    visited = [ inf ] * (N+1)
    heap = []

    def BF(start):
        visited[start] = 0
        for i in range(N):
            for j in range(M):
                node = graph[j][0]
                next_node = graph[j][1]
                cost = graph[j][2]

                if visited[node] != inf and visited[next_node] > visited[node] + cost:
                    visited[next_node] = visited[node] + cost
                    if i == N - 1:
                        return True

        return False

    negative_cycle = BF(1)

    if negative_cycle:
        print('-1')
    else:
        for i in range(2, N+1):
            if visited[i] == inf:
                print('-1')
            else:
                print(visited[i])

solution()
