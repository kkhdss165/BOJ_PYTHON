# 2606 번
import sys
from collections import deque
from collections import Counter
input = sys.stdin.readline

def solution():
    # 컴퓨터수
    N = int(input())
    # 간선
    M = int(input())

    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        src, dst = map(int, input().split())
        graph[src].append(dst)
        graph[dst].append(src)

    # print(graph)

    visited = [False] * (N+1)

    def BFS(start):
        que = deque()
        que.append(start)

        while que:
            now = que.popleft()
            for next in graph[now]:
                if visited[next] == False:
                    visited[next] = True
                    que.append(next)

    BFS(1)
    print(Counter(visited)[True] - 1)

solution()
