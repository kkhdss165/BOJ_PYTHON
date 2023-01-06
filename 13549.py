# 13549 번
# 숨바꼭질

import sys
import heapq
from collections import deque
input = sys.stdin.readline
inf = sys.maxsize
def solution():
    max_size = 100000
    plus_weight = [1,1,0]
    N, E = map(int, input().split())

    visited = [-1 for _ in range(max_size + 1)]

    heap = []

    def BFS(start):
        visited[start] = 0
        heapq.heappush(heap, (0, start))

        while heap:
            weight, now_node = heapq.heappop(heap)

            next_list = [now_node+1, now_node-1, 2* now_node]
            for idx, next_node in enumerate(next_list):
                next_weight = weight + plus_weight[idx]
                if next_node >= 0 and next_node <= max_size:
                    if visited[next_node] > next_weight or visited[next_node] == -1:
                        visited[next_node] = next_weight
                        heapq.heappush(heap, (next_weight, next_node))

    BFS(N)
    # print(visited)
    print(visited[E])

solution()
