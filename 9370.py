# 9370 번
# g,h를 거처가는 경로가 최단경로 이면 출력

import sys
import heapq
from collections import deque
input = sys.stdin.readline
inf = sys.maxsize
def solution():
    T = int(input().rstrip())
    for _ in range(T):
        # 교차로, 도로, 목적지 후보
        n, m, t = map(int, input().split())
        # 예술가 출발지, g, h
        s, g, h = map(int, input().split())

        graph = [[] for _ in range(n+1)]
        dst = []

        # 양방향 도로
        for _ in range(m):
            a, b, d = map(int, input().split())
            graph[a].append((b ,d))
            graph[b].append((a, d))

        # 목적지 후보
        for _ in range(t):
            x = int(input().rstrip())
            dst.append(x)

        def BFS(start):
            visited = [-1 for _ in range(n+1)]
            visited[start] = 0
            heap = []
            heapq.heappush(heap, (0, start))

            while heap:
                now_dis , now_node = heapq.heappop(heap)
                for next_node, plus_dis in graph[now_node]:
                    next_dis = now_dis + plus_dis
                    if visited[next_node] == -1 or visited[next_node] > next_dis:
                        visited[next_node] = next_dis
                        heapq.heappush(heap, (next_dis, next_node))

            return visited

        s_start = BFS(s)
        g_start = BFS(g)
        h_start = BFS(h)
        dst.sort()
        for d in dst:
            if min(s_start[g] + g_start[h] + h_start[d], s_start[h]+ h_start[g] + g_start[d]) == s_start[d]:
                print(d)

solution()
